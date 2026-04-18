# LLM-Powered-Customer-Support-Chatbot

Customer Support Chatbot powered by a Large
Language Model (LLM) that can interact with backend APIs to manage customer issues.
The chatbot will Understand user requests through natural language,Determine which backend API
to call.

1. main.py receives request
2. main.py → calls llm.py
3. llm.py → sends message to OpenAI
4. LLM decides which tool to call 
5. tools.py → calls crud.py
6. crud.py → interacts with DB via models.py
7. database.py → handles DB connection
8. Result goes back → main.py → user
