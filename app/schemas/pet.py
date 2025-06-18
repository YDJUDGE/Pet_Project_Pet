from pydantic import BaseModel

class PetCreate(BaseModel):
    name: str

class PetResponse(BaseModel):
    name: str
    age: int
    health: int
    hunger: int
    mood: int
    status: str
