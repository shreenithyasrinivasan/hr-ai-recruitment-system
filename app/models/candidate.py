from sqlalchemy import Column, Integer, String
from app.db.database import Base

class Candidate(Base):
    __tablename__ = "candidates"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    resume_text = Column(String)
    ats_score = Column(Integer)
    stage = Column(String)
    