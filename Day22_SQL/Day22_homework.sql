-- SQL Lesson 6: Multi-table queries with JOINs:

SELECT * FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
SELECT * FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
WHERE international_sales > domestic_sales;
SELECT * FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
ORDER BY rating DESC


-- SQL Lesson 7: OUTER JOINs:

SELECT DISTINCT building FROM employees
LEFT JOIN buildings
    ON employees.building = buildings.building_name
WHERE name != "";
SELECT DISTINCT building_name, capacity FROM buildings
LEFT JOIN employees
    ON employees.building = buildings.building_name;
SELECT DISTINCT role, building_name FROM buildings
LEFT JOIN employees
    ON employees.building = buildings.building_name


-- SQL Lesson 8: A short note on NULLs

SELECT name, role FROM employees
WHERE building IS NULL;
SELECT DISTINCT building_name FROM buildings
LEFT JOIN employees
    ON employees.building = buildings.building_name
WHERE building IS NULL


-- SQL Lesson 9: Queries with expressions

SELECT title, ((domestic_sales+international_sales)/1000000) AS combined_sales
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
SELECT title, (rating*10) AS Rating_percent
FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id;
SELECT * FROM movies
WHERE year%2 == 0


-- SQL Lesson 10: Queries with aggregates (Pt. 1)

SELECT MAX(years_employed) FROM employees;
SELECT role, AVG(years_employed) FROM employees
GROUP BY role;
SELECT DISTINCT building, SUM(years_employed) FROM employees
GROUP BY building


-- SQL Lesson 11: Queries with aggregates (Pt. 2)

SELECT COUNT(role) FROM employees
WHERE role = "Artist";
SELECT role, COUNT(role) FROM employees
GROUP BY role;
SELECT role, SUM(years_employed) FROM employees
GROUP BY role
HAVING role = "Engineer"


-- SQL Lesson 12: Order of execution of a Query

SELECT DISTINCT director, COUNT(title) FROM movies
GROUP BY director;
SELECT DISTINCT director, SUM(domestic_sales+international_sales) AS combined_sales FROM movies
INNER JOIN boxoffice
    ON movies.id = boxoffice.movie_id
GROUP BY director


-- SQL Lesson 13: Inserting rows

INSERT INTO movies
(title, director)
VALUES ("Toy Story 4", "Lee Unkrich");
INSERT INTO boxoffice
(movie_id, rating, domestic_sales, international_sales)
VALUES (15, 8.7, 340*1000000, 270*1000000)


-- SQL Lesson 14: Updating rows

UPDATE movies
SET director = "John Lasseter"
WHERE title = "A Bug's Life";
UPDATE movies
SET year = 1999
WHERE title = "Toy Story 2";
UPDATE movies
SET title = "Toy Story 3", director = "Lee Unkrich"
where title = "Toy Story 8"


-- SQL Lesson 15: Deleting rows

DELETE FROM movies
WHERE year < 2005;
DELETE FROM movies
WHERE director = "Andrew Stanton"


-- SQL Lesson 16: Creating tables

CREATE TABLE database (
    name TEXT,
    version FLOAT,
    download_count INTEGER
)


-- SQL Lesson 17: Altering tables

ALTER TABLE movies
ADD aspect_ratio FLOAT;
ALTER TABLE movies
ADD language TEXT
    DEFAULT English


-- SQL Lesson 18: Dropping tables

DROP TABLE IF EXISTS movies;
DROP TABLE IF EXISTS boxoffice