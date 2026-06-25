from __future__ import annotations
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Dict, List


class TransactionType(str, Enum):
    """Supported actions in the library."""

    BORROW = "borrow"
    RETURN = "return"


@dataclass
class Book:
    """Represents one book in the catalog."""

    title: str
    author: str
    isbn: str
    is_available: bool = True
    borrowed_by: str = ""

    def info(self) -> str:
        status = "Available" if self.is_available else f"Borrowed by {self.borrowed_by}"
        return f"{self.title} | {self.author} | ISBN: {self.isbn} | {status}"


@dataclass
class Member:
    """Represents a library member."""

    name: str
    email: str
    borrowed_books: List[str] = field(default_factory=list)

    def info(self) -> str:
        return f"{self.name} | {self.email} | Borrowed books: {len(self.borrowed_books)}"


@dataclass
class Transaction:
    """Stores a simple history record."""

    action: TransactionType
    isbn: str
    member_email: str
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat(timespec="seconds"))

    def info(self) -> str:
        return f"{self.timestamp} | {self.action.value.title()} | ISBN: {self.isbn} | Member: {self.member_email}"


class Library:
    """Holds books, members, and the rules for borrowing and returning."""

    def __init__(self) -> None:
        self.books: Dict[str, Book] = {}
        self.members: Dict[str, Member] = {}
        self.transactions: List[Transaction] = []

    def add_book(self, book: Book) -> None:
        if book.isbn in self.books:
            raise ValueError(f"Book with ISBN '{book.isbn}' already exists.")
        self.books[book.isbn] = book

    def add_member(self, member: Member) -> None:
        if member.email in self.members:
            raise ValueError(f"Member '{member.email}' already exists.")
        self.members[member.email] = member

    def borrow_book(self, isbn: str, member_email: str) -> None:
        book = self._get_book(isbn)
        member = self._get_member(member_email)

        if not book.is_available:
            raise ValueError(f"Book '{book.title}' is already borrowed.")

        book.is_available = False
        book.borrowed_by = member.email
        member.borrowed_books.append(isbn)
        self.transactions.append(Transaction(TransactionType.BORROW, isbn, member.email))

    def return_book(self, isbn: str, member_email: str) -> None:
        book = self._get_book(isbn)
        member = self._get_member(member_email)

        if isbn not in member.borrowed_books:
            raise ValueError(f"Member '{member_email}' does not have book '{isbn}'.")

        book.is_available = True
        book.borrowed_by = ""
        member.borrowed_books.remove(isbn)
        self.transactions.append(Transaction(TransactionType.RETURN, isbn, member.email))

    def search_books(self, query: str) -> List[Book]:
        query = query.casefold()
        return [
            book
            for book in self.books.values()
            if query in book.title.casefold() or query in book.author.casefold() or query in book.isbn.casefold()
        ]

    def list_books(self) -> List[Book]:
        return list(self.books.values())

    def list_members(self) -> List[Member]:
        return list(self.members.values())

    def list_transactions(self) -> List[Transaction]:
        return list(self.transactions)

    def _get_book(self, isbn: str) -> Book:
        if isbn not in self.books:
            raise ValueError(f"Book '{isbn}' not found.")
        return self.books[isbn]

    def _get_member(self, email: str) -> Member:
        if email not in self.members:
            raise ValueError(f"Member '{email}' not found.")
        return self.members[email]


def print_books(books: List[Book]) -> None:
    """Print a list of books in a readable format."""

    if not books:
        print("No books found.")
        return
    for book in books:
        print(book.info())


def print_transactions(transactions: List[Transaction]) -> None:
    """Print transaction history."""

    if not transactions:
        print("No transactions yet.")
        return
    for transaction in transactions:
        print(transaction.info())


def main() -> None:
    """Small command-line menu for manual testing."""

    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add book")
        print("2. Add member")
        print("3. Borrow book")
        print("4. Return book")
        print("5. Search books")
        print("6. List books")
        print("7. List members")
        print("8. View transactions")
        print("9. Exit")

        choice = input("Choose an option: ").strip()

        try:
            if choice == "1":
                title = input("Book title: ").strip()
                author = input("Book author: ").strip()
                isbn = input("Book ISBN: ").strip()
                library.add_book(Book(title, author, isbn))
                print("Book added.")
            elif choice == "2":
                name = input("Member name: ").strip()
                email = input("Member email: ").strip()
                library.add_member(Member(name, email))
                print("Member added.")
            elif choice == "3":
                isbn = input("Book ISBN: ").strip()
                email = input("Member email: ").strip()
                library.borrow_book(isbn, email)
                print("Book borrowed.")
            elif choice == "4":
                isbn = input("Book ISBN: ").strip()
                email = input("Member email: ").strip()
                library.return_book(isbn, email)
                print("Book returned.")
            elif choice == "5":
                query = input("Search query: ").strip()
                print_books(library.search_books(query))
            elif choice == "6":
                print_books(library.list_books())
            elif choice == "7":
                members = library.list_members()
                if not members:
                    print("No members found.")
                else:
                    for member in members:
                        print(member.info())
            elif choice == "8":
                print_transactions(library.list_transactions())
            elif choice == "9":
                print("Goodbye.")
                break
            else:
                print("Invalid option.")
        except ValueError as error:
            print(f"Error: {error}")


if __name__ == "__main__":
    main()
