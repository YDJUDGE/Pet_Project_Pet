from fastapi import APIRouter, HTTPException
from app.models.pet_model import Pet
from app.core.game import PetGame
from app.core.storage import load_pet, save_pet

router = APIRouter(prefix="/pet", tags=["pet"])


@router.get("/")
async def get_pet():
    pet = load_pet()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    pet = PetGame.update_pet(pet)
    save_pet(pet)
    return pet


@router.post("/")
async def create_pet(name: str):
    if load_pet():
        raise HTTPException(status_code=400, detail="Pet already exists")

    pet = Pet(name=name)
    save_pet(pet)
    return pet


@router.post("/feed")
async def feed_pet():
    pet = load_pet()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    pet = PetGame.update_pet(pet)
    if pet.status == "dead":
        raise HTTPException(status_code=400, detail="Pet is dead")

    pet = PetGame.feed(pet)
    save_pet(pet)
    return pet


@router.post("/heal")
async def heal_pet():
    pet = load_pet()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    pet = PetGame.update_pet(pet)
    if pet.status == "dead":
        raise HTTPException(status_code=400, detail="Pet is dead")

    pet = PetGame.heal(pet)
    save_pet(pet)
    return pet


@router.post("/play")
async def play_with_pet():
    pet = load_pet()
    if not pet:
        raise HTTPException(status_code=404, detail="Pet not found")

    pet = PetGame.update_pet(pet)
    if pet.status == "dead":
        raise HTTPException(status_code=400, detail="Pet is dead")

    pet = PetGame.play(pet)
    save_pet(pet)
    return pet
