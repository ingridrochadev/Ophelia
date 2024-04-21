from PySide6.QtCore import Qt
from PySide6.QtCore import QCoreApplication, QPropertyAnimation, QEasingCurve
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QMessageBox, QFileDialog, QBoxLayout
from pages.ui_login import Ui_Form
from pages.ui_main import Ui_MainWindow
from pages.utils import Sistema
from src.image_processing.Versao_Final_OCR import read_visto
import sys
from pages.utils_visto import Funcoes

sistema = Sistema()
    
class Home(QMainWindow, Ui_MainWindow):
        def __init__(self):
            super(Home, self).__init__()
            self.setupUi(self)
            self.setWindowTitle("Ophelia")
            self.resize(1200, 800)
            appIcon = QIcon(u"")
            self.setWindowIcon(appIcon)
            
            # Armazenar os dados do visto
            self.dados_visto = None
            
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
            
        def leftMenu(self):
            width = self.left_container.width()
            newWidth = 200 if width == 9 else 9

            self.animation = QPropertyAnimation(self.left_container, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newWidth)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()

        def leitura_img(self, nome_line, passport_line, tipo_visto_line, date_nasc_line, validade_line, city_line, nacionalidade_line, num_visto_line, dados_visto, img_space):
            file_dialog = QFileDialog(None)
            file_dialog.setFileMode(QFileDialog.ExistingFile)
            file_dialog.setViewMode(QFileDialog.Detail)

            if file_dialog.exec():
                arquivo_path = file_dialog.selectedFiles()  # Obtém o caminho do arquivo selecionado pelo usuário como array, precisa passar o index quando usar
                print(arquivo_path)
            if arquivo_path:  # Verifica se o caminho do arquivo foi selecionado
                dados_visto = read_visto(arquivo_path[0])  # Passa o caminho do arquivo para a função read_visto
                print(dados_visto)
                if dados_visto:
                    dt_nascimento = dados_visto[3].strftime("%d-%m-%Y")
                    validade_visto = dados_visto[4].strftime("%d-%m-%Y")                
                    
                    # Preenche os QLineEdit com os dados obtidos do OCR
                    nome_line.setText(dados_visto[0])
                    passport_line.setText(dados_visto[1])
                    tipo_visto_line.setText(dados_visto[5])
                    date_nasc_line.setText(dt_nascimento)
                    validade_line.setText(validade_visto)
                    city_line.setText(dados_visto[6])
                    nacionalidade_line.setText(dados_visto[2])
                    num_visto_line.setText(dados_visto[7])
                    print(dados_visto)

                    pixmap = QPixmap(arquivo_path[0])
                    self.img_space.setPixmap(pixmap.scaled(self.img_space.size(), Qt.KeepAspectRatio))
                    
                    return dados_visto
                
                else:
                    QMessageBox.warning(self, "Erro", "Não foi possível ler o arquivo. Verifique se é uma imagem válida.")             
                
                # Preenche os QLineEdit com os dados obtidos do OCR
                nome_line.setText(self.dados_visto[0])
                passport_line.setText(self.dados_visto[1])
                tipo_visto_line.setText(self.dados_visto[5])
                date_nasc_line.setText(dt_nascimento)
                self.validade_line.setText(validade_visto)
                self.city_line.setText(self.dados_visto[6])
                self.nacionalidade_line.setText(self.dados_visto[2])
                self.num_visto_line.setText(self.dados_visto[7])
                print(self.dados_visto)

                pixmap = QPixmap(arquivo_path[0])
                self.img_space.setPixmap(pixmap.scaled(self.img_space.size(), Qt.KeepAspectRatio))
            
        def inserir_dados_bd(self, dados):
            if dados:
                func = Funcoes()
                regra = func.verificar_regras_embarque(dados[5].lower(), dados[3], dados[4])
                
                if regra:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setWindowTitle(f"Visto tipo {dados[5].upper()}")
                    msg.setInformativeText(regra)
                    
                    # Define os botões e seus textos
                    ok_button = msg.addButton(QMessageBox.Ok)
                    ok_button.setText("Documentação Válida")
                    
                    discard_button = msg.addButton(QMessageBox.Discard)
                    discard_button.setText("Documentação Inválida")
                    
                    msg.setDefaultButton(QMessageBox.Discard)

                    msg.setFixedSize(200, 500)
                    
                    # Definindo a folha de estilo para a QMessageBox
                    msg.setStyleSheet("QMessageBox { font-size: 12pt; }" 
                                    "QPushButton { font-size: 12pt; }" 
                                    "QPushButton { margin-top: 10px; }")
                    
                    layout = msg.layout()
                    if isinstance(layout, QBoxLayout):
                        layout.setAlignment(Qt.AlignTop)  # Alinha os botões ao topo
                        layout.setSpacing(10)
                    
                    resp = msg.exec()
                    
                    if resp == QMessageBox.Ok:
                        #Atualizar dados lidos com as edições feitas
                        dados[0] = self.nome_line.text()
                        dados[1] = self.passport_line.text()
                        dados[2] = self.nacionalidade_line.text()
                        dados[3] = self.date_nasc_line.text()
                        dados[4] = self.validade_line.text()
                        dados[5] = self.tipo_visto_line.text()                
                        dados[6] = self.city_line.text()
                        dados[7] = self.num_visto_line.text()
                        print(dados)
                        
                        func.inserir_dados(dados)
                        
                        # Limpa os QLineEdit
                        self.nome_line.clear()
                        self.passport_line.clear()
                        self.tipo_visto_line.clear()
                        self.date_nasc_line.clear()
                        self.validade_line.clear()
                        self.city_line.clear()
                        self.nacionalidade_line.clear()
                        self.num_visto_line.clear()
                        # Remove a imagem carregada
                        self.img_space.clear()
                        
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle('Visto Inserido!')
                        msg.setText(f'Visto salvo com sucesso!')
                        msg.exec()
                    else:
                        pass

                else:
                    func.inserir_dados(self.dados_visto)
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setWindowTitle('Visto Inserido!')
                    msg.setText(f'Visto salvo com sucesso!')
                    msg.exec()
