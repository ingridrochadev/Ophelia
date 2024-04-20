from PySide6.QtCore import QCoreApplication
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui_login import Ui_MainWindow
import sys
from ui_teste import Ui_TestWindow

import sys
sys.path.append('../../pages')

from utils import Sistema

class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.login)
        self.setWindowTitle("Ophelia Sistem")
        appIcon = QIcon(u"")
        self.setWindowIcon(appIcon)

    def login(self):
        admin = "admin"
        senha ="admin"
        user = self.ui.lineEdit.text()
        passwd = self.ui.lineEdit_2.text()
        if admin == user and passwd ==senha:
            QMessageBox.information (QMessageBox(), "login realizado!", "ENTROU COM SUCESSO!")
            self.window = TesteWindow()
            self.window.show()
        else:
            QMessageBox.warning (QMessageBox(), "login errado!", "NÃO ENTROU COM SUCESSO!")

class TesteWindow(QMainWindow, Ui_TestWindow):
    def __init__(self):
        super(TesteWindow, self).__init__()
        self.setupUi(self)
        self.setWindowTitle("Ophelia TESTEEE")


if __name__ == '__main__':
    # login = QApplication(sys.argv)
    # windowl = MainWindow()
    # windowl.show()
    # login.exec()
    bianca = Sistema()
    # bianca.criar_usuario("bibi", "bibi", "bibi", "bibi", 1)
    bianca.fazer_login("bibi","bibi")
