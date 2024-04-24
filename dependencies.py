from PySide6.QtCore import Qt
from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog, QBoxLayout, QTableWidgetItem
from pages.ui_login import Ui_Form
from pages.ui_main import Ui_MainWindow
from src.image_processing.Versao_Final_OCR import read_visto
from src.database.utils.utils_usuario import Sistema
from src.database.utils.utils_visto import Funcoes
# from pages.utils_interface import Home
import sys
import pandas as pd