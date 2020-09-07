CREATE TABLE passengers (
    id SERIAL PRIMARY KEY,
    name VARCHAR NOT NULL,
    flight_id INTEGER REFERENCES flights
)
insert into passengers (name, flight_id) values('Alice',1);
insert into passengers (name, flight_id) values('Bob',1);
insert into passengers (name, flight_id) values('Charlie',2);
insert into passengers (name, flight_id) values('Dave',2);
insert into passengers (name, flight_id) values('Erin',4);
insert into passengers (name, flight_id) values('Frank',6);
insert into passengers (name, flight_id) values('Grace',6);

select * from flights where id in 
select flight_id from passengers group by flight_id having count(*)>1

insert into Calorie (name, cal) values('egg',144);
insert into Calorie (name, cal) values('biscuit',435);
insert into Calorie (name, cal) values('apple',53);
insert into Calorie (name, cal) values('corn',112);