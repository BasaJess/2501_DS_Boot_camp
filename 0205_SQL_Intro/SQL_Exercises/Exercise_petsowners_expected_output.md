# At the Vet

*Note: This markdown files contains the questions as well as the expected outputs of the queries you need to run in order to answer them.*

You are assisting a vet clinic in making sense of their data. Their data is in two tables. And they need you tu perform the following analytics:

1. How many pets, how many owners? Hint: [Use COUNT()](https://www.postgresql.org/docs/8.2/functions-aggregate.html)

Expected output pets:
![expected output pets](images/../../images/1.1_Pets.png)
Expected output owners:
![expected output pets](images/../../images/1.1_Owners.png)

2. What are the most and least common pet names? Hint: [Use ORDER BY](https://www.postgresql.org/docs/8.1/queries-order.html)

Expected Output most common name: 
![expected output most common name](../images/1.2_Petname_most_common.png)
Expected Output least common name: 
![expected output least common name](../images/1.2_Petname_least_common.png)

3. What kind of pets do we have? Hint: [Use DISTINCT](https://www.postgresql.org/docs/9.5/sql-select.html)
   
Expected output:
![expected output pet type](../images/1.3_Pet_type.png)

4. What is the gender balance across pets and species? Hint: [Use GROUP BY](https://www.postgresql.org/docs/9.4/tutorial-agg.html)

Expected output gender balance pets:
![expected output gender balance pets](images/../../images/1.4_gender_pets.png)
Expected output gender balance pets by kind:
![expected output gender balance pets by kind](images/../../images/1.4_gender_pet_type.png)

5. What is the average age of the pets? Hint: [Use AVG()](https://www.postgresql.org/docs/9.4/tutorial-agg.html)

Expected output: 
![expected output average age](image/../../images/1.5_avg_age.png)

6. How many owners have more than one pet? Hint: [Use GROUP BY HAVING](https://www.postgresql.org/docs/9.4/tutorial-agg.html)

Expected output: 
![expected output owner of more pets](image/../../images/1.6_owner_more_pets.png)

7. Do the owners that have more than one pet have the same kind of pet. [Use ARRAY_AGG](https://www.postgresqltutorial.com/postgresql-aggregate-functions/postgresql-array_agg/)
   
Expected output (one possible approach): 
![expected output](image/../../images/1.7_different_kinds_per_owner.png)

8. Do owners name their pets like owners? Hint: [Use INNER JOIN](https://www.postgresql.org/docs/8.3/tutorial-join.html)

Expected output: 
![expected output same name](image/../../images/1.8_same_name.png)

9.  Extract the information of pet names and owners side-by-side! Hint: [Use FULL JOIN](https://www.postgresql.org/docs/8.3/tutorial-join.html)

Expected output (only first rows shown):
![expected output](image/../../images/1.9_information_side_by_side.png)

10.  What are the cities with the largest amount (top 3) of pets? Hint: [Use INNER JOIN](https://www.postgresql.org/docs/8.3/tutorial-join.html)

Expected output: 
![expected output cities with most pets](image/../../images/1.10_cities_most_pets.png)


## Let's look at some of the procedures those pets had.

1. Combine the tables with the procedure history and the procedure details. You might have to join tables based on more than one column...

Expected output (one possible approach): 
![expected output](image/../../images/2.1_matching_tables.png)

2. What pets didn't get rabies vaccination? Hint: [Use LEFT JOIN](https://www.postgresql.org/docs/8.3/tutorial-join.html), [Use ARRAY_AGG()](https://www.postgresql.org/docs/8.2/functions-aggregate.html) and [Use ALL()](https://www.postgresql.org/docs/9.1/functions-comparisons.html)
   
Expected output (first part): 
![expected output](image/../../images/2.2_no_rabies.png)

3. What is the most prevalent type of surgery? Hint: [Use IS NOT NULL](https://www.postgresql.org/docs/8.3/functions-comparison.html)

Expected output: 
![expected output](image/../../images/2.3_prevalent_surgery.png)

4. What owner spent the most on their pet and how much was it? Hint: [Use SUM()](https://www.postgresql.org/docs/8.2/functions-aggregate.html)

Expected output: 
![expected output](image/../../images/2.4_most_spent.png)

5. Look at the data and ask yourself what more questions one could ask!
