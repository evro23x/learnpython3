from kinopoisk.movie import Movie
# movie_list = Movie.objects.search('Redacted')
# print(movie_list)
# len(movie_list)
# print(movie_list[0].title)
#
movie = Movie(id=278229)
movie.get_content('main_page')
print(movie)
movie.plot
print(movie.rating)
