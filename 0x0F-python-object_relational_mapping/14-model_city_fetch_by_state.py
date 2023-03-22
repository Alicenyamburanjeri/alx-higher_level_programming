#!/usr/bin/python3
"""
A script that prints all City objects from the database hbtn_0e_14_usa
The script should take 3 arguments: mysql username, mysql password and database name
Should use the module SQLAlchemy
Import State and Base from model_state - from model_state import Base, State
The script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
The code should not be executed when imported
"""

from sys import argv
from model_state import State, Base
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    db_url = "mysql+mysqldb://{}:{}@localhost:3306/{}".format(
        argv[1], argv[2], argv[3])

    engine = create_engine(db_url)
    Session = sessionmaker(bind=engine)

    session = Session()

    results = session.query(City, State).join(State)

    for city, state in results.all():
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.commit()
    session.close()
