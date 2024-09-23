class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.available = True

    def lend(self):
        if self.available:
            self.available = False
            return True
        return False

    def return_book(self):
        self.available = True

    def __str__(self):
        return f"'{self.title}' by {self.author} - {'Available' if self.available else 'Checked out'}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        new_book = Book(title, author)
        self.books.append(new_book)
        print(f"Added: {new_book}")

    def view_books(self):
        if not self.books:
            print("No books in the library.")
        else:
            print("Available Books:")
            for book in self.books:
                print(book)

    def lend_book(self, title):
        for book in self.books:
            if book.title == title:
                if book.lend():
                    print(f"You have borrowed: {book}")
                else:
                    print(f"Sorry, '{title}' is currently checked out.")
                return
        print(f"Book '{title}' not found in the library.")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.return_book()
                print(f"You have returned: {book}")
                return
        print(f"Book '{title}' not found in the library.")


# Example usage
if __name__ == "__main__":
    library = Library()

    # Adding books
    library.add_book("The Great Gatsby", "F. Scott Fitzgerald")
    library.add_book("To Kill a Mockingbird", "Harper Lee")
    library.add_book("1984", "George Orwell")

    # Viewing books
    library.view_books()

    # Lending a book
    library.lend_book("1984")
    library.lend_book("The Great Gatsby")

    # Viewing books after lending
    library.view_books()

    # Returning a book
    library.return_book("1984")

    # Final view of books
    library.view_books()
