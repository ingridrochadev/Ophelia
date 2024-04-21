from PySide6.QtCore import Qt
from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog
from pages.ui_login import Ui_Form
from pages.ui_main import Ui_MainWindow
from pages.utils import Sistema
from src.image_processing.Versao_Final_OCR import read_visto
import sys
# from src.database.inserir_visto import Funcoes

sistema = Sistema()
class Login(QWidget, Ui_Form):
    def __init__(self):
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle('Ophelia')

        self.btn_entrar.clicked.connect(self.open_system)
    
    def open_system(self):
        email = self.email_line.text()  # Obtenha o texto digitado no campo de email
        senha = self.senha_line.text()
        usuario_verificado = sistema.fazer_login(email, senha)
        
        if usuario_verificado:
            self.w = MainWindow()
            self.w.show()
            self.close()
        else:
            if self.tentativas < 3:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Acesso inválido!')
                msg.setText(f'Verifique se o email e/ou senha estão corretos. \n \n Tentativa: {self.tentativas +1} de 3.')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                sys.exit(0)
    
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
            
            #Botões de importação
            self.btn_ler.clicked.connect(self.leituraImg)
            
        def leftMenu(self):
            width = self.left_container.width()
            newWidth = 200 if width == 9 else 9

            self.animation = QPropertyAnimation(self.left_container, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newWidth)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

        def leituraImg(self):
            file_dialog = QFileDialog(self)
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setViewMode(QFileDialog.Detail)

            if file_dialog.exec():
                arquivo_path = file_dialog.selectedFiles()  # Obtém o caminho do arquivo selecionado pelo usuário

            if arquivo_path:  # Verifica se o caminho do arquivo foi selecionado
                dados_visto = read_visto(arquivo_path[0])  # Passa o caminho do arquivo para a função read_visto
                print(dados_visto)
                pixmap = QPixmap(arquivo_path[0])
                self.img_space.setPixmap(pixmap.scaled(self.img_space.size(), Qt.KeepAspectRatio))
            
            # func.inserir_dados(img_dados)
            # tipo, descricao, regra = func.verificar_tipo_visto
            
            # if !(regra):
            #     msg = QMessageBox()
            #     msg.setIcon(QMessageBox.Information)
            #     msg.setWindowTitle('Visto adicionado!')
            #     msg.exec()
            # else:
            #     msg = QMessageBox()
            #     msg.setWindowTitle(f"Visto tipo {tipo.upper()}")
            #     msg.setInformativeText(regra)
            #     msg.setStandardButtons(msg::Save | msg::Discard | msg::Cancel)
            #     msg.setDefaultButton(msg::Save)
            #     int ret = msg.exec()
                
                
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()