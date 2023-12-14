-- this is selecting a tv genres that not have the same show with Dexter
SELECT tv_genres.`name` from tv_genres 
WHERE tv_genres.id NOT IN
(SELECT tv_genres.id FROM tv_genres
INNER JOIN tv_show_genres
ON tv_show_genres.genre_id = tv_genres.id
INNER JOIN tv_shows
ON tv_shows.id = tv_show_genres.show_id
WHERE tv_shows.id = 8)
ORDER BY tv_genres.`name`;
