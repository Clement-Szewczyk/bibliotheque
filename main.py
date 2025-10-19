import sys
from PyQt6.QtWidgets import (QApplication, QStyleFactory)
from app.start.splash import Splash
from app.start.startup_dialog import StartupDialog
from app.ui.main_window import MainWindow

def main():
    StartConsole()
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    # Splash screen
    splash = Splash()
    splash.show()
    splash.load_app(app)

    # Dialog de démarrage
    dialog = StartupDialog()
    splash.finish(dialog)
    if dialog.exec() != StartupDialog.DialogCode.Accepted:
        sys.exit(0)

    # Fenêtre principale
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


def StartConsole():
    print("################### START ############################")

if __name__ == "__main__":
    main()
