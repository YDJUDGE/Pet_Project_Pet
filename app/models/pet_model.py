from pydantic import BaseModel
from datetime import datetime
from typing import Literal

PetStatus = Literal["alive", "sick", "dead"]


class Pet(BaseModel):
    name: str
    age: int = 0
    health: int = 100
    hunger: int = 0
    mood: int = 100
    status: PetStatus = "alive"
    last_updated: str = datetime.now().isoformat()

    def to_dict(self):
        return self.dict()

    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data)

