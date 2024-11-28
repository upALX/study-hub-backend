--Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 1372345 Truncate your answer to  decimal places.
SELECT ROUND(MAX(LAT_N), 4) FROM STATION WHERE LAT_N < 137.2345;
--Query a count of the number of cities in CITY having a Population larger than 100000.
SELECT COUNT(*) FROM CITY WHERE POPULATION > 100000;
--Query the total population of all cities in CITY where District is California.
SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California';
--Query the average population of all cities in CITY where District is California.
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';
--Query the average population for all cities in CITY, rounded down to the nearest integer.
SELECT ROUND(AVG(POPULATION)) FROM CITY;
--Query the sum of the populations for all Japanese cities in CITY. The COUNTRYCODE for Japan is JPN.
SELECT SUM(POPULATION) FROM CITY WHERE COUNTRYCODE = 'JPN';
--Query the difference between the maximum and minimum populations in CITY.
SELECT MAX(POPULATION) - MIN(POPULATION)  FROM CITY; 
--Query the following two values from the STATION table:
--The sum of all values in LAT_N rounded to a scale of  decimal places.
--The sum of all values in LONG_W rounded to a scale of  decimal places.
SELECT ROUND(SUM(LAT_N), 2), ROUND(SUM(LONG_W), 2) FROM STATION;
--Query the sum of Northern Latitudes (LAT_N) from STATION having values greater than 38.7889 and less than 137.2345. Truncate your answer to  decimal places.
SELECT ROUND(SUM(LAT_N), 4) FROM STATION WHERE LAT_N > 38.7880 AND LAT_N < 137.2345;  
--Query the Western Longitude (LONG_W) for the largest Northern Latitude (LAT_N) in STATION that is less than 137,2345. Round your answer to 4 decimal places.
SELECT ROUND(MAX(LONG_W), 4) FROM STATION WHERE LAT_N = (SELECT MAX(LAT_N) FROM STATION WHERE LAT_N < 137.2345);
--Query the smallest Northern Latitude (LAT_N) from STATION that is greater than 38.7780. Round your answer to  decimal places.
SELECT ROUND(MIN(LAT_N), 4) FROM STATION WHERE LAT_N > 38.7780; 
--Query the Western Longitude (LONG_W)where the smallest Northern Latitude (LAT_N) in STATION is greater than . Round your answer to  decimal places.
SELECT ROUND(LONG_W, 4) FROM STATION WHERE LAT_N = (SELECT MIN(LAT_N) FROM STATION WHERE LAT_N > 38.7780);
-- Samantha was tasked with calculating the average monthly salaries for all employees in the EMPLOYEES table, but did not realize her keyboard's  key was broken until after completing the calculation. She wants your help finding the difference between her miscalculation (using salaries with any zeros removed), and the actual average salary.

-- Write a query calculating the amount of error (i.e.:  average monthly salaries), and round it up to the next integer.
SELECT CEIL(ABS(AVG(Salary) - AVG(CAST(REPLACE(CAST(Salary AS CHAR), '0', '') AS DECIMAL)))) 
FROM EMPLOYEES;
-- We define an employee's total earnings to be their monthly  worked, and the maximum total earnings to be the maximum total earnings for any employee in the Employee table. Write a query to find the maximum total earnings for all employees as well as the total number of employees who have maximum total earnings. Then print these values as  space-separated integers.
SELECT MAX(SALARY * MONTHS), COUNT(*) FROM EMPLOYEE WHERE SALARY * MONTHS = (SELECT MAX(SALARY * MONTHS) FROM EMPLOYEE);
-- Consider  and  to be two points on a 2D plane.
--  happens to equal the minimum value in Northern Latitude (LAT_N in STATION).
--  happens to equal the minimum value in Western Longitude (LONG_W in STATION).
--  happens to equal the maximum value in Northern Latitude (LAT_N in STATION).
--  happens to equal the maximum value in Western Longitude (LONG_W in STATION).
-- Query the Manhattan Distance between points  and  and round it to a scale of  decimal places.
SELECT ROUND(ABS(ABS(MIN(LAT_N) + MIN(LONG_W)) - ABS(MAX(LAT_N) + MAX(LONG_W))), 4) FROM STATION;
--OR
SELECT ROUND(
    (ABS(MAX(LAT_N) - MIN(LAT_N)) + ABS(MAX(LONG_W) - MIN(LONG_W))),
    4
) AS manhattan_distance
FROM STATION;
