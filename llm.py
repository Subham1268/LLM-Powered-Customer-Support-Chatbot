from openai import OpenAI

# ⚠️ Hardcoded API key (ONLY for local testing)
client = OpenAI(api_key=""
tools = [
    {
        "type": "function",
        "function": {
            "name": "create_issue",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {"type": "string"},
                    "title": {"type": "string"},
                    "description": {"type": "string"},
                    "category": {"type": "string"}
                },
                "required": ["customer_id", "title", "description", "category"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_issue",
            "parameters": {
                "type": "object",
                "properties": {
                    "issue_id": {"type": "string"}
                },
                "required": ["issue_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "list_issues",
            "parameters": {
                "type": "object",
                "properties": {
                    "customer_id": {"type": "string"}
                },
                "required": ["customer_id"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "update_issue",
            "parameters": {
                "type": "object",
                "properties": {
                    "issue_id": {"type": "string"},
                    "description_update": {"type": "string"}
                },
                "required": ["issue_id", "description_update"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "close_issue",
            "parameters": {
                "type": "object",
                "properties": {
                    "issue_id": {"type": "string"}
                },
                "required": ["issue_id"]
            }
        }
    }
]

def call_llm(message, customer_id):
    messages = [
        {
            "role": "system",
            "content": f"""
You are a customer support assistant.

User customer_id = {customer_id}

You can:
- Create issues
- Get issue details
- List issues
- Update issues
- Close issues

Only call tools when required.
If not required, respond normally.
"""
        },
        {
            "role": "user",
            "content": message
        }
    ]

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        tools=tools,
        tool_choice="auto"
    )

    return response.choices[0]