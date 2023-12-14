-- list all tv genres name that exist in tv show genres
SELECT tv_genres.`name` FROM tv_genres INNER JOIN tv_show_genres
WHERE tv_show_genres.show_id = 8 AND tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_genres.`name`;
