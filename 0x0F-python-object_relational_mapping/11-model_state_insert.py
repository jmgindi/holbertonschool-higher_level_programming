#!/usr/bin/python3
"""This script adds Louisiana to states in hbtn_0e_6_usa
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
    state = State(name="Louisiana")
    session.add(state)
    new_state = session.query(State).filter_by(name="Louisiana").first()
    print(new_state.id)
    session.commit()
