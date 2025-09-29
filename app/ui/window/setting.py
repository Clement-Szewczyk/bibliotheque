from PyQt6.QtWidgets import (QDialog, QVBoxLayout, QHBoxLayout, QTabWidget, 
                             QWidget, QLabel, QLineEdit, QPushButton, QCheckBox, 
                             QComboBox, QSpinBox, QGroupBox, QFormLayout, 
                             QFileDialog, QMessageBox)
from PyQt6.QtCore import Qt
import config
import json
import os

class SettingsWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle(f"{config.APP_NAME} - Paramètres")
        self.setFixedSize(500, 400)
        self.setModal(True)
        
        # Load current settings
        self.settings = self.load_settings()
        
        self.init_ui()
        
    def init_ui(self):
        layout = QVBoxLayout()
        
        # Create tab widget
        tab_widget = QTabWidget()
        
        # General tab
        general_tab = self.create_general_tab()
        tab_widget.addTab(general_tab, "Général")
        
        # Display tab
        display_tab = self.create_display_tab()
        tab_widget.addTab(display_tab, "Affichage")
        
        # Data tab
        data_tab = self.create_data_tab()
        tab_widget.addTab(data_tab, "Données")
        
        layout.addWidget(tab_widget)
        
        # Buttons
        button_layout = QHBoxLayout()
        
        save_button = QPushButton("Sauvegarder")
        cancel_button = QPushButton("Annuler")
        reset_button = QPushButton("Réinitialiser")
        
        save_button.clicked.connect(self.save_settings)
        cancel_button.clicked.connect(self.reject)
        reset_button.clicked.connect(self.reset_settings)
        
        button_layout.addWidget(reset_button)
        button_layout.addStretch()
        button_layout.addWidget(cancel_button)
        button_layout.addWidget(save_button)
        
        layout.addLayout(button_layout)
        self.setLayout(layout)
    
    def create_general_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Application settings group
        app_group = QGroupBox("Application")
        app_layout = QFormLayout()
        
        self.app_name_edit = QLineEdit(self.settings.get("app_name", config.APP_NAME))
        app_layout.addRow("Nom de l'application:", self.app_name_edit)
        
        self.auto_save_check = QCheckBox()
        self.auto_save_check.setChecked(self.settings.get("auto_save", True))
        app_layout.addRow("Sauvegarde automatique:", self.auto_save_check)
        
        self.confirm_exit_check = QCheckBox()
        self.confirm_exit_check.setChecked(self.settings.get("confirm_exit", False))
        app_layout.addRow("Confirmer la fermeture:", self.confirm_exit_check)
        
        app_group.setLayout(app_layout)
        layout.addWidget(app_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def create_display_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Display settings group
        display_group = QGroupBox("Interface")
        display_layout = QFormLayout()
        
        self.theme_combo = QComboBox()
        self.theme_combo.addItems(["Clair", "Sombre", "Système"])
        current_theme = self.settings.get("theme", "Système")
        self.theme_combo.setCurrentText(current_theme)
        display_layout.addRow("Thème:", self.theme_combo)
        
        self.font_size_spin = QSpinBox()
        self.font_size_spin.setRange(8, 24)
        self.font_size_spin.setValue(self.settings.get("font_size", 10))
        display_layout.addRow("Taille de police:", self.font_size_spin)
        
        self.show_splash_check = QCheckBox()
        self.show_splash_check.setChecked(self.settings.get("show_splash", True))
        display_layout.addRow("Afficher l'écran de démarrage:", self.show_splash_check)
        
        display_group.setLayout(display_layout)
        layout.addWidget(display_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def create_data_tab(self):
        widget = QWidget()
        layout = QVBoxLayout()
        
        # Data settings group
        data_group = QGroupBox("Gestion des données")
        data_layout = QFormLayout()
        
        # Data file path
        data_path_layout = QHBoxLayout()
        self.data_path_edit = QLineEdit(self.settings.get("data_path", "./data.json"))
        browse_button = QPushButton("Parcourir...")
        browse_button.clicked.connect(self.browse_data_file)
        data_path_layout.addWidget(self.data_path_edit)
        data_path_layout.addWidget(browse_button)
        data_layout.addRow("Fichier de données:", data_path_layout)
        
        # Backup settings
        self.auto_backup_check = QCheckBox()
        self.auto_backup_check.setChecked(self.settings.get("auto_backup", False))
        data_layout.addRow("Sauvegarde automatique:", self.auto_backup_check)
        
        self.backup_interval_spin = QSpinBox()
        self.backup_interval_spin.setRange(1, 60)
        self.backup_interval_spin.setSuffix(" jours")
        self.backup_interval_spin.setValue(self.settings.get("backup_interval", 7))
        data_layout.addRow("Intervalle de sauvegarde:", self.backup_interval_spin)
        
        data_group.setLayout(data_layout)
        layout.addWidget(data_group)
        
        layout.addStretch()
        widget.setLayout(layout)
        return widget
    
    def browse_data_file(self):
        file_path, _ = QFileDialog.getSaveFileName(
            self, 
            "Sélectionner le fichier de données", 
            self.data_path_edit.text(),
            "JSON Files (*.json);;All Files (*)"
        )
        if file_path:
            self.data_path_edit.setText(file_path)
    
    def load_settings(self):
        settings_file = "settings.json"
        if os.path.exists(settings_file):
            try:
                with open(settings_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except (json.JSONDecodeError, FileNotFoundError):
                pass
        return {}
    
    def save_settings(self):
        settings = {
            "app_name": self.app_name_edit.text(),
            "auto_save": self.auto_save_check.isChecked(),
            "confirm_exit": self.confirm_exit_check.isChecked(),
            "theme": self.theme_combo.currentText(),
            "font_size": self.font_size_spin.value(),
            "show_splash": self.show_splash_check.isChecked(),
            "data_path": self.data_path_edit.text(),
            "auto_backup": self.auto_backup_check.isChecked(),
            "backup_interval": self.backup_interval_spin.value()
        }
        
        try:
            with open("settings.json", 'w', encoding='utf-8') as f:
                json.dump(settings, f, indent=4, ensure_ascii=False)
            
            QMessageBox.information(self, "Paramètres", "Paramètres sauvegardés avec succès!")
            self.accept()
        except Exception as e:
            QMessageBox.critical(self, "Erreur", f"Erreur lors de la sauvegarde: {str(e)}")
    
    def reset_settings(self):
        reply = QMessageBox.question(
            self, 
            "Réinitialiser", 
            "Êtes-vous sûr de vouloir réinitialiser tous les paramètres?",
            QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No
        )
        
        if reply == QMessageBox.StandardButton.Yes:
            # Reset to default values
            self.app_name_edit.setText(config.APP_NAME)
            self.auto_save_check.setChecked(True)
            self.confirm_exit_check.setChecked(False)
            self.theme_combo.setCurrentText("Système")
            self.font_size_spin.setValue(10)
            self.show_splash_check.setChecked(True)
            self.data_path_edit.setText("./data.json")
            self.auto_backup_check.setChecked(False)
            self.backup_interval_spin.setValue(7)


