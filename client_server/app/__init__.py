from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os,json
from sqlalchemy import MetaData
from dotenv import load_dotenv

load_dotenv()

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('SQLALCHEMY_DATABASE_URI')
app.config['POOL_SIZE']=20
app.config['MAX_OVERFLOW']=50

db = SQLAlchemy(app)

SCHEMA_NAME=os.getenv("SCHEMA_NAME")

from sqlalchemy import orm,create_engine
from sqlalchemy.orm import sessionmaker
engine=create_engine("postgresql://postgres:root@127.0.0.1:5432/postgres",pool_size=20, max_overflow=50)
Session=sessionmaker(bind=engine)

from app.yt_data.routes import search_api,get_api

app.register_blueprint(search_api)
app.register_blueprint(get_api)