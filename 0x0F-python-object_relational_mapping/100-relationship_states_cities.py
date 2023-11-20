#!/usr/bin/python3


"""
All states via SQLAlchemy
"""
from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                        format(argv[1], argv[2], argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)

    sess = Session(eng)
    new_state = State(name='California')

    new_city = City(name='San Francisco')
    new_state.cities.append(new_city)

    sess.add(new_state)
    sess.commit()
    sess.close()
