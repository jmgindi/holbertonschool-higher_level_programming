#!/usr/bin/python3
"""This script  all states from hbtn_0e_6_usa with an 'a' in them
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
    for city, state in session.query(City, State).join(
            State).order_by(City.id):
        print("{}: ({}) {}".format(state.name, city.id, city.name))

