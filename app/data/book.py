class Book:

    def __init__(self, title: str, author: str, year: int, genre: str, isbn: str, sale: bool, id: int = None):
        self.id = id  # Will be set automatically by FileManager
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.isbn = isbn
        self.sale = sale

    def to_dict(self):
        """Convert Book object to dictionary for JSON serialization"""
        book_dict = {
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "year": self.year,
            "isbn": self.isbn,
            "sale": self.sale
        }
        # Include ID only if it's set
        if self.id is not None:
            book_dict["id"] = self.id
        return book_dict

    @classmethod
    def from_dict(cls, data):
        """Create Book object from dictionary"""
        return cls(
            id=data.get("id"),
            title=data.get("title", ""),
            author=data.get("author", ""),
            genre=data.get("genre", ""),
            year=data.get("year", ""),
            isbn=data.get("isbn", ""),
            sale=data.get("sale", False)
        )

    def __repr__(self):
        return f"Book(id={self.id}, title={self.title}, author={self.author}, year={self.year}, genre={self.genre}, isbn={self.isbn}, sale={self.sale})"