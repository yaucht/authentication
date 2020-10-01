from fastapi import FastAPI

from .routers import authenticate

app = FastAPI()
app.include_router(authenticate.router)
