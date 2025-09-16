from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton, QMessageBox, QCheckBox
from app.service.fileManager import FileManager

class add():
    
    def __init__(self):
        self.file_manager = FileManager()
        self.dialog = QDialog()
        self.dialog.setWindowTitle("Ajouter un livre")
        self.layout = QVBoxLayout()
        self.label_title = QLabel("Titre:")
        self.input_title = QLineEdit()
        self.label_author = QLabel("Auteur:")
        self.input_author = QLineEdit()
        self.label_year = QLabel("Année de publication:")
        self.input_year = QLineEdit()
        self.label_isbn = QLabel("ISBN:")
        self.input_isbn = QLineEdit()
        self.label_read = QLabel("Lu (oui/non):")
        self.input_read = QCheckBox() 
        
        self.button_add = QPushButton("Ajouter")
        self.dialog.setLayout(self.layout)
        self.layout.addWidget(self.label_title)
        self.layout.addWidget(self.input_title)
        self.layout.addWidget(self.label_author)
        self.layout.addWidget(self.input_author)
        self.layout.addWidget(self.label_year)
        self.layout.addWidget(self.input_year)
        self.layout.addWidget(self.label_isbn)
        self.layout.addWidget(self.input_isbn)
        self.layout.addWidget(self.label_read)
        self.layout.addWidget(self.input_read)
        self.layout.addWidget(self.button_add)
        self.button_add.clicked.connect(self.add_book)
        self.dialog.exec()

    def add_book(self):
        title = self.input_title.text()
        author = self.input_author.text()
        year = self.input_year.text()
        isbn = self.input_isbn.text()
        read = self.input_read.isChecked()
        if title == "" or author == "" or year == "" or isbn == "" or (read != True and read != False):
            QMessageBox.warning(self.dialog, "Erreur", "Veuillez remplir tous les champs")
        else:
            #ajouter le livre a la base de donnee
            self.file_manager.add_book(title, author, year, isbn, read)
            self.dialog.accept()


        
        