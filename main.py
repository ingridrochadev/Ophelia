from PySide6.QtCore import Qt
from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog
from pages.ui_login import Ui_Form
from pages.ui_main import Ui_MainWindow
from pages.utils import Sistema
from src.image_processing.Versao_Final_OCR import read_visto
import sys
from src.database.utils_visto import Funcoes

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
            self.resize(1200, 800)
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
            
            # Define a página inicial como 'pg_home'
            self.Pages.setCurrentWidget(self.pg_home)
            
            #Botões de importação
            self.btn_ler.clicked.connect(self.leitura_img)
            self.btn_add_2.clicked.connect(self.inserir_dados_bd)
            
            # Armazenar os dados do visto
            self.dados_visto = None
            
        def leftMenu(self):
            width = self.left_container.width()
            newWidth = 200 if width == 9 else 9

            self.animation = QPropertyAnimation(self.left_container, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newWidth)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

        def leitura_img(self):
            file_dialog = QFileDialog(self)
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setViewMode(QFileDialog.Detail)

            if file_dialog.exec():
                arquivo_path = file_dialog.selectedFiles()  # Obtém o caminho do arquivo selecionado pelo usuário como array, precisa passar o index quando usar

            if arquivo_path:  # Verifica se o caminho do arquivo foi selecionado
                self.dados_visto = read_visto(arquivo_path[0])  # Passa o caminho do arquivo para a função read_visto
                
                dt_nascimento = self.dados_visto[3].strftime("%d-%m-%Y")
                validade_visto = self.dados_visto[4].strftime("%d-%m-%Y")                
                
                # Preenche os QLineEdit com os dados obtidos do OCR
                self.nome_line.setText(self.dados_visto[0])
                self.passport_line.setText(self.dados_visto[1])
                self.tipo_visto_line.setText(self.dados_visto[5])
                self.date_nasc_line.setText(dt_nascimento)
                self.validade_line.setText(validade_visto)
                self.gender_line.setText(self.dados_visto[6])
                self.nacionalidade_line.setText(self.dados_visto[2])
                self.num_visto_line.setText(self.dados_visto[7])
                
                #Atualizar dados lidos com as edições feitas
                self.dados_visto[0] = self.nome_line.text()
                self.dados_visto[1] = self.passport_line.text()
                self.dados_visto[2] = self.nacionalidade_line.text()
                self.dados_visto[3] = self.date_nasc_line.text()
                self.dados_visto[4] = self.validade_line.text()
                self.dados_visto[5] = self.tipo_visto_line.text()                
                self.dados_visto[6] = self.gender_line.text()
                self.dados_visto[7] = self.num_visto_line.text()

                pixmap = QPixmap(arquivo_path[0])
                self.img_space.setPixmap(pixmap.scaled(self.img_space.size(), Qt.KeepAspectRatio))
            
        def inserir_dados_bd(self):
            if self.dados_visto:
                func = Funcoes()
                regra = func.verificar_regras_embarque(self.dados_visto[5].lower())
                if regra:
                    msg = QMessageBox()
                    msg.setWindowTitle(f"Visto tipo {self.dados_visto[5].upper()}")
                    msg.setInformativeText(regra)
                    msg.setStandardButtons(QMessageBox.Save | QMessageBox.Discard | QMessageBox.Cancel)
                    msg.setDefaultButton(QMessageBox.Save)
                    msg.exec()
                else:
                    func.inserir_dados(self.dados_visto)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle('Visto Inserido!')
                    msg.setText(f'Passageiro salvo com sucesso!')
                    msg.exec()
                
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()