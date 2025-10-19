from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox,QDialog

from app.service.fileManager import FileManager

class ModifyBook(QDialog):

    def __init__(self, id, booktab=None):
        super().__init__()
        self.id = id
        self.booktable = booktab
        self.file_manager = FileManager(book_tab=self.booktable)
        self.book_data = self.file_manager.load_book_id(self.id)
        
        #print(f"ModifyBook initialized for book ID: {self.id} with data: {self.book_data}")
        
        #UI
        self.setWindowTitle("Modifier le livre")
        self.layout = QVBoxLayout()
        self.label_title = QLabel("Titre:")
        self.input_title = QLineEdit()
        self.input_title.setText(self.book_data.get('title', ''))
        self.label_author = QLabel("Auteur:")
        self.input_author = QLineEdit()
        self.input_author.setText(self.book_data.get('author', ''))
        self.label_genre = QLabel("Genre:")
        self.input_genre = QLineEdit()
        self.input_genre.setText(self.book_data.get('genre', ''))
        self.label_year = QLabel("Année de publication:")
        self.input_year = QLineEdit()
        self.input_year.setText(str(self.book_data.get('year', '')))
        self.label_isbn = QLabel("ISBN:")
        self.input_isbn = QLineEdit()
        self.input_isbn.setText(self.book_data.get('isbn', ''))
        self.label_sale = QLabel("En Vente (oui/non):")
        self.input_sale = QCheckBox()
        self.input_sale.setChecked(self.book_data.get('sale', False))
        self.button_modify = QPushButton("Modifier")
        
        self.setLayout(self.layout)
        self.layout.addWidget(self.label_title)
        self.layout.addWidget(self.input_title)
        self.layout.addWidget(self.label_author)
        self.layout.addWidget(self.input_author)
        self.layout.addWidget(self.label_genre)
        self.layout.addWidget(self.input_genre)
        self.layout.addWidget(self.label_year)
        self.layout.addWidget(self.input_year)
        self.layout.addWidget(self.label_isbn)
        self.layout.addWidget(self.input_isbn)
        self.layout.addWidget(self.label_sale)
        self.layout.addWidget(self.input_sale)
        self.layout.addWidget(self.button_modify)
        self.button_modify.clicked.connect(self.call_file)



    def call_file(self):
        print("Call")
        title = self.input_title.text()
        author = self.input_author.text()
        genre = self.input_genre.text()
        year = self.input_year.text()
        isbn = self.input_isbn.text()
        sale = self.input_sale.isChecked()
        if title == "" or author == "" or genre == "" or year == "" or isbn == "":
            QMessageBox.warning(self.window, "Erreur", "Veuillez remplir tous les champs")
        else:
            #modifier le livre a la base de donnee
            self.file_manager.modify_book(self.id, title, author, genre, year, isbn, sale)
            #Fermer la fenetre
            self.accept()
    
        
        


 
