# Menubar

from PyQt6.QtWidgets import QMenuBar
from PyQt6.QtGui import QAction

from app.service.add import add

class Menubar(QMenuBar):

    def __init__(self, parent=None):
        super().__init__(parent)

        save = QAction("save", self)
        save.setShortcut("Ctrl+S")
        self.addAction(save)
        self.save = save

        add = QAction("add", self)
        add.setShortcut("Ctrl+N")
        self.addAction(add)
        self.add = add
        self.add.triggered.connect(self.additem)

    def additem(self):
        add()  # Call the add class from app/service/add.py

