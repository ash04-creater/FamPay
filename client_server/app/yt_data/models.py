from flask_sqlalchemy import SQLAlchemy
from app import db,SCHEMA_NAME
#db = SQLAlchemy(app)

class VideoDetails(db.Model):
    __table_args__=({"schema":SCHEMA_NAME})
    __tablename__='video_details'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description=db.Column(db.String(500))
    thumbnail_url=db.Column(db.String(100))
    publishtime=db.Column(db.DateTime)