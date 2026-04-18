from sqlalchemy.orm import Session
from support_bot.models import Issue

def create_issue(db: Session, data):
    issue = Issue(**data)
    db.add(issue)
    db.commit()
    db.refresh(issue)
    return issue

def get_issue(db: Session, issue_id: str):
    return db.query(Issue).filter(Issue.id == issue_id).first()

def list_issues(db: Session, customer_id: str):
    return db.query(Issue).filter(Issue.customer_id == customer_id).all()

def update_issue(db: Session, issue_id: str, desc: str):
    issue = get_issue(db, issue_id)
    if issue:
        issue.description += "\n" + desc
        db.commit()
        db.refresh(issue)
    return issue

def close_issue(db: Session, issue_id: str):
    issue = get_issue(db, issue_id)
    if issue:
        issue.status = "closed"
        db.commit()
        db.refresh(issue)
    return issue