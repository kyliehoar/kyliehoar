/*PART A - Decreasing prices of specific tours*/
update Tour set price = price - 100 
    where price > 100 AND (state like 'CA' OR state like 'NY');
Select * from Tour;

/*PART B - Print tour guide first and last name from specific skill levels or tours*/
/* order by last name*/
select distinct guide.firstname, guide.lastname
from reservedtour natural join guide natural join tour
where guide.title='Junior Guide' OR tour.tourName='Freedom Trail'
order by guide.lastname;

/*order by first name*/
select distinct guide.firstname, guide.lastname
from reservedtour natural join guide natural join tour
where guide.title='Junior Guide' OR tour.tourName='Freedom Trail'
order by guide.firstname;

/*PART C - Print data based on customer age or tour vehicle type*/
/*order by tour name*/
select reservedtour.traveldate, 
        customer.firstname || ' ' || customer.lastname as FullName, 
        customer.age, 
        tour.tourname
from reservedtour 
    join customer on reservedtour.customerid = customer.customerid 
    join tour on reservedtour.tourid = tour.tourid
where customer.age > 65 OR tour.vehicleType = 'boat'
order by tour.tourname;

/*order by full name*/
select reservedtour.traveldate, 
        customer.firstname || ' ' || customer.lastname as FullName, 
        customer.age, 
        tour.tourname
from reservedtour 
    join customer on reservedtour.customerid = customer.customerid 
    join tour on reservedtour.tourid = tour.tourid
where customer.age > 65 OR tour.vehicleType = 'boat'
order by FullName;

/*PART D - List tour guides part of each tour*/
select distinct tour.tourname, guide.firstname, guide.lastname
from reservedtour
    join tour on reservedtour.tourid = tour.tourid
    join guide on reservedtour.guideid = guide.guideid
order by tour.tourname;