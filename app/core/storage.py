import json
import os
from app.models.pet_model import Pet

PET_FILE = "get_data.json"

def save_pet(pet: Pet):
    with open(PET_FILE, "w") as f:
        json.dump(pet.to_dict(), f)

def load_pet() -> Pet:
    if not os.path.exists(PET_FILE):
        return None
    with open(PET_FILE, "r") as f:
        data = json.load(f)
        return Pet.from_dict(data)

