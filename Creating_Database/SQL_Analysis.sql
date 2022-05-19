SELECT * FROM games;

/*Top five most sold games*/
SELECT name,sales_millions
FROM games
ORDER BY sales_millions DESC
LIMIT 5;

/*most popular genre*/
SELECT genre, COUNT(genre) AS count_genre
FROM games
GROUP BY genre
ORDER BY count_genre DESC;

/*most publisher*/
SELECT publisher, COUNT(publisher) AS count_publisher
FROM games
GROUP BY publisher
ORDER BY count_publisher DESC
LIMIT 5;

/*most developer*/
SELECT developer, COUNT(developer) AS count_developer 
FROM games GROUP BY developer
ORDER BY count_developer DESC
LIMIT 5;

/*most popular series*/
SELECT series, COUNT(series) AS count_series
FROM games
GROUP BY series
ORDER BY count_series DESC
LIMIT 5;

