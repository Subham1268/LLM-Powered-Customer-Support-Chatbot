from sqlalchemy import Column, String, Text
import uuid
from support_bot.database import Base

class Issue(Base):
    __tablename__ = "issues"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    customer_id = Column(String, nullable=False)
    title = Column(Text)
    description = Column(Text)
    category = Column(String)
    status = Column(String, default="open")