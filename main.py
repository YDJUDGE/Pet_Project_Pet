from fastapi import FastAPI
from app.api.endpoints import router as pet_router
import uvicorn

app = FastAPI()
app.include_router(pet_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
