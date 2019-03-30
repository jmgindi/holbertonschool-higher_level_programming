#!/usr/bin/python3
"""This script lists all states from hbtn_0e_6_usa with an 'a' in them
"""


from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

if __name__ == "__main__":
    eng = create_engine("mysql+mysqldb://{}:{}@localhost:3306/{}".format(
                        argv[1], argv[2], argv[3]))
    Base.metadata.create_all(eng)
    Session = sessionmaker(bind=eng)
    session = Session()
    for state in session.query(State).
            filter(State.name.like('%a%').
            order_by(State.id.asc()).all():
        print("{}: {}".format(state.id, state.name))
