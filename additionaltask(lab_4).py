class Film:

    genre = ""          
    release_year = 0   

    def __init__(self, name="", duration=0, reviews=0, tickets_sold=0, budget=0):
        
        self.__name = name
        self.__duration = duration
        self.__reviews = reviews
        self.__tickets_sold = tickets_sold
        self.__budget = budget

    
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

    def get_tickets_sold(self):
        return self.__tickets_sold

    def set_tickets_sold(self, tickets_sold):
        self.__tickets_sold = tickets_sold

    def get_budget(self):
        return self.__budget

    def set_budget(self, budget):
        self.__budget = budget

    def increment_reviews(self):
        self.__reviews += 1

    def __str__(self):
        return (f"Film(Name: {self.__name}, Duration: {self.__duration} min, Reviews: {self.__reviews}, "
                f"Tickets Sold: {self.__tickets_sold}, Budget: {self.__budget} USD)")

    def __repr__(self):
        return (f"Film(name='{self.__name}', duration={self.__duration}, reviews={self.__reviews}, "
                f"tickets_sold={self.__tickets_sold}, budget={self.__budget})")

def main():

    film1 = Film("Inception", 148, 2000000, tickets_sold=30000000, budget=160000000)
    film2 = Film("Interstellar", 169, 1500000, tickets_sold=28000000, budget=165000000)
    film3 = Film("The Dark Knight", 152, 2300000, tickets_sold=35000000, budget=185000000)

    film1.genre = "Sci-Fi"
    film1.release_year = 2010

    film2.genre = "Sci-Fi"
    film2.release_year = 2014

    film3.genre = "Action"
    film3.release_year = 2008

    film1.increment_reviews()
    film2.increment_reviews()
    film3.increment_reviews()

    print(film1)
    print(f"Genre: {film1.genre}, Release Year: {film1.release_year}\n")

    print(film2)
    print(f"Genre: {film2.genre}, Release Year: {film2.release_year}\n")

    print(film3)
    print(f"Genre: {film3.genre}, Release Year: {film3.release_year}\n")

    films = [film1, film2, film3]
    unsuccessful_film = max(films, key=lambda f: f.get_budget() - f.get_reviews())

    print("Unsuccessful Film:")
    print(unsuccessful_film)

if __name__ == "__main__":
    main()