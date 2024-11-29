-- Given the CITY and COUNTRY tables, query the names of all cities where the CONTINENT is 'Africa'.
-- Note: CITY.CountryCode and COUNTRY.Code are matching key columns.
SELECT c.NAME FROM CITY c LEFT JOIN COUNTRY co on co.Code = c.COUNTRYCODE WHERE co.CONTINENT = 'Africa';