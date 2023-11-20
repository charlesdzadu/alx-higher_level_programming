#!/usr/bin/python3
""" prints the first State object from the database
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
    sess = Session()
    for instance in sess.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")
