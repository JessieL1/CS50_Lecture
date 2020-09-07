import os

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

DATABASE_URL="postgresql://postgres:postgres@localhost/postgres"
engine = create_engine(os.getenv("DATABASE_URL"))
#engine = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres')

db=scoped_session(sessionmaker(bind=engine))

def main():
    flights=db.execute("select id,origin,destination,duration from flights").fetchall()
    for flight in flights:
        print(f"Flights {flight.id}: {flight.origin} to {flight.destination}, {flight.duration} minitues.")
    #用户输入id,存入变量flight_id
    flight_id = int(input("\nFlight ID:"))
    #从表里取该id的数据
    flight=db.execute("select id,origin,destination,duration from flights where id=:id",
        {"id":flight_id}).fetchone()
    if flight is None:
        print("Error: No such flight.")
        return
    
    #有数据，列出该id的乘客
    passengers = db.execute("select name from passengers where flight_id = :id",{"id": flight_id}).fetchall()
    
    print("\nPassengers:\n")
    for passenger in passengers:
        print(passenger.name)
    if len(passengers) == 0:
        print("No passengers.")
    

if __name__ == "__main__":
    main()

