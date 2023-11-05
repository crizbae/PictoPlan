from pydantic import BaseModel
from typing import Dict

class Item(BaseModel):
    Title: str
    SessionId: str
    Objective: str
    Materials: str
    Procedure: Dict[str, str]
    Assessment: str