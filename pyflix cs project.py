import pickle
import time

def save_to_file(movies, filename):
    with open(filename, 'wb') as file:
        pickle.dump(movies, file)

def load_from_file(filename):
    try:
        with open(filename, 'rb') as file:
            movies = pickle.load(file)
        return movies
    except FileNotFoundError:
        return []

def display_menu():
    print("1. 🎬 Add Movie")
    time.sleep(0.5)
    print("2. 🎥 View All Movies")
    time.sleep(0.5)
    print("3. 🔍 Search by Movie Name")
    time.sleep(0.5)
    print("4. ⭐ Search by Movie Rating")
    time.sleep(0.5)
    print("5. 🎭 Search by Movie Genre")
    time.sleep(0.5)
    print("6. 🚪 Exit")
    time.sleep(0.5)

def add_movie():
    time.sleep(0.5)
    title = input("Enter the movie title: ")
    time.sleep(0.5)
    genre = input("Enter the genre: ")
    time.sleep(0.5)
    rating = input("Enter the rating: ")
    time.sleep(0.5)
    rec = [title, genre, rating]

    with open("movie.dat", "ab") as f:
        pickle.dump(rec, f)

def view_all_movies():
    time.sleep(0.5)
    with open("movie.dat", "rb") as f:
        while True:
            try:
                movie = pickle.load(f)
                print(movie)
                time.sleep(0.5)
            except EOFError:
                print("File ends")
                break

def search_by_movie_name():
    time.sleep(0.5)
    name = input("Enter the movie name to search: ")
    time.sleep(0.5)
    found = False
    with open("movie.dat", "rb") as f:
        while True:
            try:
                movie = pickle.load(f)
                if name.lower() in movie[0].lower():
                    print(movie)
                    found = True
                    time.sleep(0.5)
            except EOFError:
                break
    if not found:
        print(f"No movies found with the name '{name}'.")

def search_by_rating():
    time.sleep(0.5)
    rating_input = input("Enter the movie rating to search: ")
    time.sleep(0.5)
    found = False
    with open("movie.dat", "rb") as f:
        while True:
            try:
                movie = pickle.load(f)
                if rating_input.lower() in movie[2].lower():
                    print(movie)
                    found = True
                    time.sleep(0.5)
            except EOFError:
                break
    if not found:
        print(f"No movies found with the rating '{rating_input}'.")

def search_by_genre():
    time.sleep(0.5)
    genre_input = input("Enter the movie genre to search: ")
    time.sleep(0.5)
    found = False
    with open("movie.dat", "rb") as f:
        while True:
            try:
                movie = pickle.load(f)
                if genre_input.lower() in movie[1].lower():
                    print(movie)
                    found = True
                    time.sleep(0.5)
            except EOFError:
                break
    if not found:
        print(f"No movies found with the genre '{genre_input}'.")

def main():
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ")

        if choice == '1':
            add_movie()
        elif choice == '2':
            view_all_movies()
        elif choice == '3':
            search_by_movie_name()
        elif choice == '4':
            search_by_rating()
        elif choice == '5':
            search_by_genre()
        elif choice == '6':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

if __name__ == "__main__":
    main()
