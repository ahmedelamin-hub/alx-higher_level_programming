#!/usr/bin/python3
"""
Script that lists all State objects from the database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import State and Base


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    dbname = sys.argv[3]
    
    # Create an engine that connects to the MySQL server
    engine = create_engine(f'mysql+mysqldb://{username}:{password}@localhost/{dbname}', pool_pre_ping=True)

    # Create a sessionmaker bound to this engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states in the database, order by state.id
    states = session.query(State).order_by(State.id.asc()).all()

    # Print each state id and name
    for state in states:
        print(f"{state.id}: {state.name}")

    # Close the session
    session.close()
