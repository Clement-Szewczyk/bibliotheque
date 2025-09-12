import time
from PyQt6.QtWidgets import QSplashScreen
from PyQt6.QtGui import QPixmap
from PyQt6.QtCore import Qt

class Splash(QSplashScreen):
    def __init__(self):
        pixmap = QPixmap(400, 300)
        pixmap.fill(Qt.GlobalColor.white)
        super().__init__(pixmap)

        self.showMessage("Démarrage...",
                         Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter,
                         Qt.GlobalColor.black)

    def load_app(self, app):
        """Simule un chargement"""
        for i in range(1, 6):
            time.sleep(0.5)
            self.showMessage(f"Chargement... {i*20}%",
                             Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter,
                             Qt.GlobalColor.black)
            app.processEvents()
