import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'usuario'
    id = Column(Integer, primary_key=True)
    user_name = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    favorites = relationship("Favourite", back_populates="usuario")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    description = Column(String(250))
    race = Column(String(250))
    favorites = relationship("Favourite", back_populates="character")

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    modelo = Column(String(250))
    max_speed = Column(Integer)
    favorites = relationship("Favourite", back_populates="vehicle")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250))
    terrain = Column(String(250))
    favorites = relationship("Favourite", back_populates="planet")

class Favourite(Base):
    __tablename__ = 'favourite'
    id = Column(Integer, primary_key=True)
    character_id = Column(Integer, ForeignKey('character.id'))
    vehicle_id = Column(Integer, ForeignKey('vehicle.id'))
    planet_id = Column(Integer, ForeignKey('planet.id'))
    usuario_id = Column(Integer, ForeignKey('usuario.id'))
    
    usuario = relationship("Usuario", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    vehicle = relationship("Vehicle", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")

def to_dict(self):
    return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e
