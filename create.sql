CREATE TABLE flights (
  id SERIAL PRIMARY KEY,
  origin VARCHAR NOT NULL,
  destination VARCHAR NOT NULL,
  duration INTEGER NOT NULL
);

/////////////////////
# SELECT origin, COUNT(*) FROM flights GROUP BY origin HAVING COUNT(*) > 1;

/////////////////////
# SELECT origin, destination, name FROM flights JOIN passengers ON passengers.flight_id = flight.id;

////////////////////
SQL injection

SELECT * FROM users
  WHERE (username = username)
  and (password = password);
  
////////////////////
Race conditions

SQL Transactions

python

import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,  sessionmaker

engine = create_engine(os.getenv("DATABASE_URL")
db = scoped_session(sessionmaker(bind=engine))

def main():
flights = db.
