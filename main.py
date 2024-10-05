from AddBook import add_book
from ViewBooks import view_books
from DeleteBook import delete_book
from BorrowedBook import borrow_book
from ReturnBook import return_book


def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main_menu()


# alternative
class BookNode:
    def __init__(self, bid, title, author, status='0'):
        self.bid = bid
        self.title = title
        self.author = author
        self.status = status  # '0' for available, '1' for issued
        self.next = None


class BookList:
    head = None

    @staticmethod
    def add_book(book):
        if BookList.head is None:
            BookList.head = book
        else:
            current = BookList.head
            while current.next:
                current = current.next
            current.next = book

    @staticmethod
    def delete_book(bid):
        current = BookList.head
        prev = None

        while current:
            if current.bid == bid:
                if prev:
                    prev.next = current.next
                else:
                    BookList.head = current.next
                return True
            prev = current
            current = current.next
        return False

    @staticmethod
    def borrow_book(bid):
        current = BookList.head
        while current:
            if current.bid == bid and current.status == '0':
                current.status = '1'  # Book is issued
                return True
            current = current.next
        return False

    @staticmethod
    def return_book(bid):
        current = BookList.head
        while current:
            if current.bid == bid and current.status == '1':
                current.status = '0'  # Book is available
                return True
            current = current.next
        return False


def add_book():
    bid = input("Enter Book ID: ")
    title = input("Enter Book Title: ")
    author = input("Enter Book Author: ")
    status = '0'  # Default status: available
    new_book = BookNode(bid, title, author, status)
    BookList.add_book(new_book)
    print("Book added successfully!")


def view_books():
    if BookList.head is None:
        print("No books in the library.")
    else:
        current = BookList.head
        print("Book ID | Title | Author | Status")
        while current:
            print(f"{current.bid} | {current.title} | {current.author} | {current.status}")
            current = current.next


def delete_book():
    bid = input("Enter the Book ID to delete: ")
    if BookList.delete_book(bid):
        print(f"Book with ID {bid} has been deleted.")
    else:
        print(f"No book found with ID {bid}.")


def borrow_book():
    bid = input("Enter the Book ID to borrow: ")
    if BookList.borrow_book(bid):
        print(f"Book with ID {bid} has been borrowed.")
    else:
        print(f"Book with ID {bid} is not available or doesn't exist.")


def return_book():
    bid = input("Enter the Book ID to return: ")
    if BookList.return_book(bid):
        print(f"Book with ID {bid} has been returned and is now available.")
    else:
        print(f"Book with ID {bid} was not found in the borrowed list.")


def main_menu():
    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. View Books")
        print("3. Delete Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            delete_book()
        elif choice == '4':
            borrow_book()
        elif choice == '5':
            return_book()
        elif choice == '6':
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")


if __name__ == "__main__":
    main_menu()
