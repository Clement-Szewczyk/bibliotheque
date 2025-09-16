from PyQt6.QtWidgets import QMainWindow

from app.ui.components.menubar import Menubar

import config



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{config.APP_NAME}")
        #taille ecran pc
        self.showMaximized()
        self.menubar = Menubar(self)
        self.setMenuBar(self.menubar)
  




        

    