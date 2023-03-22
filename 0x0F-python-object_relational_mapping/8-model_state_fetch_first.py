#!/usr/bin/python3
"""
A script that prints the first State object from the database hbtn_0e_6_usa
The script should take 3 arguments: mysql username, mysql password and database name
The module SQLAlchemy must be used
Import State and Base from model_state - from model_state import Base, State
Script should connect to a MySQL server running on localhost at port 3306
The state displayed must be the first in states.id
Fetch all states from the database before displaying the result is not allowed
If the table states is empty, print Nothing followed by a new line
Code should not be executed when imported
"""
import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)

    session = Session()

    state = session.query(State).order_by(State.id).first()
    if state is not None:
        print('{0}: {1}'.format(state.id, state.name))
    else:
        print("Nothing")
