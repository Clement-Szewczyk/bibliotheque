import json
from app.data.book import Book

class FileManager:

    def __init__(self, book_tab=None):
        #print("FileManager initialized")
        self.pathfile = "./data.json"
        self.books = []
        self.load_books()
        self.book_tab = book_tab

    def get_next_id(self):
        """Generate the next available ID"""
        if not self.books:
            return 1
        
        # Find the maximum existing ID
        max_id = max(book.id for book in self.books if book.id is not None)
        return max_id + 1

    def assign_missing_ids(self):
        """Assign IDs to books that don't have one (for backward compatibility)"""
        next_id = 1
        existing_ids = {book.id for book in self.books if book.id is not None}
        
        for book in self.books:
            if book.id is None:
                # Find next available ID
                while next_id in existing_ids:
                    next_id += 1
                book.id = next_id
                existing_ids.add(next_id)
                next_id += 1

    def load_books(self):
        try:
            with open(self.pathfile, "r") as f:
                books_data = json.load(f)
            # Convert dictionaries to Book objects
            self.books = [Book.from_dict(book_data) for book_data in books_data]
            
            # Assign IDs to books that don't have one (backward compatibility)
            self.assign_missing_ids()
            
            # Save if any IDs were assigned
            if any(book.id is not None for book in self.books):
                self.save_books()
                
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            self.books = []
        return [book.to_dict() for book in self.books]  # Return as dicts for UI compatibility
    
    def load_book_id(self, book_id):
        for book in self.books:
            if book.id == book_id:
                return book.to_dict()
        return None
    
    def save_books(self):
        # Convert Book objects to dictionaries before saving
        books_data = [book.to_dict() for book in self.books]
        with open(self.pathfile, "w") as f:
            json.dump(books_data, f, indent=4)

    def add_book(self, title, author, genre, year, isbn, sale):
        #print(f"Book added: {title}, {author}, {year}, {isbn}, Read: {read}")
        # Create book with auto-incremented ID
        book = Book(title, author, genre, year, isbn, sale)
        book.id = self.get_next_id()
        
        self.books.append(book)
        self.save_books()
        if self.book_tab:
            self.book_tab.load_books()

    def remove_book(self, book_id):
        """Remove a book by its ID"""
        self.books = [book for book in self.books if book.id != book_id]
        self.save_books()
        if self.book_tab:
            self.book_tab.load_books()

    def modify_book(self, book_id, title, author, genre, year, isbn, sale):
        for book in self.books : 
            if book_id == book.id:
                book.title = title
                book.author = author
                book.genre = genre
                book.year = year
                book.isbn = isbn
                book.sale = sale

                self.save_books()
                return
            else : 
                return "Pas de livre correspondant"


