from fastapi import FastAPI
from health.router import router

app = FastAPI()

app.include_router(router)