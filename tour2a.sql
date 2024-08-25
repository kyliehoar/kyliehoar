-- Drop ReservedTours, Customers, Tours, Locations, and Guides (so that the file can be run more than once)
drop table ReservedTour;
drop table Customer;
drop table Location;
drop table Tour;
drop table Guide;
drop table NewGuide;

-- Drop sequences created
drop sequence customerID_seq;
drop sequence tourID_seq;
drop sequence guideID_seq;
drop sequence reservedTourID_seq;
drop sequence newGuideID_seq;

-- Create ReservedTour, Customers, Tours, Locations, and Guides tables where
create table Customer (
	customerID number(3),
	firstName varchar2(15),
	lastName varchar2(20),
	address varchar2(30),
	phone number(10),
	age number(3) not null,
	Constraint Customer_PK Primary Key (customerID),
    Constraint phone_UN Unique (phone),
    Constraint Customer_age check (age is not null)
);

create sequence customerID_seq;
insert into Customer values (customerID_seq.nextval, 'Michael', 'Davis', '8711 Meadow St.', 2497873464, 67);
insert into Customer values (customerID_seq.nextval, 'Lisa', 'Ward', '17 Valley Drive', 9865553232, 20);
insert into Customer values (customerID_seq.nextval, 'Brian', 'Gray', '1212 8th St.', 4546667821, 29);
insert into Customer values (customerID_seq.nextval, 'Nicole', 'Myers', '9 Washington Court', 9864752346, 18);
insert into Customer values (customerID_seq.nextval, 'Kelly', 'Ross', '98 Lake Hill Drive', 8946557732, 26);
insert into Customer values (customerID_seq.nextval, 'Madison', 'Powell', '100 Main St.', 8915367188, 57);
insert into Customer values (customerID_seq.nextval, 'Ashley', 'Martin', '42 Oak St.', 1233753684, 73);
insert into Customer values (customerID_seq.nextval, 'Joshua', 'White', '1414 Cedar St.', 6428369619, 18);
insert into Customer values (customerID_seq.nextval, 'Tyler', 'Clark', '42 Elm Place', 1946825344, 22);
insert into Customer values (customerID_seq.nextval, 'Anna', 'Young', '657 Redondo Ave.', 7988641411, 25);
insert into Customer values (customerID_seq.nextval, 'Justin', 'Powell', '5 Jefferson Ave.', 2324648888, 17);
insert into Customer values (customerID_seq.nextval, 'Bruce', 'Allen', '143 Cambridge Ave.', 5082328798, 45);
insert into Customer values (customerID_seq.nextval, 'Rachel', 'Sanchez', '77 Massachusetts Ave.', 6174153059, 68);
insert into Customer values (customerID_seq.nextval, 'Dylan', 'Lee', '175 Forest St.', 2123043923, 19);
insert into Customer values (customerID_seq.nextval, 'Austin', 'Garcia', '35 Tremont St.', 7818914567, 82);

select * from Customer;

create table Tour (
	tourID number(2),
	tourName varchar2(25),
	description varchar2(35),
	city varchar2(25),
	state char(2),
	vehicleType varchar2(10),
	price number(5,2),
	Constraint Tour_PK Primary Key (tourID),
	Constraint Tour_vehicleTypeVal check (vehicleType in ('boat', 'bus', 'car'))
);

create sequence tourID_seq;
insert into Tour values (tourID_seq.nextval, 'Alcatraz', 'Alcatraz Island', 'San Francisco', 'CA', 'boat', 75.5);
insert into Tour values (tourID_seq.nextval, 'Magnificent Mile', 'Tour of Michigan Ave', 'Chicago', 'IL', 'bus', 22.75);
insert into Tour values (tourID_seq.nextval, 'Duck Tour', 'Aquatic tour of the Charles River', 'Boston', 'MA', 'boat', 53.99);
insert into Tour values (tourID_seq.nextval, 'Freedom Trail', 'Historic tour of Boston', 'Boston', 'MA', 'car', 34.25);
insert into Tour values (tourID_seq.nextval, 'NY Museums', 'Tour of NYC Museums', 'New York', 'NY', 'bus', 160.8);

select * from Tour;

create table Location (
    locationID char(3),
    locationName varchar2(40),
    locationType varchar2(15),
    address varchar2(40),
    tourID number(2),
    Constraint locationID_PK Primary Key (locationID),
    Constraint Loc_tourID_FK Foreign Key (tourID) 
		References Tour (tourID) On Delete Cascade
);

insert into Location values('AI1', 'San Francisco Pier 33', 'Historic', 'Pier 33 Alcatraz Landing', 1);
insert into Location values('AI2', 'Alcatraz Ferry Terminal', 'Historic', 'Ferry Terminal', 1);
insert into Location values('AI3', 'Agave Trail', 'Park', 'Alcatraz Agave Trail', 1);
insert into Location values('MM1', 'Art Institute', 'Museum', '111 S Michigan Avenue', 2);
insert into Location values('MM2', 'Chicago Tribune', 'Historic', '435 N Michigan Avenue', 2);
insert into Location values('MM3', 'White Castle', 'Restaurant', 'S Wabash Avenue', 2);
insert into Location values('DT1', 'Charles River', 'Historic', '10 Mass Avenue', 3);
insert into Location values('DT2', 'Salt and Pepper Bridge', 'Historic', '100 Broadway', 3);
insert into Location values('FT1', 'Boston Common', 'Park', '139 Tremont Street', 4);
insert into Location values('FT2', 'Kings Chapel', 'Historic', '58 Tremont Street', 4);
insert into Location values('FT3', 'Omni Parker House', 'Restaurant', '60 School Street', 4);
insert into Location values('FT4', 'Paul Revere House', 'Historic', '19 North Square', 4);
insert into Location values('FT5', 'Bunker Hill Monument', 'Historic', 'Monument Square', 4);
insert into Location values('NY1', 'Metropolitan Museum of Art', 'Museum', '1000 5th Ave', 5);
insert into Location values('NY2', 'Museum of Modern Art', 'Museum', '11 W 53rd St', 5);
insert into Location values('NY3', 'New York Botanical Garden', 'Park', '2900 Southern Boulevard', 5);
insert into Location values('NY4', 'New Museum', 'Museum', '235 Bowery', 5);

select * from Location;

create table Guide (
	guideID number(2),
	firstName varchar2(15),
	lastName varchar2(20),
	driverLicense number(8),
	title varchar2(15),
	salary number(7,2),
    licenseType varchar2(10),
	Constraint Guide_PK Primary Key (guideID),
	Constraint Guide_U1 Unique (driverLicense),
	Constraint Guide_driverLicenseVal check (driverLicense is not null),
    Constraint Guide_licenseType check (licenseType in ('land', 'sea', 'both'))
);

create sequence guideID_seq;
insert into Guide values (guideID_seq.nextval, 'Emily', 'Williams', '74920983', 'Senior Guide', 24125, 'land');
insert into Guide values (guideID_seq.nextval, 'Ethan', 'Brown', '72930684', 'Guide', 30500, 'sea');
insert into Guide values (guideID_seq.nextval, 'Chloe', 'Jones', '50973848', 'Senior Guide', 27044, 'both');
insert into Guide values (guideID_seq.nextval, 'Ben', 'Miller', '58442323', 'Junior Guide', 32080, 'both');
insert into Guide values (guideID_seq.nextval, 'Mia', 'Davis', '56719583', 'Junior Guide', 49000, 'land');
insert into Guide values (guideID_seq.nextval, 'Noah', 'Garcia', '93291234', 'Guide', 22000, 'land');
insert into Guide values (guideID_seq.nextval, 'Liam', 'Rodriguez', '58799394', 'Junior Guide', 31750, 'sea');
insert into Guide values (guideID_seq.nextval, 'Mason', 'Wilson', '88314545', 'Senior Guide', 45000, 'land');
insert into Guide values (guideID_seq.nextval, 'Olivia', 'Smith', '82391452', 'Junior Guide', 25025, 'sea');
insert into Guide values (guideID_seq.nextval, 'Sofia', 'Johnson', '12930638', 'Guide', 47000, 'both');

select * from Guide;

create table ReservedTour (
	reservedTourID number(3),
	travelDate date,
	customerID number(3),
	tourID number(2),
	guideID number(2),
    price number(6,2),
	Constraint ReservedTour_PK Primary Key(reservedTourID),
	Constraint RT_customerID_FK Foreign Key (customerID) 
		References Customer (customerID) On Delete Set Null,
	Constraint RT_tourID_FK Foreign Key (tourID) 
		References Tour (tourID) On Delete Set Null,
	Constraint RT_guideID_FK Foreign Key (guideID) 
		References Guide (guideID) On Delete Set Null
);

create sequence reservedTourID_seq
start with 100
increment by 5;

insert into ReservedTour values (reservedTourID_seq.nextval, '6-Feb-18', 6, 1, 2, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '31-Aug-18', 14, 3, 5, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '10-Apr-19', 11, 4, 1, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '29-Jul-18', 7, 2, 4, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '15-Mar-18', 14, 3, 2, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '28-Feb-19', 12, 4, 6, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '3-Jun-18', 14, 4, 2, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '17-May-18', 5, 1, 10, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '11-Apr-19', 9, 5, 3, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '24-Nov-18', 13, 4, 9, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '3-Aug-18', 3, 5, 7, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '13-Dec-17', 2, 1, 7, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '9-Nov-17', 4, 5, 1, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '21-Jan-19', 10, 2, 10, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '11-Dec-17', 5, 1, 7, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '12-Aug-18', 1, 3, 5, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '22-Jun-18', 5, 3, 8, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '1-Feb-19', 8, 2, 9, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '15-Oct-17', 15, 4, 8, null);
insert into ReservedTour values (reservedTourID_seq.nextval, '8-Mar-18', 4, 1, 3, null);

select * from ReservedTour;

-- Customer (customerID PK, firstName, lastName, address, phone, age)
-- Tour(tourID PK, tourName, description, city, state, vehicleType, price)
-- Location(locationID PK, locationName, locationType, address, tourID FK)
-- Guide(guideID PK, firstName, lastName, driverLicense, title, salary, licenseType)
-- ReservedTour(reservedTourID PK, travelDate, customerID FK, tourID FK, guideID FK, price)