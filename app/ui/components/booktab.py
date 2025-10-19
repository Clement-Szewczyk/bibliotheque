from app.service.fileManager import FileManager
from PyQt6.QtWidgets import (QWidget, QVBoxLayout, QListWidget, QTableWidget, QPushButton, QHBoxLayout, QMessageBox, QTableWidgetItem)
from PyQt6.QtCore import Qt

from app.service.fileManager import FileManager
from app.service.modify_book import ModifyBook
from app.service.addBook import AddBookDialog

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
        self.add_button.clicked.connect(self.addBook)
        button_layout.addWidget(self.add_button)

        self.remove_button = QPushButton("Supprimer le livre sélectionné")
        self.remove_button.clicked.connect(self.addBook)
        button_layout.addWidget(self.remove_button)

        self.layout.addLayout(button_layout)

    def addBook(self):
        dialog = AddBookDialog(self)
        dialog.exec()

    def load_books(self):
        # Configuration des colonnes de la table
        books = self.file_manager.load_books()

        if not books:
            self.bookTable.setRowCount(0)
            self.bookTable.setColumnCount(8)  
            self.bookTable.setHorizontalHeaderLabels(["Titre", "Auteur", "Genre", "Année", "ISBN", "En Vente", "Modifier", "Supprimer"])
            return
        
        # Configuration de la table
        self.bookTable.setRowCount(len(books))
        self.bookTable.setColumnCount(8)  
        self.bookTable.setHorizontalHeaderLabels(["Titre", "Auteur", "Genre", "Année", "ISBN", "En Vente", "Modifier", "Supprimer"])

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

            # Add modify button
            modify_button = QPushButton("Modifier")
            modify_button.clicked.connect(lambda checked, book_id=book.get('id'): self.modify_book(book_id))
            self.bookTable.setCellWidget(row, 6, modify_button)

            # Add delete button
            delete_button = QPushButton("Supprimer")
            delete_button.clicked.connect(lambda checked, book_id=book.get('id'): self.delete_book(book_id))
            self.bookTable.setCellWidget(row, 7, delete_button)



        # Ajustement automatique de la largeur des colonnes
        self.bookTable.resizeColumnsToContents()

    def remove_selected_book(self):
        """Remove the selected book from the table"""
        current_row = self.bookTable.currentRow()
        if current_row >= 0:
            book_id_item = self.bookTable.item(current_row, 0)
            if book_id_item:
                book_id = int(book_id_item.text())
                self.delete_book(book_id)
        else:
            QMessageBox.warning(self, "Aucune sélection", "Veuillez sélectionner un livre à supprimer.")

    def delete_book(self, book_id):
        """Delete a book by its ID"""
        reply = QMessageBox.question(
            self, 
            "Confirmer la suppression", 
            f"Êtes-vous sûr de vouloir supprimer ce livre (ID: {book_id})?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            self.file_manager.remove_book(book_id)

    def modify_book(self, book_id):
        """Modify a book by its ID"""
        modify_window = ModifyBook(book_id, self)
        modify_window.exec()
        
    def refresh_table(self):
        """Force refresh the table data"""
        self.file_manager.load_books()  # Reload from file
        self.load_books()  # Update UI






