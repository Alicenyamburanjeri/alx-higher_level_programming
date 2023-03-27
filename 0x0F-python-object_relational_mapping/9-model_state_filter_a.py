#!/usr/bin/python3
"""
A script that lists all State objects
contain letter a from the database hbtn_0e_6_usa
The script should take 3 arguments:
mysql username, mysql password and database name
Use the module SQLAlchemy
Import State and Base from model_state
Results must be sorted in ascending order by states.id
Your code should not be executed when imported
"""

import sys
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.
                           format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(
        State.id).filter(State.name.like('%a%'))

    for state in states:
        print('{}: {}'.format(state.id, state.name))
