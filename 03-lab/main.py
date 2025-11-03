from Book import Book
from Library import Library

def main():
  library = Library()

  # Dodanie kilku książek do biblioteki
  if len(library.books) == 0:
    print("Adding sample books to the library...")
    library.add_book(Book("The Great Gatsby", "F. Scott Fitzgerald", 1925))
    library.add_book(Book("1984", "George Orwell", 1949))
    library.add_book(Book("To Kill a Mockingbird", "Harper Lee", 1960))
  else:
     print(f"Welcome back! Loaded {len(library.books)} books from the library.")

  while True:
    print("Library Menu:")
    print("1. List all books")
    print("2. Add a new book")
    print("3. Borrow a book")
    print("4. Return a book")
    print("5. Exit")

    choice = input("Choose an option (1-5): ")

    if choice == '1':
      library.list_books()

    
    elif choice == '2':
      title = input("Enter book title: ")
      author = input("Enter book author: ")
      year = input("Enter publication year: ")
      try:
        year = int(year)
        library.add_book(Book(title, author, year))
      except ValueError:
        print("Invalid year. Please enter a number.")
      
    elif choice == '3':
        title = input("Enter the title of the book to borrow: ")
        library.borrow_book(title)
      
    elif choice == '4':
        title = input("Enter the title of the book to return: ")
        library.return_book(title)
      
    elif choice == '5':
        print("Exiting the library system. Goodbye!")
        break
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
  main()