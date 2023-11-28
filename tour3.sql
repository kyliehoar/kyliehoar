-- PART 3

--Housekeeping/testing prior to Question 1
drop table NewGuide;
drop sequence newGuideID_seq;

create table NewGuide (
	newGuideID number(2),
	firstName varchar2(15),
	lastName varchar2(20),
	driverLicense number(8),
	title varchar2(15),
	salary number(7,2),
    licenseType varchar2(10),
	Constraint newGuide_PK Primary Key (newGuideID),
	Constraint newGuide_U1 Unique (driverLicense),
	Constraint newGuide_driverLicenseVal check (driverLicense is not null),
    Constraint newGuide_licenseType check (licenseType in ('land', 'sea', 'both'))
);

create sequence newGuideID_seq;
insert into NewGuide values (newGuideID_seq.nextval, 'Emily', 'Williams', '74920983', 'Senior Guide', 24125, 'land');
insert into NewGuide values (newGuideID_seq.nextval, 'Ethan', 'Brown', '72930684', 'Guide', 30500, 'sea');
insert into NewGuide values (newGuideID_seq.nextval, 'Chloe', 'Jones', '50973848', 'Senior Guide', 27044, 'both');
insert into NewGuide values (newGuideID_seq.nextval, 'Ben', 'Miller', '58442323', 'Junior Guide', 32080, 'both');
select * from NewGuide;

-- 1
-- include table insert with sample values
select G.title, sum(GSalary) + sum(NGSalary) AS Sum
from (select title, sum(salary) as GSalary from Guide group by title) G,
     (select title, sum(salary) as NGSalary from NewGuide group by title) NG
where G.title = NG.title
group by G.title;

-- 2
select firstName, lastName, count(distinct locationID) as Visits
from Customer C
join ReservedTour RT on C.customerID = RT.customerID
join Tour T on RT.tourID = T.tourID
join Location L on T.tourID = L.tourID
group by firstName, lastName
having count(distinct locationID) = (select Max(CNT) as MaxCount
                                        from (select count(distinct locationID) as CNT
                                            from Location L
                                            join Tour T on L.tourID = T.tourID
                                            join ReservedTour RT on T.tourID = RT.tourID
                                            join Customer C on RT.customerID = C.customerID
                                            group by firstName, lastName));

--Housekeeping/testing prior to Question 3
drop table SFBook;
drop table Stock;

drop sequence ISBN_seq;
drop sequence warehouseCode_seq;

create table SFBook (
    ISBN number(10),
    title varchar2(20),
    year number(4),
    price number(6,2),
    awardWinner varchar2(10),
    publisherName varchar2(10),
    Constraint ISBN_PK Primary Key(ISBN)
);


create sequence ISBN_seq;
insert into SFBook values (ISBN_seq.nextval, 'title', 2004, 59.99, 'John', 'Wiley');
insert into SFBook values (ISBN_seq.nextval, 'title1', 2018, 189.99, 'Maria', 'Wiley');
insert into SFBook values (ISBN_seq.nextval, 'fjesgg', 2021, 1189.99, 'Jane', 'Joe');
insert into SFBook values (ISBN_seq.nextval, 'gjmvsoe', 2000, 339.99, 'Kay', 'Winter');
insert into SFBook values (ISBN_seq.nextval, 'fncorf', 2003, 189.87, 'Mike', 'Will');
insert into SFBook values (ISBN_seq.nextval, 'frnevwr;', 1834, 1.99, 'Hank', 'Wiley');
insert into SFBook values (ISBN_seq.nextval, 'fnrfn', 1930, 349.00, 'Dude', 'Sammy');
Select * from SFBook;


create table Stock (
    warehouseCode number(6),
    ISBN number(10),
    city varchar2(10),
    numberOfBooks number(3),
    Constraint warehouseCode_PK Primary Key(warehouseCode),
    Constraint ISBN_FK Foreign Key(ISBN) References SFBook(ISBN) on Delete Set Null
);

create sequence warehouseCode_seq
minvalue 100;
insert into Stock values (warehouseCode_seq.nextval, 1, 'Wanda', 5);
insert into Stock values (warehouseCode_seq.nextval, 2, 'Edgartown', 10);
insert into Stock values (warehouseCode_seq.nextval, 2, 'John', 9);
insert into Stock values (warehouseCode_seq.nextval, 3, 'Carlestown', 3);
insert into Stock values (warehouseCode_seq.nextval, 3, 'Boston', 60);
insert into Stock values (warehouseCode_seq.nextval, 6, 'Savannah', 2);
insert into Stock values (warehouseCode_seq.nextval, 6, 'Nebraska', 3);
insert into Stock values (warehouseCode_seq.nextval, 7, 'Worcester', 20);
Select * from Stock;

-- 3
select warehouseCode, city
from (select warehouseCode, city, sum(numberOfBooks) as SUM 
                                from Stock S 
                                join SFBook SF on S.ISBN = SF.ISBN 
                                where publisherName like 'Wiley' 
                                group by warehouseCode, city 
                                having sum(numberOfBooks) < 10);