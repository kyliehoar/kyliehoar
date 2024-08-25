/*
Create a query named “NoLabMgr” using views instead of sub-queries for the following:
for each location that is an office, list the number of CS staff who are not lab managers but only if there is
more than one person in the office
*/

drop view NotLabManager;
drop view NoLabMgr;

create view NotLabManager AS
select C.accountName, officeID, count(acronym) as COUNT
from CSStaff C join CSStaffTitles CT on C.accountName = CT.accountName
where CT.acronym not like '%Lab%'
group by C.accountName, officeID;

create view NoLabMgr AS
select officeID, count(accountName) as Count 
from NotLabManager
group by officeID
having count(*) > 1;
Select * from NoLabMgr;

/*
Create a procedure named “NumberOfStaff” that takes an office id (for example, 233) as an input
parameter and displays the total number of computer science staff members at that location. Hint: Use
the function dbms_output.put_line(). Make sure to run the following command so you can see the
output:
set serveroutput on
*/

Create or Replace Procedure NumberOfStaff (officeID varchar2) IS
staffCountNumber number(5);
locationID varchar2(10);
Begin
Select count(accountName), officeID into staffCountNumber, locationID
From CSStaff
Where CSStaff.officeID = NumberOfStaff.officeID
Group By officeID;
dbms_output.put_line('Number of Staff: ' || staffCountNumber || ' ' || 
'Location: ' || locationID);
End NumberOfStaff;
/
set serveroutput on;

exec NumberOfStaff(129);
exec NumberOfStaff(233);

/*
Edges that are added cannot have two of the same locations. Only check new edges being added. Name
the trigger NoSameLocations
*/

create or replace trigger NoSameLocations
before insert on Edges
for each row
when (new.startingLocationID = new.endingLocationID)
begin
    RAISE_APPLICATION_ERROR(-20004, 'Cannot insert record.');
end;
/

/*
The only edges that can be added with locations on different floors are those edges that have either both
elevator locations or both staircase locations. Only check new edges being added. Name the trigger
CrossFloorEdge
*/

create or replace trigger CrossFloorEdge
before insert on Edges
for each row
declare
    startingFloor number(1);
    endingFloor number(1);
    startLocType varchar2(15);
    endLocType varchar2(15);
begin
    startingFloor := 0;
    startLocType := '';
    endingFloor := 0;
    endLocType := '';
    
    select mapFloor, locationType into startingFloor, startLocType
    from Locations L
    where locationID = :new.startingLocationID;
    
    select mapFloor, locationType into endingFloor, endLocType
    from Locations L
    where locationID = :new.endingLocationID;
    
    if (startingFloor <> endingFloor) then
        if not ((startLocType like '%Elevator%' and endLocType like '%Elevator%') or (startLocType like '%Stair%' and endLocType like '%Stair%')) then
            RAISE_APPLICATION_ERROR(-20004, 'Cannot insert record.');
        end if;
    end if;
end;
/

/*
For Project 2, the enforcement of Locations inheritance to be disjoint will be done using a trigger instead
of using Roles (locationType). An office cannot be located in non-office locations, i.e. the locationType
must be ‘Office’. An error message will result when a new office is added to Offices when the matching
locationID in Locations is not of locationType 'Office'. Check the existing Offices records as well as any new
office records being entered. Create this trigger named “MustBeOffice” using a cursor.
*/
drop trigger MustBeOffice;

create or replace trigger MustBeOffice
before insert on Offices
for each row
declare
    cursor c1 is select officeID from Offices join Locations on officeID = locationID
    where locationType not like 'Office';
begin
for rec in c1 loop
    RAISE_APPLICATION_ERROR(-20004, 'LocationID not pointing to Office');
end loop;
end;
/

/*
Professors cannot have more than 3 titles otherwise an error message will result. Create a statement-level
trigger named TitleLimit that will check for violations when inserts or updates are made.
*/

create or replace trigger TitleLimit
after insert or update on CSStaffTitles
declare
numTitles number;
begin
numTitles := 0;
select max(counts) into numTitles
from (select accountName, acronym from CSStaffTitles) A join
(select accountName, count(acronym) as counts from CSStaffTitles group by accountName) B on A.accountName = B.accountName
where A.acronym like '%Prof%';
if (numTitles > 3) then
    RAISE_APPLICATION_ERROR(-20004, 'Cannot insert record.');
end if;
end;
/

/*
Insert records to test the triggers above.
*/

insert into Edges values('2H15_2H15', '2H15', '2H15');
insert into Edges values('2S2_2S2', '2S2', '2S2');

insert into Edges values('2S2_3H2', '2S2', '3H2');
insert into Edges values('2H2_3H2', '2H2', '3H2');

insert into Offices values('2S2');
insert into Offices values('2H15');
insert into Offices values ('A21');

insert into CSStaffTitles values('cew', 'Dir-DS');
insert into CSStaffTitles values('cew', 'Admin 5');