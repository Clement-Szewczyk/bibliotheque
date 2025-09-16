import json

class FileManager:

    def __init__(self):
        #print("FileManager initialized")
        self.pathfile = "./data.json"
        self.load_books()

    def load_books(self):
        try:
            with open(self.pathfile, "r") as f:
                self.books = json.load(f)
        except FileNotFoundError:
            self.books = []
        except json.JSONDecodeError:
            self.books = []
    
    def save_books(self):
        with open(self.pathfile, "w") as f:
            json.dump(self.books, f, indent=4)

    def add_book(self, title, author, year, isbn, read):
        #print(f"Book added: {title}, {author}, {year}, {isbn}, Read: {read}")
        new_book = {
            "title": title,
            "author": author,
            "year": year,
            "isbn": isbn,
            "read": read
        }
        self.books.append(new_book)
        self.save_books()


