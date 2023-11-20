#!/usr/bin/python3
""" prints the State object with the name passed
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engi = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                         .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engi)
    Session = sessionmaker(bind=engi)
    sessi = Session()
    for instance in sessi.query(State).filter(State.name.like('%a%')):
        sessi.delete(instance)
    sessi.commit()
