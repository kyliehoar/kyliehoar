-- Assignment 2
-- Part 2.1
select G.title, count(G.licenseType) as Mismatches
from ReservedTour RT
    join Guide G on RT.guideID = G.guideID
    join Tour T on RT.tourID = T.tourID
where (G.licenseType like 'sea' and T.vehicleType like 'car') or
        (G.licenseType like 'sea' and T.vehicleType like 'bus') or
        (G.licenseType like 'land' and T.vehicleType like 'boat')
group by G.title;

/*
The reason why natural joins would give you the wrong answer here is because natural joins are based on joining tables with common attributes.
Because in this problem we are comparing License Type from Guide with Vehicle Type from Tour, these are different attributes and may produce
a false answer where natural joins are concerned.
*/
    
-- Part 2.2
update ReservedTour set price = 
    (select price from Tour where ReservedTour.tourID = Tour.tourID);
select * from ReservedTour;

-- Part 2.3
select C.firstName, C.lastName, to_char(T.price, '990.90') as TotalLandPrice
from ReservedTour RT
    join Customer C on RT.customerID = C.customerID
    join Tour T on RT.tourID = T.tourID
where (T.vehicleType like 'bus' or T.vehicleType like 'car')
order by T.price DESC, C.lastName, C.firstName;

-- Part 2.4
select T.vehicleType, L.locationType, count(L.locationType) as Places
from Tour T
    join Location L on T.tourID = L.tourID
group by T.vehicleType, L.locationType
having count(L.locationType) > 1;

-- Part 2.5
select G.firstName || ' ' || G.lastName as GuideName, to_char(sum(RT.price*1.1), '99,999.99') as TotalRevenue
from Guide G
    join ReservedTour RT on G.guideID = RT.guideID
group by G.firstName, G.lastName;