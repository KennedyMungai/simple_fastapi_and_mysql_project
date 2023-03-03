from fastapi import APIRouter
from db import conn

user = APIRouter()

@user.get('/')
async def read_data():
    return conn.execute(users.select()).fetchall()