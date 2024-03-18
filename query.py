from movies import Movies

def main():
    movies = Movies('./movies.txt')
    
    while True:
        print("\nMENU:")
        print("q. Quit")
        
        choice = input("Enter your choice: ").lower()
        
        if choice == 'q':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
