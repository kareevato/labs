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
        if hasattr(self, "_Film__name"):  
            print(f"Deleting Film '{self.__name}' from memory")
        else:
            print("Deleting unknown Film from memory")

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

    films = [film1, film2, film3]

    for film in films:
        film.increment_reviews()
        print(film)
        print(f"Genre: {film.genre}, Release Year: {film.release_year}\n")

    unsuccessful_film = films[0]
    max_difference = films[0].get_budget() - films[0].get_reviews()

    for film in films[1:]:  
        difference = film.get_budget() - film.get_reviews()
        if difference > max_difference:
            max_difference = difference
            unsuccessful_film = film

    print("Unsuccessful Film:")
    print(unsuccessful_film)

if __name__ == "__main__":
    main()