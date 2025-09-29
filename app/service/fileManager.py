import json

class FileManager:

    def __init__(self, book_tab=None):
        #print("FileManager initialized")
        self.pathfile = "./data.json"
        self.load_books()
        self.book_tab = book_tab

    def load_books(self):
        try:
            with open(self.pathfile, "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            self.books = []
        return self.books
    
    def save_books(self):
        with open(self.pathfile, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, title, author, genre, year, isbn, sale):
        #print(f"Book added: {title}, {author}, {year}, {isbn}, Read: {read}")
        new_book = {
            "title": title,
            "author": author,
            "genre": genre,
            "year": year,
            "isbn": isbn,
            "sale": sale
        }
        self.books.append(new_book)
        self.save_books()
        if self.book_tab:
            self.book_tab.load_books()



