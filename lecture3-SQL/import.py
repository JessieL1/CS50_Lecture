import os
import csv

from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session,sessionmaker

DATABASE_URL="postgresql://postgres:postgres@localhost/postgres"
engine = create_engine(os.getenv("DATABASE_URL"))
#engine = create_engine('postgresql+psycopg2://postgres:postgres@127.0.0.1:5432/postgres')

db=scoped_session(sessionmaker(bind=engine))

def main():
    #打开要导入的数据文件
    f = open("flights.csv")
    reader = csv.reader(f)
    for ori,dest,dur in reader:
        #placeholder占位符
        db.execute("insert into flights (origin,destination,duration) values (:origin,:destination,:duration)",
            {"origin":ori,"destination":dest,"duration":dur})

        print(f"Added flight from {ori} to {dest}, lasting {dur} minitues.")
    db.commit()

if __name__ == "__main__":
    main()

