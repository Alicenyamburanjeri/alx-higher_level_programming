#!/usr/bin/python3
"""
A script that adds the State object “Louisiana” to the database hbtn_0e_6_usa
The script should take 3 arguments: mysql username, mysql password and database name
The module SQLAlchemy is used
Import State and Base from model_state - from model_state import Base, State
The script should connect to a MySQL server running on localhost at port 3306
The new states.id should be printed after creation
The code should not be executed when imported
"""


m sys import argv
from model_state import State, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    print('{0}'.format(new_state.id))
    session.close()
