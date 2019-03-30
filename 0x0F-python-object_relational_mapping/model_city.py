#!/usr/bin/python3
"""This module contains 1 class:
    City
"""
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State

class City(Base):
    """City class for use with SQLAlchemy
    Attributes:
        __tablename__: table to reference
        id: id of object instance
        name: string of max 128 chars not null
        state_id: foreign key to state
    """

    __tablename__ = "cities"
    id = Column(Integer, autoincrement=True,
                    nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
