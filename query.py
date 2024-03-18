from movies import Movies

def main():
    movies = Movies('./movies.txt')
    
    while True:
        print("\nMENU:")
        print("1. List all movie names")
        print("2. Search movies by title")
        print("q. Quit")
        
        choice = input("Enter your choice: ").lower()
        
        if choice == '1':
            list_all_movies(movies)
        elif choice == '2':
            search_movies_by_title(movies)
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def list_all_movies(movies):
    print("\nAll Movie Names:")
    for idx, movie in enumerate(movies._movies, start=1):
        print(f"{idx}. {movie['name']}")

def search_movies_by_title(movies):
    partial_title = input("Enter partial title to search: ").lower()
    found_movies = []

    for movie in movies._movies:
        if partial_title in movie['name'].lower():
            found_movies.append(movie['name'])

    if found_movies:
        print("\nMovies Found:")
        for movie in found_movies:
            print(movie)
    else:
        print("No movies found with the provided partial title.")

if __name__ == "__main__":
    main()
