-- lists number of shows by genre
SELECT tv_genres.name AS genre,
COUNT(*) AS number_of_shows from tv_show_genres
INNER JOIN tv_genres ON tv_show_genres.genre_id = tv_genres.id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
