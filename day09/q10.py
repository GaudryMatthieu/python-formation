#Create a class to represent a Movie with attributes like title, director, and rating

class Movies:
    def __init__(self, title, director, rating):
        self.title = title
        self.director = director
        self.rating = rating

def main():
    movie1 = Movies("Inception", "Christopher Nolan", 9.8)
    print(f"Movie Title: {movie1.title}\nDirector: {movie1.director}\nRating: {movie1.rating}")

if __name__ == '__main__':
    main()