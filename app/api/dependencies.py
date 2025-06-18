from fastapi import HTTPException
from app.core.storage import load_pet
from app.models.pet_model import Pet

def current_game_pet() -> Pet:
    pet = load_pet()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")
    return pet
