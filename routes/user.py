from fastapi import APIRouter
from db import conn
from models.index import users

user = APIRouter()

@user.get('/')
async def read_data():
    return conn.execute(users.select()).fetchall()