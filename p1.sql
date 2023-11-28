alter table Edge
drop constraint startLoc_FK;
alter table Hallway
drop constraint HallwaylocationID_FK;
alter table Office
drop constraint OfficelocationID_FK;
alter table HasAnOrderedList
drop constraint ListlocationID_FK;
alter table Title
drop constraint TitleaccountName_FK;
alter table EmployeePhoneNum
drop constraint PhoneaccountNum_FK;
alter table AssignedTo
drop constraint AssignedaccountName_FK;
alter table AssignedTo
drop constraint AssignedlocationID_FK;

drop sequence seqPathID;

drop table Location;
drop table Path;
drop table Edge;
drop table HasAnOrderedList;
drop table Hallway;
drop table Office;
drop table Employee;
drop table AssignedTo;
drop table EmployeePhoneNum;
drop table Title;

create table Location(
    locationID varchar2(4),
    locationName varchar2(30),
    locationType varchar2(30),
    floor number(2),
    Xcoord number(3),
    Ycoord number(3),
    Constraint locationID_PK Primary Key (locationID),
    Constraint floor_Unique check (floor in ('1', '2', '3', 'A', 'B')),
    Constraint loc_Unique Unique (floor, Xcoord, Ycoord)
);
insert into Location values('307', 'FL307', 'Office', '3',  900,  440);
insert into Location values('308', 'FL308', 'Office', '3',  900,  335);
insert into Location values('311', 'FL311', 'Conference Room', '3',  900,  375);
insert into Location values('312', 'FL312', 'Office', '3',  945,  510);
insert into Location values('314', 'FL314', 'Office', '3',  845,  660);
insert into Location values('316', 'FL316', 'Office', '3',  845,  760);
insert into Location values('317', 'FL317', 'Office', '3',  925,  670);
insert into Location values('318', 'FL318', 'Office', '3',  950,  700);
insert into Location values('319', 'FL319', 'Office', '3',  925,  735);
insert into Location values('320', 'FL320', 'Lecture Hall', '3',  900,  920);
insert into Location values('3E1', '3rd Floor Elevator', 'Elevator', '3',  820,  415);
insert into Location values('3H1', 'FL3H1', 'Hallway ', '3',  790,  150);
insert into Location values('3H2', 'FL3H2', 'Hallway ', '3',  790,  340);
insert into Location values('3H3', 'FL3H3', 'Hallway ', '3',  790,  375);
insert into Location values('3H4', 'FL3H4', 'Hallway ', '3',  790,  420);
insert into Location values('3H5', 'FL3H5', 'Hallway ', '3',  790,  465);
insert into Location values('3H6', 'FL3H6', 'Hallway ', '3',  900,  465);
insert into Location values('3H7', 'FL3H7', 'Hallway ', '3',  900,  510);
insert into Location values('3H8', 'FL3H8', 'Hallway ', '3',  790,  660);
insert into Location values('3H9', 'FL3H9', 'Hallway ', '3',  790,  700);
insert into Location values('3H10', 'FL3H10', 'Hallway ', '3',  925,  700);
insert into Location values('3H11', 'FL3H11', 'Hallway ', '3',  790,  755);
insert into Location values('3H12', 'FL3H12', 'Hallway ', '3',  790,  925);
insert into Location values('3H13', 'FL3H13', 'Hallway ', '3',  840,  920);
insert into Location values('3S1', '3rd Floor Staircase 1', 'Staircase', '3',  835,  340);
insert into Location values('3S2', '3rd Floor Staircase 2', 'Staircase', '3',  840,  965);
Select * from Location;

create table Edge(
    startLoc varchar2(4),
    endLoc varchar2(4),
    Constraint startLoc_FK Foreign Key (startLoc) References Location (locationID) on delete set NULL,
    Constraint uniqueLocs Unique (startLoc, endLoc)
);
insert into Edge values('307', '3H6');
insert into Edge values('308', '311');
insert into Edge values('311', '308');
insert into Edge values('311', '3H3');
insert into Edge values('312', '3H7');
insert into Edge values('314', '3H8');
insert into Edge values('316', '3H11');
insert into Edge values('317', '3H10');
insert into Edge values('318', '3H9');
insert into Edge values('319', '3H10');
insert into Edge values('320', '3H13');
insert into Edge values('3E1', '3H4');
insert into Edge values('3H1', '3H2');
insert into Edge values('3H1', '3H3');
insert into Edge values('3H1', '3H4');
insert into Edge values('3H1', '3H5');
insert into Edge values('3H1', '3H8');
insert into Edge values('3H1', '3H9');
insert into Edge values('3H1', '3H11');
insert into Edge values('3H1', '3H12');
insert into Edge values('3H2', '3S1');
insert into Edge values('3H2', '3H1');
insert into Edge values('3H3', '311');
insert into Edge values('3H3', '3H1');
insert into Edge values('3H4', '3E1');
insert into Edge values('3H4', '3H1');
insert into Edge values('3H5', '3H6');
insert into Edge values('3H5', '3H1');
insert into Edge values('3H6', '307');
insert into Edge values('3H6', '3H7');
insert into Edge values('3H6', '3H5');
insert into Edge values('3H7', '312');
insert into Edge values('3H7', '3H6');
insert into Edge values('3H8', '314');
insert into Edge values('3H8', '3H1');
insert into Edge values('3H9', '318');
insert into Edge values('3H9', '3H1');
insert into Edge values('3H10', '317');
insert into Edge values('3H10', '319');
insert into Edge values('3H10', '3H9');
insert into Edge values('3H11', '316');
insert into Edge values('3H11', '3H1');
insert into Edge values('3H12', '3H1');
insert into Edge values('3H12', '3H13');
insert into Edge values('3H12', '3S2');
insert into Edge values('3H13', '320');
insert into Edge values('3S1', '3H2');
insert into Edge values('3S2', '3H12');
insert into Edge values('3S2', '3H13');
Select * from Edge;

create table Path(
    pathID number(2),
    Constraint pathID_PK Primary Key (pathID)
);
create sequence seqPathID;
insert into Path values(seqPathID.nextval);
insert into Path values(seqPathID.nextval);
insert into Path values(seqPathID.nextval);
Select * from Path;

create table HasAnOrderedList(
    locationID varchar2(4),
    pathID number(2),
    orderNumber varchar2(40),
    Constraint ListlocationID_FK Foreign Key (locationID) references Location (locationID) on delete set NULL
);
insert into HasAnOrderedList values('3E1', 1,'3E1, 3H4, 3H1, 3H12, 3H13, 320');
insert into HasAnOrderedList values('312', 2,'312, 3H7, 3H5, 3H1, 3H9, 3H10, 319');
insert into HasAnOrderedList values('3S2', 3,'S2, 3H12, 3H1, 3H3, 311, 308');
Select * from HasAnOrderedList;

create table Hallway(
    locationID varchar2(4),
    longName varchar2(40),
    Constraint HallwaylocationID_FK Foreign Key (locationID) References Location (locationID) on delete set NULL
);
insert into Hallway values('3H1', 'description');
insert into Hallway values('3H2', 'description');
insert into Hallway values('3H3', 'description');
insert into Hallway values('3H4', 'description');
insert into Hallway values('3H5', 'description');
insert into Hallway values('3H6', 'description');
insert into Hallway values('3H7', 'description');
insert into Hallway values('3H8', 'description');
insert into Hallway values('3H9', 'description');
insert into Hallway values('3H10', 'description');
insert into Hallway values('3H11', 'description');
insert into Hallway values('3H12', 'description');
insert into Hallway values('3H13', 'description');
Select * from Hallway;

create table Office(
    locationID varchar2(4),
    Constraint OfficelocationID_FK Foreign Key (locationID) References Location (locationID) on delete set NULL
);
insert into Office values('3H2');
insert into Office values('3H3');
insert into Office values('3H5');
insert into Office values('3H6');
insert into Office values('3H7');
insert into Office values('3H8');
insert into Office values('3H9');
insert into Office values('3H10');
Select * from Office;

create table Employee(
    accountName varchar2(15),
    firstName varchar2(20) not null,
    lastName varchar2(20) not null,
    -- locationID varchar2(4),
    Constraint accountName_PK Primary Key (accountName)
);
insert into Employee values('ruiz', 'Carolina', 'Ruiz');
insert into Employee values('rich', 'Charles', 'Rich');
insert into Employee values('ccaron', 'Christine', 'Caron');
insert into Employee values('cshue', 'Craig', 'Shue');
insert into Employee values('cew', 'Craig', 'Wills');
insert into Employee values('dd', 'Daniel', 'Dougherty');
insert into Employee values('deselent', 'Douglas', 'Selent');
insert into Employee values('rundenst', 'Elke', 'Rundensteiner');
insert into Employee values('emmanuel', 'Emmanuel', 'Agu');
insert into Employee values('heineman', 'George', 'Heineman');
insert into Employee values('ghamel', 'Glynis', 'Hamel');
insert into Employee values('lauer', 'Hugh', 'Lauer');
insert into Employee values('jleveillee', 'John', 'Leveillee');
insert into Employee values('josephbeck', 'Joseph', 'Beck');
insert into Employee values('kfisler', 'Kathryn', 'Fisler');
insert into Employee values('kven', 'Krishna', 'Venkatasubramanian');
insert into Employee values('claypool', 'Mark', 'Claypool');
insert into Employee values('hofri', 'Micha', 'Hofri');
insert into Employee values('ciaraldi', 'Michael', 'Ciaraldi');
insert into Employee values('mvoorhis', 'Michael', 'Voorhis');
insert into Employee values('meltabakh', 'Mohamed', 'Eltabakh');
insert into Employee values('nth', 'Neil', 'Heffernan');
insert into Employee values('nkcaligiuri', 'Nicole', 'Caligiuri');
insert into Employee values('rcane', 'Refie', 'Cane');
insert into Employee values('tgannon', 'Thomas', 'Gannon');
insert into Employee values('wwong2', 'Wilson', 'Wong');
Select * from Employee;

create table AssignedTo(
    locationID varchar2(4),
    accountName varchar2(15),
    Constraint AssignedlocationID_FK Foreign Key (locationID) References Location (locationID) on delete set NULL,
    Constraint AssignedaccountName_FK Foreign Key (accountName) References Employee (accountName) on delete set NULL
);

create table EmployeePhoneNum(
    phoneNumber varchar2(15),
    accountName varchar2(15),
    Constraint PhoneaccountNum_FK Foreign Key (accountName) References Employee (accountName) on delete set NULL
);
insert into EmployeePhoneNum values('5640', 'ruiz');
insert into EmployeePhoneNum values('5945', 'rich');
insert into EmployeePhoneNum values('5678', 'ccaron');
insert into EmployeePhoneNum values('4933', 'cshue');
insert into EmployeePhoneNum values('5357, 5622', 'cew');
insert into EmployeePhoneNum values('5621', 'dd');
insert into EmployeePhoneNum values('5493', 'deselent');
insert into EmployeePhoneNum values('5815', 'rundenst');
insert into EmployeePhoneNum values('5568', 'emmanuel');
insert into EmployeePhoneNum values('5502', 'heineman');
insert into EmployeePhoneNum values('5252', 'ghamel');
insert into EmployeePhoneNum values('5493', 'lauer');
insert into EmployeePhoneNum values('5822', 'jleveillee');
insert into EmployeePhoneNum values('6156', 'josephbeck');
insert into EmployeePhoneNum values('5118', 'kfisler');
insert into EmployeePhoneNum values('6571', 'kven');
insert into EmployeePhoneNum values('5409', 'claypool');
insert into EmployeePhoneNum values('6911', 'hofri');
insert into EmployeePhoneNum values('5117', 'ciaraldi');
insert into EmployeePhoneNum values('5669, 5674', 'mvoorhis');
insert into EmployeePhoneNum values('6421', 'meltabakh');
insert into EmployeePhoneNum values('5569', 'nth');
insert into EmployeePhoneNum values('5357', 'nkcaligiuri');
insert into EmployeePhoneNum values('5357', 'rcane');
insert into EmployeePhoneNum values('5357', 'tgannon');
insert into EmployeePhoneNum values('5706', 'wwong2');
Select * from EmployeePhoneNum;

create table Title(
    acronym varchar2(20),
    tName varchar2(70),
    accountName varchar2(15),
    Constraint TitleaccountName_FK Foreign Key (accountName) References Employee (accountName) on delete set NULL
);
insert into Title values('Assoc Prof',  'Associate Professor', 'ruiz');
insert into Title values('Prof',  'Professor', 'rich');
insert into Title values('Admin 6',  'Administrative Assistant VI', 'ccaron');
insert into Title values('Asst Prof',  'Assistant Professor', 'cshue');
insert into Title values('Prof, DeptHead',  'Professor, Department Head', 'cew');
insert into Title values('Prof',  'Professor', 'dd');
insert into Title values('Asst TProf',  'Assistant Teaching Professor', 'deselent');
insert into Title values('Prof, Dir-DS',  'Professor, Director of Data Science', 'rundenst');
insert into Title values('Assoc Prof, C-MGRG',  'Associate Professor, Coordinator of Mobile Graphics Research Group', 'emmanuel');
insert into Title values('Assoc Prof',  'Associate Professor', 'heineman');
insert into Title values('SrInst',  'Senior Instructor', 'ghamel');
insert into Title values('TProf',  'Teaching Professor', 'lauer');
insert into Title values('Lab1',  'Lab Manager I', 'jleveillee');
insert into Title values('Assoc Prof',  'Associate Professor', 'josephbeck');
insert into Title values('Prof',  'Professor', 'kfisler');
insert into Title values('Asst Prof',  'Assistant Professor', 'kven');
insert into Title values('Prof',  'Professor', 'claypool');
insert into Title values('Prof',  'Professor', 'hofri');
insert into Title values('SrInst',  'Senior Instructor', 'ciaraldi');
insert into Title values('Lab2',  'Lab Manager II', 'mvoorhis');
insert into Title values('Assoc Prof',  'Associate Professor', 'meltabakh');
insert into Title values('Prof, Dir-LST',  'Professor, Director of Learn Sciences and Technologies', 'nth');
insert into Title values('Admin 5',  'Administrative Assistant V', 'nkcaligiuri');
insert into Title values('GradAdmin',  'Graduate Admin Coordinator', 'rcane');
insert into Title values('Adj Assoc Prof',  'Adjunct Associate Professor', 'tgannon');
insert into Title values('Asst Prof',  'Assistant Professor', 'wwong2');
Select * from Title;