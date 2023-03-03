"""This file holds the logic that helps the file interact with the database"""

from sqlalchemy import create_engine, MetaData

engine = create_engine("mysql+pymysql://root@localhost:3306/fastapirefresher")

meta = MetaData()

conn = engine.connect()