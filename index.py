"""The entry point of yhe project
"""
from fastapi import FastAPI
from routes.user import user

app = FastAPI()

app.include_router(user)