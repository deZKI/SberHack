from pydantic import BaseModel
from typing import List

class MatchResult(BaseModel):
    matches: List[str]
    scores: List[float]
