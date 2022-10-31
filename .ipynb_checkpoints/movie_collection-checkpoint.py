from customize_collection import Stack

class Movie:
    def __init__(self, movie_name, duration) -> None:
        self.movieName = movie_name
        self.duration = duration
    def __str__(self) -> str:
        return f"{self.movieName}, duration: {self.duration}"
    def to_string(self):
        return self.__str__()

class MovieCollection:
    '''
    MovieCollection works as Last In First out strategy. Recently added movie will be showed first
    So we use Stack to demonstrate this algorithm
    '''
    def __init__(self) -> None:
        self.movies = Stack()

    def insert(self, movie):
        '''
        Insert movie to movie stack
        '''
        self.movies.push(movie)
    
    def displayMovie(self):
        '''
        Description: After the movie has been shown once, it is discarded
        '''
        latest_movie = self.movies.pop()
        return latest_movie
        #print(f'Movies: {latest_movie} is displaying')

# if __name__ == '__main__':
#     m1 = Movie('Normal people', 120)
#     m2 = Movie('Titanic', 200)

#     movies = MovieCollection()
#     movies.insert(m1)
#     movies.insert(m2)
#     movies.displayMovie()
    