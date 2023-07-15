def movie_organizer(*args):
    result = {}

    for movie_name, gen in args:
        if gen not in result:
            result[gen] = []
        result[gen].append(movie_name)

    sorted_movies = sorted(result.items(), key=lambda x: (-len(x[1]), x[0]))

    res = ''
    for genre, movies in sorted_movies:
        movies = sorted(movies)
        res += f"{genre} - {len(movies)}\n"
        for x in movies:
            res += f"* {x}\n"

    return res.strip()

print(movie_organizer(
    ("Avatar: The Way of Water", "Action"),
    ("House Of Gucci", "Drama"),
    ("Top Gun", "Action"),
    ("Ted", "Comedy"),
    ("Duck Soup", "Comedy"),
    ("The Dark Knight", "Action"),
    ("A Star Is Born", "Musicals"),
    ("The Warrior", "Action"),
    ("Like A Boss", "Comedy"),
    ("The Green Mile", "Drama"),
    ("21 Jump Street", "Comedy")))
