from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QStackedWidget, QLabel, QPushButton, QTabWidget, QStyleFactory)
from PyQt6.QtGui import QGuiApplication

from app.ui.components.menubar import Menubar
from app.ui.components.navigationBar import NavigationBar
from app.ui.components.booktab import BookTab
import config



class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{config.APP_NAME}")
        #Taille max de l'écran
        screen = QGuiApplication.primaryScreen().geometry()
        self.resize(screen.width(), screen.height())
        self.setMinimumSize(800, 600)  # Taille minimale
        
        # Centrer la fenêtre sur l'écran
        self.center_window()
        
        # Widget central avec onglets
        self.tab_widget = QTabWidget()
        self.setCentralWidget(self.tab_widget)
        
        # Onglet des livres (une seule instance)
        self.book_tab = BookTab()
        self.tab_widget.addTab(self.book_tab, "Livres")

        # Menubar avec référence au book_tab
        self.menubar = Menubar(self.book_tab, self)
        self.setMenuBar(self.menubar)
    
    def center_window(self):
        """Centre la fenêtre sur l'écran"""
        screen = QGuiApplication.primaryScreen().geometry()
        window = self.geometry()
        x = (screen.width() - window.width()) // 2
        y = (screen.height() - window.height()) // 2
        self.move(x, y)

