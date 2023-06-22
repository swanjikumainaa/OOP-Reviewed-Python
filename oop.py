# 1. **Ancestral Stories:** In many African cultures, the art of storytelling is passed
# down from generation to generation. Imagine you're creating an application that
# records these oral stories and translates them into different languages. The
# stories vary by length, moral lessons, and the age group they are intended for.
# Think about how you would model `Story`, `StoryTeller`, and `Translator`
# objects, and how inheritance might come into play if there are different types of
# stories or storytellers.

class Story:
    def __init__(self, length, moral_lessons, age_group):
        self.length = length
        self.moral_lessons = moral_lessons
        self.age_group = age_group

    def read(self):
        print("Reading the story")  

    def translate(self, language):
        print(f"Translating the story into {language}")  


class StoryTeller:
    def __init__(self, name, style):
        self.name = name
        self.style = style

    def tell_story(self, story):
        print(f"{self.name} is telling a story")  


class Translator:
    def __init__(self, languages):
        self.languages = languages

    def translate_story(self, story, language):
        print(f"Translating the story into {language}")  



story = Story(length="Medium", moral_lessons=["Unity", "Respect"], age_group="Children")
storyteller = StoryTeller(name="John Doe", style="Engaging")
translator = Translator(languages=["English", "Swahili", "French"])

story.read()
story.translate(language="Swahili")
storyteller.tell_story(story)
translated_story = translator.translate_story(story, language="Swahili")


# 2. **African Cuisine:** You're creating a recipe app specifically for African cuisine.
# The app needs to handle recipes from different African countries, each with its
# unique ingredients, preparation time, cooking method, and nutritional
# information. Consider creating a `Recipe` class, and think about how you might
# create subclasses for different types of recipes (e.g., `MoroccanRecipe`,
# `EthiopianRecipe`, `NigerianRecipe`), each with their own unique properties and
# methods.

class Recipe:
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info):
        self.name = name
        self.ingredients = ingredients
        self.preparation_time = preparation_time
        self.cooking_method = cooking_method
        self.nutritional_info = nutritional_info

    def display_recipe(self):
        print(f"Recipe: {self.name}")
        print("Ingredients:")
        for ingredient in self.ingredients:
            print(f"- {ingredient}")
        print(f"Preparation Time: {self.preparation_time} minutes")
        print(f"Cooking Method: {self.cooking_method}")
        print("Nutritional Information:")
        for key, value in self.nutritional_info.items():
            print(f"- {key}: {value}")


class MoroccanRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, spice_level):
        super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
        self.spice_level = spice_level

    def display_recipe(self):
        super().display_recipe()
        print(f"Spice Level: {self.spice_level}")


class EthiopianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, injera_required):
        super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
        self.injera_required = injera_required

    def display_recipe(self):
        super().display_recipe()
        print(f"Injera Required: {self.injera_required}")


class NigerianRecipe(Recipe):
    def __init__(self, name, ingredients, preparation_time, cooking_method, nutritional_info, jollof_rice_level):
        super().__init__(name, ingredients, preparation_time, cooking_method, nutritional_info)
        self.jollof_rice_level = jollof_rice_level

    def display_recipe(self):
        super().display_recipe()
        print(f"Jollof Rice Level: {self.jollof_rice_level}")



recipe1 = MoroccanRecipe(
    name="Moroccan Tajine",
    ingredients=["Chicken", "Onions", "Tomatoes", "Spices"],
    preparation_time=30,
    cooking_method="Slow cooking",
    nutritional_info={"Calories": 350, "Protein": 25},
    spice_level="Medium"
)

recipe2 = EthiopianRecipe(
    name="Ethiopian Doro Wat",
    ingredients=["Chicken", "Onions", "Berbere Spice Mix", "Injera"],
    preparation_time=45,
    cooking_method="Stewing",
    nutritional_info={"Calories": 400, "Protein": 30},
    injera_required=True
)

recipe3 = NigerianRecipe(
    name="Nigerian Jollof Rice",
    ingredients=["Rice", "Tomatoes", "Pepper", "Onions"],
    preparation_time=40,
    cooking_method="One-pot cooking",
    nutritional_info={"Calories": 300, "Protein": 20},
    jollof_rice_level="Very Spicy"
)


recipe1.display_recipe()

recipe2.display_recipe()

recipe3.display_recipe()

# 3. **Wildlife Preservation:** You're a wildlife conservationist working on a
# program to track different species in a national park. Each species has its own
# characteristics and behaviors, such as its diet, typical lifespan, migration
# patterns, etc. Some species might be predators, others prey. You'll need to

# create classes to model `Species`, `Predator`, `Prey`, etc., and think about how
# these classes might relate to each other through inheritance.

class Species:
    def __init__(self, name, diet, lifespan):
        self.name = name
        self.diet = diet
        self.lifespan = lifespan

    def display_info(self):
        print(f"Species: {self.name}")
        print(f"Diet: {self.diet}")
        print(f"Lifespan: {self.lifespan} years")


class Predator(Species):
    def __init__(self, name, diet, lifespan, hunting_method):
        super().__init__(name, diet, lifespan)
        self.hunting_method = hunting_method

    def display_info(self):
        super().display_info()
        print(f"Hunting Method: {self.hunting_method}")


class Prey(Species):
    def __init__(self, name, diet, lifespan, migration_pattern):
        super().__init__(name, diet, lifespan)
        self.migration_pattern = migration_pattern

    def display_info(self):
        super().display_info()
        print(f"Migration Pattern: {self.migration_pattern}")


species1 = Predator("Lion", "Carnivore", 15, "Ambush hunting")
species2 = Prey("Wildebeest", "Herbivore", 20, "Seasonal migration")

species1.display_info()

species2.display_info()


# 4. **African Music Festival:** You're in charge of organizing a Pan-African music
# festival. Many artists from different countries, each with their own musical style
# and instruments, are scheduled to perform. You need to write a program to
# manage the festival lineup, schedule, and stage arrangements. Think about how
# you might model the `Artist`, `Performance`, and `Stage` classes, and consider
# how you might use inheritance if there are different types of performances or
# stages.

class Artist:
    def __init__(self, name, country, musical_style):
        self.name = name
        self.country = country
        self.musical_style = musical_style

    def display_info(self):
        print(f"Artist: {self.name}")
        print(f"Country: {self.country}")
        print(f"Musical Style: {self.musical_style}")


class Performance:
    def __init__(self, artist, start_time, end_time):
        self.artist = artist
        self.start_time = start_time
        self.end_time = end_time

    def display_info(self):
        print("Performance Details:")
        self.artist.display_info()
        print(f"Start Time: {self.start_time}")
        print(f"End Time: {self.end_time}")


class Stage:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity
        self.performances = []

    def add_performance(self, performance):
        self.performances.append(performance)

    def display_schedule(self):
        print(f"Stage: {self.name}")
        print(f"Capacity: {self.capacity}")
        print("Scheduled Performances:")
        for performance in self.performances:
            performance.display_info()
            print()



artist1 = Artist("Femi Kuti", "Nigeria", "Afrobeat")
artist2 = Artist("Salif Keita", "Mali", "Mande music")

performance1 = Performance(artist1, "18:00", "20:00")
performance2 = Performance(artist2, "20:30", "22:30")


stage = Stage("Main Stage", 5000)


stage.add_performance(performance1)
stage.add_performance(performance2)


stage.display_schedule()


# 5. Create a class called Product with attributes for name, price, and quantity.
# Implement a method to calculate the total value of the product (price * quantity).
# Create multiple objects of the Product class and calculate their total values.

class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def calculate_total_value(self):
        return self.price * self.quantity


product1 = Product("Item 1", 10.99, 5)
product2 = Product("Item 2", 5.99, 10)
product3 = Product("Item 3", 8.50, 2)


total_value1 = product1.calculate_total_value()
total_value2 = product2.calculate_total_value()
total_value3 = product3.calculate_total_value()


print(f"Total value of {product1.name}: {total_value1}")
print(f"Total value of {product2.name}: {total_value2}")
print(f"Total value of {product3.name}: {total_value3}")


# 6. Implement a class called Student with attributes for name, age, and grades (a
# list of integers). Include methods to calculate the average grade, display the
# student information, and determine if the student has passed (average grade >=
# 60). Create objects for the Student class and demonstrate the usage of these
# methods.

class Student:
    def __init__(self, name, age, grades):
        self.name = name
        self.age = age
        self.grades = grades

    def calculate_average_grade(self):
        total_grades = sum(self.grades)
        average_grade = total_grades / len(self.grades)
        return average_grade

    def display_student_info(self):
        print("Student Information:")
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Grades: {self.grades}")

    def has_passed(self):
        average_grade = self.calculate_average_grade()
        return average_grade >= 60



student = Student("John Doe", 18, [80, 75, 90, 65, 70])


student.display_student_info()


average_grade = student.calculate_average_grade()
print(f"Average Grade: {average_grade}")


if student.has_passed():
    print("Status: Passed")
else:
    print("Status: Failed")
    
    
# 7. Create a FlightBooking class that represents a flight booking system. Implement
# methods to search for available flights based on destination and date, reserve
# seats for customers, manage passenger information, and generate booking
# confirmations.   

class FlightBooking:
    def __init__(self):
        self.flights = []

    def add_flight(self, flight):
        self.flights.append(flight)

    def search_flights(self, destination, date):
        available_flights = []
        for flight in self.flights:
            if flight.destination == destination and flight.date == date and flight.is_available():
                available_flights.append(flight)
        return available_flights

    def reserve_seat(self, flight, passenger):
        if flight.is_available() and flight.has_available_seats():
            flight.reserve_seat(passenger)
            return True
        return False

    def generate_booking_confirmation(self, flight, passenger):
        if flight.is_passenger_reserved(passenger):
            confirmation = f"Booking Confirmation:\nFlight: {flight}\nPassenger: {passenger}"
            return confirmation
        return None


class Flight:
    def __init__(self, flight_number, destination, date, seats):
        self.flight_number = flight_number
        self.destination = destination
        self.date = date
        self.seats = seats
        self.passenger_list = []

    def is_available(self):
        return len(self.passenger_list) < self.seats

    def has_available_seats(self):
        return len(self.passenger_list) < self.seats

    def reserve_seat(self, passenger):
        self.passenger_list.append(passenger)

    def is_passenger_reserved(self, passenger):
        return passenger in self.passenger_list


booking_system = FlightBooking()


flight1 = Flight("F001", "New York", "2023-07-15", 100)
flight2 = Flight("F002", "London", "2023-07-20", 150)
flight3 = Flight("F003", "Paris", "2023-07-25", 200)

booking_system.add_flight(flight1)
booking_system.add_flight(flight2)
booking_system.add_flight(flight3)


available_flights = booking_system.search_flights("London", "2023-07-20")
print("Available Flights:")
for flight in available_flights:
    print(flight.flight_number, flight.destination, flight.date)


passenger1 = "John Doe"
reserved = booking_system.reserve_seat(flight2, passenger1)
if reserved:
    print(f"Seat reserved for {passenger1} on Flight {flight2.flight_number}")


confirmation = booking_system.generate_booking_confirmation(flight2, passenger1)
if confirmation:
    print(confirmation)
    

# 8. Create a LibraryCatalog class that handles the cataloging and management of
# books in a library. Implement methods to add new books, search for books by
# title or author, keep track of available copies, and display book details.   


class Book:
    def __init__(self, title, author, num_copies):
        self.title = title
        self.author = author
        self.num_copies = num_copies

    def __str__(self):
        return f"{self.title} by {self.author}"

class LibraryCatalog:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def search_by_title(self, title):
        matching_books = []
        for book in self.books:
            if book.title.lower() == title.lower():
                matching_books.append(book)
        return matching_books

    def search_by_author(self, author):
        matching_books = []
        for book in self.books:
            if book.author.lower() == author.lower():
                matching_books.append(book)
        return matching_books

    def display_book_details(self, book):
        print(f"Title: {book.title}")
        print(f"Author: {book.author}")
        print(f"Available Copies: {book.num_copies}")

    def borrow_book(self, book):
        if book.num_copies > 0:
            book.num_copies -= 1
            return True
        return False

    def return_book(self, book):
        book.num_copies += 1



catalog = LibraryCatalog()


book1 = Book("Python Crash Course", "Eric Matthes", 3)
book2 = Book("Clean Code", "Robert C. Martin", 5)
book3 = Book("The Great Gatsby", "F. Scott Fitzgerald", 2)
catalog.add_book(book1)
catalog.add_book(book2)
catalog.add_book(book3)


title_search_results = catalog.search_by_title("python crash course")
author_search_results = catalog.search_by_author("Robert C. Martin")

print("Search Results by Title:")
for book in title_search_results:
    catalog.display_book_details(book)

print("\nSearch Results by Author:")
for book in author_search_results:
    catalog.display_book_details(book)


borrowed = catalog.borrow_book(book1)
if borrowed:
    print(f"\nBook {book1.title} borrowed successfully.")


catalog.return_book(book1)
print(f"\nBook {book1.title} returned.")


print("\nUpdated Book Details:")
catalog.display_book_details(book1)



