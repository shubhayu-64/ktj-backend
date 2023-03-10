from pydantic import BaseModel, Field
from typing import List


class TeamDBSchema(BaseModel):
    teamID: str
    teamLeadID: str
    teamMembers: List[str] = Field(min_length=1, max_length=10)
    eventName: str
    eventDescription: str
    