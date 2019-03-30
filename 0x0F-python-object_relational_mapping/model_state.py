#!/usr/bin/python3
"""This module contains 1 class:
    State
"""
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """State class for use with SQLAlchemy
    Attributes:
        __tablename__: table to reference
        id: id of object instance
        name: string of max 128 chars not null
    """

    id = Column(Integer, autoincrement=True,
                    nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
