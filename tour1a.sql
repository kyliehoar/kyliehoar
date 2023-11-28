/*Drop tables so that files can be run over and over*/
drop table ReservedTour purge;
drop table Customer purge;
drop table Tour purge;
drop table Guide purge;

/*Drop sequences so that the file can be run over and over*/
drop sequence customerIDseq;
drop sequence tourID_seq;
drop sequence guideID_seq;
drop sequence reservedTourID_seq;

/*Customer Table*/
create table Customer (
    customerID number,
    firstName varchar2(15),
    lastName varchar2(20),
    address varchar2(30),
    phone number(10),
    age number(3),
    
    Constraint customerID_PK Primary Key(customerID)
);

/*Create Sequence for customerID*/
create sequence customerIDseq
    start with 1
    increment by 1;

/*Customer Data*/
insert into Customer values(customerIDSeq.nextval, 'Michael', 'Davis', '8711 Meadow St.', 2497873464, 67);
insert into Customer values(customerIDSeq.nextval, 'Lisa', 'Ward', '17 Valley Drive', 9865553232, 20);
insert into Customer values(customerIDSeq.nextval, 'Brian', 'Gray', '1212 8th St.', 4546667821, 29);
insert into Customer values(customerIDSeq.nextval, 'Nicole', 'Myers', '9 Washington Court', 9864752346, 18);
insert into Customer values(customerIDSeq.nextval, 'Kelly', 'Ross', '98 Lake Hill Drive', 8946557732, 26);
insert into Customer values(customerIDSeq.nextval, 'Madison', 'Powell', '100 Main St.', 8915367188, 57);
insert into Customer values(customerIDSeq.nextval, 'Ashley', 'Martin', '42 Oak St.', 1233753684, 73);
insert into Customer values(customerIDSeq.nextval, 'Joshua', 'White', '1414 Cedar St.', 6428369619, 18);
insert into Customer values(customerIDSeq.nextval, 'Tyler', 'Clark', '42 Elm Place', 1946825344, 22);
insert into Customer values(customerIDSeq.nextval, 'Anna', 'Young', '657 Redondo Ave.', 7988641411, 25);
insert into Customer values(customerIDSeq.nextval, 'Justin', 'Powell', '5 Jefferson Ave.', 2324648888, 17);
insert into Customer values(customerIDSeq.nextval, 'Bruce', 'Allen', '143 Cambridge Ave.', 5082328798, 45);
insert into Customer values(customerIDSeq.nextval, 'Rachel', 'Sanchez', '77 Massachusetts Ave.', 6174153059, 68);
insert into Customer values(customerIDSeq.nextval, 'Dylan', 'Lee', '175 Forest St.', 2123043923, 19);
insert into Customer values(customerIDSeq.nextval, 'Austin', 'Garcia', '35 Tremont St.', 7818914567, 82);
Select * from Customer;

/*Tour Table*/
create table Tour (
    tourID number,
    tourName varchar2(25),
    description varchar2(35),
    city varchar2(25),
    state char(2),
    vehicleType varchar2(10),
    price number(5,2),
    
    Constraint tourID_PK Primary Key(tourID),
    Constraint vehicleType_CH check(vehicleType in ('boat','bus','car'))
);

/*Create Sequence for tourID*/
create sequence tourID_seq
    start with 1 
    increment by 1;

/*Tour Data*/
insert into Tour values(1, 'Alcatraz', 'Alcatraz Island', 'San Francisco', 'CA', 'boat', 75.5);
insert into Tour values(2, 'Magnificent Mile', 'Tour of Michigan Ave', 'Chicago', 'IL', 'bus', 22.75);
insert into Tour values(3, 'Duck Tour', 'Aquatic tour of the Charles River', 'Boston', 'MA', 'boat', 53.99);
insert into Tour values(4, 'Freedom Trail', 'Historic tour of Boston', 'Boston', 'MA', 'car', 34.25);
insert into Tour values(5, 'NY Museums', 'Tour of NYC Museums', 'New York', 'NY', 'bus', 160.8);
Select * from Tour;

/*Guide Table*/
create table Guide (
    guideID number,
    FirstName varchar2(15),
    LastName varchar2(20),
    driverLicense number(8) Not Null,
    Title varchar2(15),
    Salary number(7,2),
    
    Constraint guideID_PK Primary Key(guideID),
    Constraint diverLicense_U1 Unique(driverLicense)
);

/*Create Sequence for guideID*/
create sequence guideID_seq
    start with 1 
    increment by 1;

/*Guide Data*/
insert into Guide values(1, 'Emily', 'Williams', 74920983, 'Senior Guide', 24125);
insert into Guide values(2, 'Ethan', 'Brown', 72930684, 'Guide', 30500);
insert into Guide values(3, 'Chloe', 'Jones', 50973848, 'Senior Guide', 27044);
insert into Guide values(4, 'Ben', 'Miller', 58442323, 'Junior Guide', 32080);
insert into Guide values(5, 'Mia', 'Davis', 56719583, 'Junior Guide', 49000);
insert into Guide values(6, 'Noah', 'Garcia', 93291234, 'Guide', 22000);
insert into Guide values(7, 'Liam', 'Rodriguez', 58799394, 'Junior Guide', 31750);
insert into Guide values(8, 'Mason', 'Wilson', 88314545, 'Senior Guide', 45000);
insert into Guide values(9, 'Olivia', 'Smith', 82391452, 'Junior Guide', 25025);
insert into Guide values(10, 'Sofia', 'Johnson', 12930638, 'Guide', 47000);
Select * from Guide;

/*ReservedTour Table*/
create table ReservedTour (
    reservedTourID number,
    travelDate date,
    customerID number(3),
    tourID number(2),
    guideID number(2),
    
    Constraint reservedTourID_PK Primary Key(reservedTourID),
    Constraint customerID_FK Foreign Key(customerID) references Customer(customerID) On Delete Set Null,
    Constraint tourID_FK Foreign Key(tourID) references Tour(tourID) On Delete Set Null,
    Constraint guideID_FK Foreign Key(guideID) references Guide(guideID) On Delete Set Null
);

/*Create Sequence for reservedTourID*/
create sequence reservedTourID_seq
    start with 100 
    increment by 5;

/*ReservedTour Data*/
insert into ReservedTour values(100, '6-Feb-18', 6, 1, 2);
insert into ReservedTour values(105, '31-Aug-18', 14, 3, 5);
insert into ReservedTour values(110, '10-Apr-19', 11, 4, 1);
insert into ReservedTour values(115, '29-Jul-18', 7, 2, 4);
insert into ReservedTour values(120, '15-Mar-18', 14, 3, 2);
insert into ReservedTour values(125, '28-Feb-19', 12, 4, 6);
insert into ReservedTour values(130, '3-Jun-18', 14, 4, 2);
insert into ReservedTour values(135, '17-May-18', 5, 1, 10);
insert into ReservedTour values(140, '11-Apr-19', 9, 5, 3);
insert into ReservedTour values(145, '24-Nov-18', 13, 4, 9);
insert into ReservedTour values(150, '3-Aug-18', 3, 5, 7);
insert into ReservedTour values(155, '13-Dec-17', 2, 1, 7);
insert into ReservedTour values(160, '9-Nov-17', 4, 5, 1);
insert into ReservedTour values(165, '21-Jan-19', 10, 2, 10);
insert into ReservedTour values(170, '11-Dec-17', 5, 1, 7);
insert into ReservedTour values(175, '12-Aug-18', 1, 3, 5);
insert into ReservedTour values(180, '22-Jun-18', 5, 3, 8);
insert into ReservedTour values(185, '1-Feb-19', 8, 2, 9);
insert into ReservedTour values(190, '15-Oct-17', 15, 4, 8);
insert into ReservedTour values(195, '8-Mar-18', 4, 1, 3);
Select * from ReservedTour;