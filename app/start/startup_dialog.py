from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton
from app.ui.window.setting import SettingsWindow

class StartupDialog(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Bienvenue")
        self.resize(300, 150)

        layout = QVBoxLayout()

        Start_button = QPushButton("Démarrer")
        Settings_button = QPushButton("Paramètres")
        Exit_button = QPushButton("Quitter")
        layout.addWidget(Start_button)
        layout.addWidget(Settings_button)
        layout.addWidget(Exit_button)

        self.setLayout(layout)
    
        # Connect button signals
        Start_button.clicked.connect(self.start_app)
        Settings_button.clicked.connect(self.open_settings)
        Exit_button.clicked.connect(self.exit_app)

    def start_app(self):
        self.accept()  # Ferme le dialog avec un code de succès

    def open_settings(self):
        settings_window = SettingsWindow()
        settings_window.exec()

    def exit_app(self):
       # ferme le dialogue sans lancer l'application principale
        self.reject()
    
        