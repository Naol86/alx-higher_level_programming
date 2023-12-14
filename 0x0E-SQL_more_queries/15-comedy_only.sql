-- select all comedy in tv shows
SELECT tv_shows.title FROM tv_shows INNER JOIN tv_show_genres
WHERE tv_shows.id = tv_show_genres.show_id AND tv_show_genres.genre_id = 5
ORDER BY tv_shows.title;
