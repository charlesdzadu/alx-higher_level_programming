#!/usr/bin/python3
"""
All states via SQLAlchemy module
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session

if __name__ == "__main__":
    eng = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                        format(argv[1], argv[2], argv[3]),
                        pool_pre_ping=True)
    Base.metadata.create_all(eng)

    sess = Session(eng)
    new_obj = State(name='Louisiana')
    sess.add(new_obj)
    sess.commit()
    print(new_obj.id)
    sess.close()
