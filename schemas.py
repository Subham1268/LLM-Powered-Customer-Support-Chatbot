from pydantic import BaseModel

class ChatRequest(BaseModel):
    message: str
    customer_id: str

class IssueCreate(BaseModel):
    customer_id: str
    title: str
    description: str
    category: str

class IssueUpdate(BaseModel):
    issue_id: str
    description_update: str