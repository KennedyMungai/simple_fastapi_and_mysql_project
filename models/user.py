"""The file contains the definition of the user model
"""
from sqlalchemy import Table, Column
from db import meta

users = Table(
    'users', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255)),
    Column('password', String(255)),
)