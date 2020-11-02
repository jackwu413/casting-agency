
import os
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy import Column, String, Integer, Date, create_engine 



database_name = "casting_agency"
database_path = "postgres://{}/{}".format('localhost:5432', database_name)

db = SQLAlchemy()

def setup_db(app): 
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    db.drop_all()
    db.create_all()


class Movie(db.Model): 
    __tablename__ = 'movies'

    id = Column(Integer, primary_key=-True)
    title = Column(String)
    release = Column(Date)


class Actor(db.Model): 
    __tablename__ = 'actors'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)
    gender = Column(String)

    def insert(self): 
        db.session.add(self)
        db.session.commit()

    def delete(self): 
        db.session.delete(self)
        db.session.commit()