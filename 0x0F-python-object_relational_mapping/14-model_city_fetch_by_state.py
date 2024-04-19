#!/usr/bin/python3
"""
A script that prints all City objects from the database `hbtn_0e_14_usa` sorted by city ids.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    if len(sys.argv) == 4:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        database_name = sys.argv[3]

        # Create the connection URL
        url = f'mysql+mysqldb://{mysql_username}:{mysql_password}@localhost:3306/{database_name}'

        # Create engine
        engine = create_engine(url, pool_pre_ping=True)

        # Create a configured "Session" class
        Session = sessionmaker(bind=engine)

        # Create a session
        session = Session()

        # Query cities joined with states, ordered by cities.id
        results = session.query(City, State).join(State).order_by(City.id).all()
        for city, state in results:
            print(f"{state.name}: ({city.id}) {city.name}")

        session.close()
    else:
        print("Usage: ./14-model_city_fetch_by_state.py <mysql username> <mysql password> <database name>")
