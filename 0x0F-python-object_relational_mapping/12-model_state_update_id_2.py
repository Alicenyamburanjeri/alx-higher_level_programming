#!/usr/bin/python3
"""
A script that changes the name of a State object from the database hbtn_0e_6_usa
The script should take 3 arguments: mysql username, mysql password and database name, using the module SQLAlchemy
Import State and Base from model_state - from model_state import Base, State
The script should connect to a MySQL server running on localhost at port 3306
The name of the State where id = 2 should be changed to New Mexico
The code should not be executed when imported
"""
from sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).filter(State.id == 2).first()
    state.name = "New Mexico"
    session.commit()

    session.close()
