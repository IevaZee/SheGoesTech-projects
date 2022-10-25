SELECT * FROM north_american_cities
WHERE country = "Canada";
SELECT * FROM north_american_cities
WHERE country = "United States"	
ORDER BY latitude DESC;
SELECT * FROM north_american_cities
WHERE longitude < -87.629798
ORDER BY longitude ASC;
SELECT * FROM north_american_cities
WHERE country = "Mexico"
ORDER BY population DESC
LIMIT 2;
SELECT * FROM north_american_cities
WHERE country = "United States"
ORDER BY population DESC
LIMIT 2 OFFSET 2