from PyQt6.QtWidgets import QLabel

class NavigationBar:

    def __init__(self):
        super().__init__()
        self.welcome_label = QLabel("Navigation Bar")
        self.welcome_label.setStyleSheet("font-size: 16px; font-weight: bold; padding: 10px;")