from kinopoisk.movie import Movie
film_name = input("Введите название фильма: ")
movie_list = Movie.objects.search(film_name)
for movie in movie_list:
    print(movie.actors)


# print(type(movie_list))
# print(movie_list)
# len(movie_list)
# print(movie_list[0].title)
