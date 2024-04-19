#!/usr/bin/python3
"""
A script that changes the name of the State object with id=2 to "New Mexico"
in the database `hbtn_0e_6_usa`.
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

        # Find the State with id=2
        state_to_update = session.query(State).get(2)

        if state_to_update:
            # Change the name of the State
            state_to_update.name = "New Mexico"
            session.commit()

        session.close()
    else:
        print("Usage: ./12-model_state_update_id_2.py <mysql username> <mysql password> <database name>")
