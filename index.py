"""The entry point of yhe project
"""
from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def index():
    return {'Chickens R Us'}