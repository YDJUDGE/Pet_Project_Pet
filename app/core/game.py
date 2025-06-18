from datetime import datetime
from app.models.pet_model import Pet

class PetGame:
    @staticmethod
    def update_pet(pet: Pet) -> Pet:
        """Обновляет состояние питомца"""
        last_updated = datetime.fromisoformat(pet.last_updated)
        now = datetime.now()
        delta_minutes = (now - last_updated).total_seconds() / 60

        if delta_minutes < 1:
            return pet

        for _ in range(int(delta_minutes)):
            if pet.status == "dead":
                break

            pet.age += 1
            pet.health = max(0, pet.health - (5 if pet.hunger > 70 else 2))
            pet.hunger = min(100, pet.hunger + 3)
            pet.mood = (pet.health + (100 - pet.hunger)) // 2

            if pet.health <= 0 or pet.hunger >= 100:
                pet.status = "dead"
            elif pet.health <= 30:
                pet.status = "sick"
            else:
                pet.status = "alive"

        pet.last_updated = now.isoformat()
        return pet

    @staticmethod
    def feed(pet: Pet) -> Pet:
        """Покормить питомуа"""
        pet.hunger = max(0, pet.hunger - 30)
        pet.mood = min(100, pet.mood + 10)
        return pet

    @staticmethod
    def heal(pet: Pet):
        """Вылечить питомца"""
        pet.health = min(100, pet.health + 20)
        pet.hunger = min(100, pet.hunger + 10)
        return pet

    @staticmethod
    def play(pet: Pet) -> Pet:
        """Поиграть с питомцем"""
        pet.mood = min(100, pet.mood + 15)
        pet.hunger = min(100, pet.hunger + 5)
        return pet

    @staticmethod
    def update_status(pet: Pet) -> Pet:
        """Получить состояние питомца"""
        pet.mood = (pet.health + (100 - pet.hunger)) // 2
        if pet.health <= 0 or pet.hunger >= 100:
            pet.status = "dead"
        elif pet.health <= 30:
            pet.status = "sick"
        else:
            pet.status = "alive"
        return pet
