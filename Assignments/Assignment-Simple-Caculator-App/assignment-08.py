import json
import os
from datetime import datetime, timedelta

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_borrowed = False
        self.due_date = None

    def __str__(self):
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"

class Library:
    def __init__(self):
        self.books = []
        self.data_file = "library_data.json"
        self.load_data()

    def add_book(self, book):
        self.books.append(book)
        print(f"Added: {book}")
        self.save_data()

    def remove_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                self.books.remove(book)
                print(f"Removed: {book}")
                self.save_data()
                return
        print("Book not found.")

    def borrow_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if not book.is_borrowed:
                    book.is_borrowed = True
                    book.due_date = datetime.now() + timedelta(days=14)
                    print(f"Borrowed: {book}")
                    print(f"Due date: {book.due_date.strftime('%Y-%m-%d')}")
                    self.save_data()
                    return
                else:
                    print("Book is already borrowed.")
                    return
        print("Book not found.")

    def return_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                if book.is_borrowed:
                    book.is_borrowed = False
                    book.due_date = None
                    print(f"Returned: {book}")
                    self.save_data()
                    return
                else:
                    print("Book is not borrowed.")
                    return
        print("Book not found.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                status = "Available" if not book.is_borrowed else f"Borrowed (Due: {book.due_date.strftime('%Y-%m-%d')})"
                print(f"{book} - {status}")

    def save_data(self):
        data = []
        for book in self.books:
            book_data = {
                "title": book.title,
                "author": book.author,
                "isbn": book.isbn,
                "is_borrowed": book.is_borrowed,
                "due_date": book.due_date.isoformat() if book.due_date else None
            }
            data.append(book_data)
        
        with open(self.data_file, "w") as f:
            json.dump(data, f)

    def load_data(self):
        if os.path.exists(self.data_file):
            with open(self.data_file, "r") as f:
                data = json.load(f)
            
            for book_data in data:
                book = Book(book_data["title"], book_data["author"], book_data["isbn"])
                book.is_borrowed = book_data["is_borrowed"]
                book.due_date = datetime.fromisoformat(book_data["due_date"]) if book_data["due_date"] else None
                self.books.append(book)

def main():
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Borrow a book")
        print("4. Return a book")
        print("5. List all books")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            isbn = input("Enter book ISBN: ")
            library.add_book(Book(title, author, isbn))
        elif choice == "2":
            isbn = input("Enter book ISBN to remove: ")
            library.remove_book(isbn)
        elif choice == "3":
            isbn = input("Enter book ISBN to borrow: ")
            library.borrow_book(isbn)
        elif choice == "4":
            isbn = input("Enter book ISBN to return: ")
            library.return_book(isbn)
        elif choice == "5":
            library.list_books()
        elif choice == "6":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()