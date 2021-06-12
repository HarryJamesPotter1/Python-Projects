import imdb

a = imdb.IMDb()
movie_name = input("Enter the name of the movie: ")
movies = a.search_movie_advanced((str(movie_name)))
index = movies[0].getID()
movie = a.get_movie(index)
movie_title = movie["title"]
movie_year = movie["year"]
movie_cast = movie["cast"]
list_of_cast = ",".join(map(str, movie_cast))
print("Title of the movie is: ", movie_title)
print("Year of Release of the Movie: ", movie_year)
print("Full cast of the movie: ", movie_cast)

