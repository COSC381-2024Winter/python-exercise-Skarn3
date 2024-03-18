from movies import Movies

def main():
    movies = Movies('./movies.txt')
    
    while True:
        print("\nMENU:")
        print("1. List all movie names")
        print("q. Quit")
        
        choice = input("Enter your choice: ").lower()
        
        if choice == '1':
            list_all_movies(movies)
        elif choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def list_all_movies(movies):
    print("\nAll Movie Names:")
    for movie in movies._movies:
        print(movie['name'])

if __name__ == "__main__":
    main()
