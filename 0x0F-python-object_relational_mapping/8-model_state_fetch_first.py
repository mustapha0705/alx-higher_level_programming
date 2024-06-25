#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
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

    # Query the first instance of State
    instance = session.query(State).first()

    # Print the id and name of the first instance, or "Nothing"
    if instance is None:
        print("Nothing")
    else:
        print(instance.id, instance.name, sep=": ")

    # Close the session
    session.close()
