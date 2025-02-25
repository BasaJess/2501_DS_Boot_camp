
SET SCHEMA 'petsowners';

--1. How many pets, how many owners? Hint: [Use COUNT()](https://www.postgresql.org/docs/8.2/functions-aggregate.html)
SELECT count(*) FROM owners;

SELECT count(*) FROM pets;

--2. What are the most and least common pet names? Hint: [Use ORDER BY](https://www.postgresql.org/docs/8.1/queries-order.html)

SELECT pets.name, count(*) AS number_of_pets
FROM  pets 
GROUP BY pets.name
ORDER BY number_of_pets DESC;

--3. What kind of pets do we have? Hint: [Use DISTINCT](https://www.postgresql.org/docs/9.5/sql-select.html)

SELECT DISTINCT(kind) 
FROM pets ;

--4. What is the gender balance across pets and species? Hint: [Use GROUP BY]

SELECT pets.gender, pets.kind, count(*) AS number_of_pets_per_gender
FROM  pets 
GROUP BY pets.gender, pets.kind
ORDER BY number_of_pets_per_gender DESC;

--5. What is the average age of the pets? Hint: [Use AVG()]

SELECT AVG(pets.age) 
FROM pets ;

--6. How many owners have more than one pet? Hint: [Use GROUP BY HAVING]

SELECT petid, COUNT(*)
FROM pets
GROUP BY petid
HAVING COUNT(*) > 1; 

SELECT ownerid, count(*)
    FROM pets
    GROUP BY ownerid
    HAVING COUNT(ownerid) > 1;

SELECT COUNT(*) AS num_owners_with_multiple_pets
FROM (
    SELECT ownerid, count(*)
    FROM pets
    GROUP BY ownerid
    HAVING COUNT(ownerid) > 1
) AS owners_with_multiple_pets; 


--7. Do the owners that have more than one pet have the same kind of pet.

SELECT ownerid, ARRAY_AGG(DISTINCT kind)
FROM pets
GROUP BY ownerid
Having COUNT(*) > 1 ;

--some of them have multiple pets!!

--8 Do owners name their pets like owners?
SELECT o.*, p.*
FROM owners o
INNER JOIN  pets p ON o.ownerid = p.ownerid
WHERE o.name = p.name;

SELECT o.*, p.*
FROM pets p 
INNER JOIN owners o ON o.ownerid = p.ownerid
WHERE o.name = p.name;

-- 9 Extract the information of pet names and owners side-by-side!

SELECT p.name AS pet_name, o.name AS owner_name
FROM pets p
FULL JOIN owners o ON o.ownerid = p.ownerid
ORDER BY pet_name ;


--10. What are the cities with the largest amount (top 3) of pets? 

SELECT  o.city AS city_name, count(p.petid) AS number_of_pets
FROM pets p
FULL JOIN owners o ON o.ownerid = p.ownerid
GROUP BY o.city
ORDER BY number_of_pets DESC
LIMIT 3;


-- Part 2 : Let's look at some of the procedures those pets had.

--1 Combine the tables with the procedure history and the procedure details.
SELECT ph.petid , ph.proceduredate , ph.proceduretype , ph.proceduresubcode , pd.description , pd.price 
FROM procedurehistory ph
LEFT JOIN proceduredetails pd ON (ph.proceduretype = pd.proceduretype AND ph.proceduresubcode =pd.proceduresubcode );



--2 What pets did't get rabies vaccination?
-- ALl pets who DID get a rabies vaccination
SELECT ph.petid , ph.proceduredate , ph.proceduretype , ph.proceduresubcode , pd.description , pd.price 
FROM procedurehistory ph
LEFT JOIN proceduredetails pd ON (ph.proceduretype = pd.proceduretype AND ph.proceduresubcode =pd.proceduresubcode )
WHERE pd.description  = 'Rabies';

-- First solution to get all pets who did not get a vaccination, using the query above and NOT IN
SELECT distinct(petid)
FROM procedurehistory
WHERE petid NOT IN (
SELECT ph.petid
FROM procedurehistory ph
LEFT JOIN proceduredetails pd ON (ph.proceduretype = pd.proceduretype AND ph.proceduresubcode =pd.proceduresubcode )
WHERE pd.description  = 'Rabies');

-- Second solution to get all pets who did not get a vaccination, using the query above and ALL
SELECT distinct(petid)
FROM procedurehistory
WHERE petid != ALL (
SELECT ph.petid
FROM procedurehistory ph
LEFT JOIN proceduredetails pd ON (ph.proceduretype = pd.proceduretype AND ph.proceduresubcode =pd.proceduresubcode )
WHERE pd.description  = 'Rabies');

-- Solution provided by neue fische
SELECT t.petid from (
SELECT * FROM procedurehistory p 
LEFT JOIN proceduredetails p2 
ON p.proceduretype = p2.proceduretype AND p.proceduresubcode = p2.proceduresubcode) t
GROUP BY t.petid
HAVING 'Rabies' != ALL(array_agg(t.description)) ;

-- Testing array_agg, which only works with group by

SELECT t.petid, array_agg(t.description)from (
SELECT * FROM procedurehistory p 
LEFT JOIN proceduredetails p2 
ON p.proceduretype = p2.proceduretype AND p.proceduresubcode = p2.proceduresubcode) t;
GROUP BY t.petid;

-- task 3: What is the most prevalent type of surgery? 

SELECT pd.description, count(*)
FROM procedurehistory ph
LEFT JOIN proceduredetails pd
ON (ph.proceduretype = pd.proceduretype AND ph.proceduresubcode = pd.proceduresubcode)
WHERE ph.proceduretype = 'GENERAL SURGERIES'
GROUP BY pd.description
ORDER BY count(*) DESC;

--task 4: What owner spent the most on their pet and how much was it?


SET search_path TO 'petsowners';

SELECT o.name, o.surname , p.ownerid, sum(pd.price)
FROM pets p
LEFT JOIN owners o ON p.ownerid = o.ownerid
INNER JOIN procedurehistory ph  ON ph.petid = p.petid
LEFT JOIN proceduredetails pd ON (ph.proceduretype = pd.proceduretype AND ph.proceduresubcode = pd.proceduresubcode)
GROUP BY p.ownerid, o.name, o.surname
ORDER BY sum(pd.price) DESC
LIMIT 1;









