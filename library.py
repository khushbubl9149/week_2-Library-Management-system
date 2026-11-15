
import json
import os


# Custom Exceptions
class BookNotAvailableError(Exception):
    pass


class BookNotFoundError(Exception):
    pass


class MemberNotFoundError(Exception):
    pass


# Book Class
class Book:
    def __init__(self, book_id, title, author, available=True):
        self.book_id = book_id
        self.title = title
        self.author = author
        self.available = available

    def display(self):
        status = "Available" if self.available else "Issued"

        print(
            f"{self.book_id}. {self.title} "
            f"by {self.author} - {status}"
        )


# Parent Class
class Person:
    def __init__(self, member_id, name):
        self.member_id = member_id
        self.name = name

    def display(self):
        print(f"Member ID: {self.member_id}, Name: {self.name}")


# Child Class (Inheritance)
class Student(Person):
    def __init__(self, member_id, name, course):
        super().__init__(member_id, name)
        self.course = course

    def display(self):
        print(
            f"Student ID: {self.member_id}, "
            f"Name: {self.name}, Course: {self.course}"
        )


# Library Class
class Library:

    FILE_NAME = "library_data.json"

    def __init__(self):
        self.books = {}
        self.members = {}
        self.load_data()

    # Save data into JSON
    def save_data(self):
        data = {
            "books": [
                {
                    "book_id": book.book_id,
                    "title": book.title,
                    "author": book.author,
                    "available": book.available
                }
                for book in self.books.values()
            ],
            "members": [
                {
                    "member_id": member.member_id,
                    "name": member.name,
                    "course": member.course
                }
                for member in self.members.values()
            ]
        }

        with open(self.FILE_NAME, "w") as file:
            json.dump(data, file, indent=4)

    # Load data from JSON
    def load_data(self):
        if not os.path.exists(self.FILE_NAME):
            return

        try:
            with open(self.FILE_NAME, "r") as file:
                data = json.load(file)

            for item in data.get("books", []):
                book = Book(
                    item["book_id"],
                    item["title"],
                    item["author"],
                    item["available"]
                )
                self.books[book.book_id] = book

            for item in data.get("members", []):
                member = Student(
                    item["member_id"],
                    item["name"],
                    item["course"]
                )
                self.members[member.member_id] = member

        except (json.JSONDecodeError, KeyError, TypeError) as error:
            print("Could not load library data:", error)

    # Add a new book
    def add_book(self, book):
        if book.book_id in self.books:
            print("Book ID already exists!")
            return

        self.books[book.book_id] = book
        self.save_data()
        print("Book added successfully!")

    # Register a student
    def add_member(self, member):
        if member.member_id in self.members:
            print("Member ID already exists!")
            return

        self.members[member.member_id] = member
        self.save_data()
        print("Student registered successfully!")

    # Display all books
    def show_books(self):
        if not self.books:
            print("No books available.")
            return

        print("\n----- Library Books -----")

        for book in self.books.values():
            book.display()

    # Display all members
    def show_members(self):
        if not self.members:
            print("No members registered.")
            return

        print("\n----- Registered Members -----")

        for member in self.members.values():
            member.display()

    # Issue a book
    def issue_book(self, book_id, member_id):
        if book_id not in self.books:
            raise BookNotFoundError("Book not found!")

        if member_id not in self.members:
            raise MemberNotFoundError("Member not found!")

        book = self.books[book_id]

        if not book.available:
            raise BookNotAvailableError(
                "Sorry! This book is already issued."
            )

        book.available = False
        self.save_data()

        print("Book issued successfully!")

    # Return a book
    def return_book(self, book_id):
        if book_id not in self.books:
            raise BookNotFoundError("Book not found!")

        book = self.books[book_id]

        if book.available:
            raise BookNotAvailableError(
                "This book has not been issued."
            )

        book.available = True
        self.save_data()

        print("Book returned successfully!")


# Main Program
def main():

    library = Library()

    while True:

        print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
        print("1. Add Book")
        print("2. Register Student")
        print("3. Show All Books")
        print("4. Show All Members")
        print("5. Issue Book")
        print("6. Return Book")
        print("7. Exit")

        choice = input("\nEnter your choice: ").strip()

        try:

            if choice == "1":

                book_id = int(input("Enter Book ID: "))
                title = input("Enter Book Title: ").strip()
                author = input("Enter Author Name: ").strip()

                if not title or not author:
                    raise ValueError("Title and author cannot be empty.")

                book = Book(book_id, title, author)
                library.add_book(book)

            elif choice == "2":

                member_id = int(input("Enter Student ID: "))
                name = input("Enter Student Name: ").strip()
                course = input("Enter Course: ").strip()

                if not name or not course:
                    raise ValueError("Name and course cannot be empty.")

                student = Student(member_id, name, course)
                library.add_member(student)

            elif choice == "3":

                library.show_books()

            elif choice == "4":

                library.show_members()

            elif choice == "5":

                book_id = int(input("Enter Book ID: "))
                member_id = int(input("Enter Student ID: "))

                library.issue_book(book_id, member_id)

            elif choice == "6":

                book_id = int(input("Enter Book ID: "))

                library.return_book(book_id)

            elif choice == "7":

                print("Thank you for using the Library System!")
                break

            else:

                print("Invalid choice! Please select 1 to 7.")

        except ValueError as error:
            print("Invalid input:", error)

        except (
            BookNotFoundError,
            BookNotAvailableError,
            MemberNotFoundError
        ) as error:
            print("Error:", error)


if __name__ == "__main__":
    main()
