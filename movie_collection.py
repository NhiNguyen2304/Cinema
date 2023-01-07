import random
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
    
    def display_movie(self):
        '''
        Description: After the movie has been shown once, it is discarded
        '''
        latest_movie = self.movies.pop()
        return latest_movie
        #print(f'Movies: {latest_movie} is displaying')
    
    def receive_movie(self, input_random_num = 3):
        #Simulate receive new movies at random times,
        #movies = MovieCollection()

        # copy for favourite movie
        fav_movie = Movie('Titanic', 200)

        #inital movie list with some movies
        m2 = Movie("Spider men", 135)
        m3 = Movie("Avatar", 225)
        self.movies.push(m2)
        self.movies.push(m3)

        # Initial a movie is random movie that cinema will receive
        random_movie = Movie('Normal people', 120)

        # Random receive movie at a random timing (use random generates a number from 0 => 3.)
        if random.randint(0,3) == input_random_num:
            print("######## Receive a new movie #########")
            self.movies.push(random_movie)
        else:
            print(f"######## Waiting for too long for a new movie. So add a movie from favourite movie {fav_movie} ########")
            self.movies.push(fav_movie)
        
        return self.movies

if __name__ == '__main__':

    movies = MovieCollection()
    movies.receive_movie()
