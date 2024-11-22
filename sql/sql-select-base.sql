

SELECT * FROM CITY WHERE COUNTRYCODE = 'USA' AND population > 100000;

--Query the NAME field for all American cities in the CITY table with populations larger than 120000. The CountryCode for America is USA.
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'USA' AND POPULATION > 120000;

--Query all in city table
SELECT * FROM CITY;
--Query all columns for a city in CITY with the ID 1661.
SELECT * FROM CITY where ID = 1661;
--Query all attributes of every Japanese city in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT * FROM CITY WHERE COUNTRYCODE = 'JPN';
--Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.
SELECT NAME FROM CITY WHERE COUNTRYCODE = 'JPN';
--Query a list of CITY and STATE from the STATION table.
SELECT CITY, STATE from STATION;
--Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.
SELECT DISTINCT CITY FROM STATION WHERE MOD(ID, 2) = 0;
--Find the difference between the total number of CITY entries in the table and the number of distinct CITY entries in the table.
SELECT count(CITY) - count(distinct(CITY)) FROM STATION;
