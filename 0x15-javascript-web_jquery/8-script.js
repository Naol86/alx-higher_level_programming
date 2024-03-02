$.get("https://swapi-api.alx-tools.com/api/films/?format=json",
    function (data) {
        $('#list_movies').text(data['results'][0]['title']);
    }
);
