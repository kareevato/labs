class Film:
    genre = ""          
    release_year = 0    


    def __init__(self, name="", duration=0, reviews=0):
        
        self.set_name(name)
        self.set_duration(duration)
        self.set_reviews(reviews)

    def __del__(self):
        name = getattr(self, "_Film__name", "unknown")  
        print(f"Deleting Film '{name}' from memory")

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_duration(self):
        return self.__duration

    def set_duration(self, duration):
        self.__duration = duration

    def get_reviews(self):
        return self.__reviews

    def set_reviews(self, reviews):
        self.__reviews = reviews

    def __str__(self):
        return f"Film(Name: {self.__name}, Duration: {self.__duration} min, Reviews: {self.__reviews})"

    def __repr__(self):
        return f"Film(name='{self.__name}', duration={self.__duration}, reviews={self.__reviews})"


def main():
    
    film1 = Film("Inception", 148, 2000000)
    film2 = Film("Interstellar", 169, 1500000)
    film3 = Film("The Dark Knight", 152, 2300000)

    film1.genre = "Sci-Fi"
    film1.release_year = 2010

    film2.genre = "Sci-Fi"
    film2.release_year = 2014

    film3.genre = "Action"
    film3.release_year = 2008

    print(film1)
    print(f"Genre: {film1.genre}, Release Year: {film1.release_year}\n")

    print(film2)
    print(f"Genre: {film2.genre}, Release Year: {film2.release_year}\n")

    print(film3)
    print(f"Genre: {film3.genre}, Release Year: {film3.release_year}\n")

if __name__ == "__main__":
 main()
