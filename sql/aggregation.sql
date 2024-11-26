--Query the greatest value of the Northern Latitudes (LAT_N) from STATION that is less than 1372345 Truncate your answer to  decimal places.
SELECT ROUND(MAX(LAT_N), 4) FROM STATION WHERE LAT_N < 137.2345;
--Query a count of the number of cities in CITY having a Population larger than 100000.
SELECT COUNT(*) FROM CITY WHERE POPULATION > 100000;
--Query the total population of all cities in CITY where District is California.
SELECT SUM(POPULATION) FROM CITY WHERE DISTRICT = 'California';
--Query the average population of all cities in CITY where District is California.
SELECT AVG(POPULATION) FROM CITY WHERE DISTRICT = 'California';