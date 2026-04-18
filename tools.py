from support_bot.crud import (
    create_issue,
    get_issue,
    list_issues,
    update_issue,
    close_issue
)

def handle_tool(tool_name, db, args):
    if tool_name == "create_issue":
        return create_issue(db, args)

    elif tool_name == "get_issue":
        return get_issue(db, args["issue_id"])

    elif tool_name == "list_issues":
        return list_issues(db, args["customer_id"])

    elif tool_name == "update_issue":
        return update_issue(db, args["issue_id"], args["description_update"])

    elif tool_name == "close_issue":
        return close_issue(db, args["issue_id"])

    return {"error": "Unknown tool"}