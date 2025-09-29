from app.service.fileManager import FileManager
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QListWidget, QTableWidget, QPushButton, QHBoxLayout, QMessageBox, QTableWidgetItem)
from PyQt6.QtCore import Qt

class BookTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.file_manager = FileManager(book_tab=self)
        self.init_ui()
        self.load_books()

    def init_ui(self):
        self.layout = QVBoxLayout(self)

        # tab des livres
        self.bookTable = QTableWidget()
        self.layout.addWidget(self.bookTable)

        # Boutons
        button_layout = QHBoxLayout()
        
        self.add_button = QPushButton("Ajouter un livre")
        self.add_button.clicked.connect(self.file_manager.add_book)
        button_layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Supprimer le livre sélectionné")
        #self.remove_button.clicked.connect(self.file_manager.remove_book)
        button_layout.addWidget(self.remove_button)

        self.layout.addLayout(button_layout)

    def load_books(self):
        # Configuration des colonnes de la table
        books = self.file_manager.load_books()

        if not books:
            self.bookTable.setRowCount(0)
            self.bookTable.setColumnCount(6)
            self.bookTable.setHorizontalHeaderLabels(["Titre", "Auteur", "Genre", "Année", "ISBN", "En Vente"])
            return
        
        # Configuration de la table
        self.bookTable.setRowCount(len(books))
        self.bookTable.setColumnCount(6)
        self.bookTable.setHorizontalHeaderLabels(["Titre", "Auteur", "Genre", "Année", "ISBN", "En Vente"])
        
        # Remplissage des données
        for row, book in enumerate(books):
            self.bookTable.setItem(row, 0, QTableWidgetItem(book.get('title', '')))
            self.bookTable.setItem(row, 1, QTableWidgetItem(book.get('author', '')))
            self.bookTable.setItem(row, 2, QTableWidgetItem(book.get('genre', '')))
            self.bookTable.setItem(row, 3, QTableWidgetItem(str(book.get('year', ''))))
            self.bookTable.setItem(row, 4, QTableWidgetItem(book.get('isbn', '')))
            read_item = QTableWidgetItem("Oui" if book.get('sale', False) else "Non")
            read_item.setTextAlignment(Qt.AlignmentFlag.AlignCenter)
            self.bookTable.setItem(row, 5, read_item)

        # Ajustement automatique de la largeur des colonnes
        self.bookTable.resizeColumnsToContents()
        
    def refresh_table(self):
        """Force refresh the table data"""
        self.file_manager.load_books()  # Reload from file
        self.load_books()  # Update UI






