from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from support_bot.database import SessionLocal, engine
from support_bot import models
from support_bot.llm import call_llm
from support_bot.tools import handle_tool
from support_bot.schemas import ChatRequest
import json

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# DB Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/chat")
def chat(req: ChatRequest, db: Session = Depends(get_db)):
    try:
        llm_response = call_llm(req.message, req.customer_id)

        # If tool is called
        if llm_response.message.tool_calls:
            tool_call = llm_response.message.tool_calls[0]
            tool_name = tool_call.function.name

            args = json.loads(tool_call.function.arguments)

            result = handle_tool(tool_name, db, args)

            # Convert SQLAlchemy object to dict
            if hasattr(result, "__dict__"):
                result_data = {k: v for k, v in result.__dict__.items() if not k.startswith("_")}
            else:
                result_data = result

            return {
                "response": f"{tool_name} executed successfully",
                "data": result_data
            }

        # Normal LLM response
        return {
            "response": llm_response.message.content
        }

    except Exception as e:
        return {"error": str(e)}