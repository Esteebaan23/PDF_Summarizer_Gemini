from pydantic import BaseModel
from typing import Optional

class QueryRequest(BaseModel):
    question: str
    session_id: Optional[str] = "default"

class QueryResponse(BaseModel):
    answer: str
    context_used: list[str]