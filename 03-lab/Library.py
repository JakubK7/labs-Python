import json
from Book import Book
import os


class Library:
    def __init__(self, filename='data/library.json'):
        os.makedirs(os.path.dirname(filename) or '.', exist_ok=True)
        self.books = [] 
        self.filename = filename
        self.load_from_file() 

    def add_book(self, book):
        self.books.append(book)
        self.save_to_file()
        print(f"Book '{book.title}' added to the library.")
    
    def list_books(self):
        if not self.books:
            print("No books in the library")
            return
        print("\n---Books in the library:")
        for i, book in enumerate(self.books, 1):
            print(f"{i}. {book}")
        print("-------------------------\n")

    def borrow_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and book.is_available:
                if book.borrow_book():
                    self.save_to_file()
                    print(f"You have borrowed '{book.title}'.")
                    return
        print(f"Sorry, the book '{title}' is not available.")

    def return_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower() and not book.is_available:
                if book.return_book():
                    self.save_to_file()
                    print(f"You have returned '{book.title}'.")
                    return
        print(f"The book '{title}' was not borrowed from this library.")

    # Zapis do pliku JSON
    def save_to_file(self):
        data = []
        for book in self.books:
            data.append({
                'title': book.title,
                'author': book.author,
                'year': book.year,
                'is_available': book.is_available
            })
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(data, f, ensure_ascii=False, indent=4)
            print(f"Library data saved to {self.filename}.")
        except Exception as e:
            print(f"Error saving library data: {e}")

    # Wczytanie z pliku JSON
    def load_from_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
            self.books = []
            for item in data:
                book = Book(item['title'], item['author'], item['year'])
                book.is_available = item['is_available']
                self.books.append(book)
        except FileNotFoundError:
            pass
        except Exception as e:
            print(f"Error loading library data: {e}")