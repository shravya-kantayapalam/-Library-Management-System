# library_management.py

class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def __str__(self):
        status = "Available" if self.available else "Checked Out"
        return f"ID: {self.book_id}, Title: {self.title}, Author: {self.author}, Status: {status}"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_id, title, author):
        for book in self.books:
            if book.book_id == book_id:
                print("Book ID already exists.")
                return
        self.books.append(Book(book_id, title, author))
        print(f"Book '{title}' added successfully.")

    def remove_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                self.books.remove(book)
                print(f"Book '{book.title}' removed successfully.")
                return
        print("Book not found.")

    def search_book(self, keyword):
        found = False
        for book in self.books:
            if keyword.lower() in book.title.lower() or keyword.lower() in book.author.lower():
                print(book)
                found = True
        if not found:
            print("No books found matching the keyword.")

    def list_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            for book in self.books:
                print(book)

    def check_out(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if book.available:
                    book.available = False
                    print(f"You have checked out '{book.title}'.")
                else:
                    print("Book already checked out.")
                return
        print("Book not found.")

    def check_in(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                if not book.available:
                    book.available = True
                    print(f"You have returned '{book.title}'.")
                else:
                    print("Book was not checked out.")
                return
        print("Book not found.")

def main():
    library = Library()
    while True:
        print("\n--- Library Management System ---")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Search Book")
        print("4. List All Books")
        print("5. Check Out Book")
        print("6. Check In Book")
        print("7. Exit")
        choice = input("Enter your choice (1-7): ")

        if choice == '1':
            book_id = input("Enter Book ID: ")
            title = input("Enter Book Title: ")
            author = input("Enter Author: ")
            library.add_book(book_id, title, author)
        elif choice == '2':
            book_id = input("Enter Book ID to remove: ")
            library.remove_book(book_id)
        elif choice == '3':
            keyword = input("Enter title or author to search: ")
            library.search_book(keyword)
        elif choice == '4':
            library.list_books()
        elif choice == '5':
            book_id = input("Enter Book ID to check out: ")
            library.check_out(book_id)
        elif choice == '6':
            book_id = input("Enter Book ID to check in: ")
            library.check_in(book_id)
        elif choice == '7':
            print("Exiting Library Management System. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
