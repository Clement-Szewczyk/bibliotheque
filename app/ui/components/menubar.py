# Menubar

from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

from app.service.addBook import AddBookDialog
from app.ui.window.setting import SettingsWindow

class Menubar(QMenuBar):

    def __init__(self, book_tab=None, parent=None):
        super().__init__(parent)
        self.book_tab = book_tab

        save = QAction("save", self)
        save.setShortcut("Ctrl+S")
        self.addAction(save)
        self.save = save

        add = QAction("add", self)
        add.setShortcut("Ctrl+N")
        self.addAction(add)
        self.add = add
        self.add.triggered.connect(self.addBook)

        settings = QAction("settings", self)
        settings.setShortcut("Ctrl+P")
        self.addAction(settings)
        self.settings = settings
        self.settings.triggered.connect(self.open_settings)

    def addBook(self):
        dialog = AddBookDialog(self.book_tab)
        dialog.exec()

    def open_settings(self):
        settings_window = SettingsWindow()
        settings_window.exec()

