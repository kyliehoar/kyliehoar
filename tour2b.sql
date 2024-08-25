-- List for each level of guide how many mismatches there are between the required tour's vehicle type and the guide's license type
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
    
-- Update the ReservedTours prices based on prices in Tours
update ReservedTour set price = 
    (select price from Tour where ReservedTour.tourID = Tour.tourID);
select * from ReservedTour;

-- For each customer list the first name, last name, and total amount being spent for land-based tours
-- Format the price so it is displayed with 2 decimals
-- If price is less than 1, make sure there is a leading 0
-- Sort price in descending order
select C.firstName, C.lastName, to_char(T.price, '990.90') as TotalLandPrice
from ReservedTour RT
    join Customer C on RT.customerID = C.customerID
    join Tour T on RT.tourID = T.tourID
where (T.vehicleType like 'bus' or T.vehicleType like 'car')
order by T.price DESC, C.lastName, C.firstName;

-- For each vehicle type needed for a tour, list the number of locations that the vehicle type will be used for in a given location type
select T.vehicleType, L.locationType, count(L.locationType) as Places
from Tour T
    join Location L on T.tourID = L.tourID
group by T.vehicleType, L.locationType
having count(L.locationType) > 1;

-- List the full name of a guide and the total price with a tax of %10 of the tours that the guide is responsible for
-- Make sure there is a comma for the thousands place, 2 decimals, and no leading 0 for values less than 1
select G.firstName || ' ' || G.lastName as GuideName, to_char(sum(RT.price*1.1), '99,999.99') as TotalRevenue
from Guide G
    join ReservedTour RT on G.guideID = RT.guideID
group by G.firstName, G.lastName;