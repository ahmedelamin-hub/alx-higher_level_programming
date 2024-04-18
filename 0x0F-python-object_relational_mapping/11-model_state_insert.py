#!/usr/bin/python3
"""
A script that adds the State object "Louisiana" to the database `hbtn_0e_6_usa`
and prints the new state's id after creation.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    if len(sys.argv) == 4:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Create the connection URL
        url = f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}'

        # Create engine
        engine = create_engine(url, pool_pre_ping=True)

        # Bind the engine to the Base class
        Base.metadata.create_all(engine)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Create a new State object
        new_state = State(name="Louisiana")

        # Add the new State to the session
        session.add(new_state)
        session.commit()

        # Print the new state's id
        print(new_state.id)

        session.close()
    else:
        print("Usage: ./11-model_state_insert.py <mysql username> <mysql password> <database name>")
