#!/usr/bin/python3
"""
Prints State objects whose name contains 'a' from the database hbtn_0e_6_usa.
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    # Create engine for connecting to MySQL database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost:3306/{}'
        .format(sys.argv[1], sys.argv[2], sys.argv[3])
    )

    # Create all tables based on metadata from Base
    Base.metadata.create_all(engine)

    # Create a sessionmaker instance bound to the engine
    Session = sessionmaker(bind=engine)

    # Create a session object to interact with the database
    session = Session()

    # Query instances of State where name contains 'a' and print id and name
    for instance in session.query(State).filter(State.name.like('%a%')):
        print(instance.id, instance.name, sep=": ")

    # Close the session
    session.close()
