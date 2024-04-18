#!/usr/bin/python3
"""
A script that lists all State objects that contain the letter 'a' from the
database `hbtn_0e_6_usa`.
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

        # Query states containing letter 'a'
        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id)

        for state in states_with_a:
            print(f"{state.id}: {state.name}")

        session.close()
    else:
        print("Usage: ./9-model_state_filter_a.py <mysql username> <mysql password> <database name>")
