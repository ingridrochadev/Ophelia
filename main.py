from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget
from ui_login import Ui_Form
from ui_main import Ui_MainWindow
import sys

class Login(QWidget, Ui_Form):
    def __init__(self):
        super(Login, self).__init__()
        self.setupUi(self)
        self.setWindowTitle('Ophelia')

        self.btn_entrar.clicked.connect(self.open_system)
    
    def open_system(self):
        
        if self.senha_line.text() == '1234':
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            print('Senha inválida!')
    
class MainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super(MainWindow, self).__init__()
            self.setupUi(self)
            self.setWindowTitle("Ophelia")
            appIcon = QIcon(u"")
            self.setWindowIcon(appIcon)
            
            #Togle Button
            self.btn_toggle.clicked.connect(self.leftMenu)
            
            #Páginas do sistema
            self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
            self.btn_add.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_adicionar))
            self.btn_listar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_listar))
            self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
            self.btn_editarUsuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_alterar_usuario))
            
        def leftMenu(self):
            width = self.left_container.width()
            if width == 9:
                newWidth = 200
            else:
                newWidth = 9

            self.animation = QPropertyAnimation(self.left_container, b"maximumWidth")
            self.animation.setDuration(700)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newWidth)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
            
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()