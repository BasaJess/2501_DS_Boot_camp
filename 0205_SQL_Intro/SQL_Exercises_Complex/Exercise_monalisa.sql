SET SCHEMA 'monalisa';

--3. who all live in paris

SELECT *
FROM person p 
WHERE p.residence = 'Paris';

--4. Get all the names who travelled to Paris before 23.10.2014.

SELECT *
FROM flight f
WHERE dest_city = 'Paris' AND date < '2014-10-23' ;

--5. Get all the names who travelled from Paris after 23.10.2014.

SELECT *
FROM flight f
WHERE start_city = 'Paris' AND date > '2014-10-23';

--6. Get all the names who travelled to Paris before 23.10.2014, and whose names also appear in entries for journeys departing from Paris after 23.10.2014. 

SELECT *
FROM flight f
WHERE dest_city = 'Paris' AND date < '2014-10-23' AND f.name IN 
(SELECT name
FROM flight f
WHERE start_city = 'Paris' AND date > '2014-10-23') ;

--7. Get all the names of persons who live in Paris or who spent their time in Paris on 23.10.2014 (according to the travel data).

SELECT f.* , p.*
FROM person p
FULL JOIN flight f ON f.person_id = p.id
WHERE p.residence = 'Paris' OR( f.dest_city = 'Paris' AND date < '2014-10-23') OR (start_city = 'Paris' AND date > '2014-10-23') ;

--8. What foreign keys are used in the table containing the messages and which is the referenced table?

--contract sender id and contract receiver id are both foreign keys

--10. What are the names of the table containing the text messages and the ones containing phone contracts?

--messages and phone_contract

--11. Get all the text messages which were sent between 2014-10-20 and 2014-10-25.

SELECT m.*
FROM messages m
WHERE m.sent BETWEEN '2014-10-20' AND '2014-10-25';

--12. Get all the contract ids where the contract.person_id is equal to one of the persons from the results of question 7.

SELECT f.* , p.*, pc.*
FROM person p
FULL JOIN flight f ON f.person_id = p.id
FULL JOIN phone_contract pc ON pc.person_id = p.id
WHERE p.residence = 'Paris' OR( f.dest_city = 'Paris' AND date < '2014-10-23') OR (start_city = 'Paris' AND date > '2014-10-23') ;

--13. Get all text messages with the sent date between 2014-10-20 and 2014-10-25 and the contract_sender_id is equal to the contract ids. And where the contract.person_id is equal to one of the persons from the results of question 7.

SELECT  p.name, p.residence, m.message, m.sent, m.id, pc2.person_id, p2."name" 
FROM person p
FULL JOIN flight f ON f.person_id = p.id
FULL JOIN phone_contract pc ON pc.person_id = p.id
FULL JOIN messages m ON m.contract_sender_id = pc.id
FULL JOIN phone_contract pc2 ON pc2.id = m.contract_receiver_id 
FULL JOIN person p2 ON p2.id = pc2.person_id 
WHERE p.residence = 'Paris' OR
( f.dest_city = 'Paris' AND date < '2014-10-23') OR 
(start_city = 'Paris' AND date > '2014-10-23') AND
(m.sent BETWEEN '2014-10-20' AND '2014-10-25')
ORDER BY m.sent;