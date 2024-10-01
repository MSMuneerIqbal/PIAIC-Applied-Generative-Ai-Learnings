import json
import os
from datetime import datetime, timedelta

def create_book(title, author, isbn):
    return {
        "title": title,
        "author": author,
        "isbn": isbn,
        "is_borrowed": False,
        "due_date": None
    }

def add_book(library, title, author, isbn):
    book = create_book(title, author, isbn)
    library.append(book)
    print(f"Added: {book['title']} by {book['author']} (ISBN: {book['isbn']})")
    save_data(library)

def remove_book(library, isbn):
    for book in library:
        if book['isbn'] == isbn:
            library.remove(book)
            print(f"Removed: {book['title']} by {book['author']} (ISBN: {book['isbn']})")
            save_data(library)
            return
    print("Book not found.")

def borrow_book(library, isbn):
    for book in library:
        if book['isbn'] == isbn:
            if not book['is_borrowed']:
                book['is_borrowed'] = True
                book['due_date'] = (datetime.now() + timedelta(days=14)).isoformat()
                print(f"Borrowed: {book['title']} by {book['author']}")
                print(f"Due date: {datetime.fromisoformat(book['due_date']).strftime('%Y-%m-%d')}")
                save_data(library)
                return
            else:
                print("Book is already borrowed.")
                return
    print("Book not found.")

def return_book(library, isbn):
    for book in library:
        if book['isbn'] == isbn:
            if book['is_borrowed']:
                book['is_borrowed'] = False
                book['due_date'] = None
                print(f"Returned: {book['title']} by {book['author']}")
                save_data(library)
                return
            else:
                print("Book is not borrowed.")
                return
    print("Book not found.")

def list_books(library):
    if not library:
        print("No books in the library.")
    else:
        for book in library:
            status = "Available" if not book['is_borrowed'] else f"Borrowed (Due: {datetime.fromisoformat(book['due_date']).strftime('%Y-%m-%d')})"
            print(f"{book['title']} by {book['author']} (ISBN: {book['isbn']}) - {status}")

def save_data(library):
    with open("library_data.json", "w") as f:
        json.dump(library, f)

def load_data():
    if os.path.exists("library_data.json"):
        with open("library_data.json", "r") as f:
            return json.load(f)
    return []

def main():
    library = load_data()

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
            add_book(library, title, author, isbn)
        elif choice == "2":
            isbn = input("Enter book ISBN to remove: ")
            remove_book(library, isbn)
        elif choice == "3":
            isbn = input("Enter book ISBN to borrow: ")
            borrow_book(library, isbn)
        elif choice == "4":
            isbn = input("Enter book ISBN to return: ")
            return_book(library, isbn)
        elif choice == "5":
            list_books(library)
        elif choice == "6":
            print("Thank you for using the Library Management System.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
