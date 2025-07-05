from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="Pet Matching Service")
app.include_router(router)
