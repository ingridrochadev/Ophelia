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
import openpyxl

sistema = Sistema()
func = Funcoes()

class Login(QWidget, Ui_Form):
    def __init__(self):
        super(Login, self).__init__()
        self.tentativas = 0
        self.setupUi(self)
        self.setWindowTitle('Ophelia')
        self.resize(900, 660)
        appIcon = QIcon(u"pages/icons/logo_branca.png")
        self.setWindowIcon(appIcon)

        self.btn_entrar.clicked.connect(self.open_system)
        self.stackedWidget.setCurrentWidget(self.page_login)
        
        self.set_up_botoes_login()
        
    def set_up_botoes_login(self):
        self.btn_esquecer_senha.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_email_esqueci))
        self.btn_send_email_esqueci.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_codigo_2))
        self.btn_entrar.clicked.connect(self.open_system)
        self.btn_voltar1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_login))
        self.btn_voltar1_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_login))
        self.btn_voltar1_3.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_login))
        # if codigo_certo:
        #     self.btn_send_email_esqueci_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_mudar_senha))
        # else:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
        #     msg.setWindowTitle('Acesso inválido!')
        #     msg.setText(f'Código Incorreto')
        #     msg.exec()
        
    def open_system(self):
        email = self.email_line.text()  # Obtém o texto digitado no campo de email
        senha = self.senha_line.text()
        usuario_verificado = sistema.fazer_login(email, senha)
        perfil = sistema.verificar_tipo_perfil(email)
        
        if usuario_verificado:
            self.w = MainWindow(perfil)
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
        def __init__(self, perfil):
            super(MainWindow, self).__init__()
            self.setupUi(self)
            self.setWindowTitle("Ophelia")
            self.resize(1200, 800)
            appIcon = QIcon(u"pages/icons/logo_branca.png")
            self.setWindowIcon(appIcon)
            # Define a página inicial como 'pg_home'
            self.Pages.setCurrentWidget(self.pg_home)
            # Armazenar os dados do visto
            self.dados_visto = None
            self.status_visto = None
            self.set_up_botoes(perfil)
            
        def leftMenu(self):
            width = self.left_container.width()
            newWidth = 200 if width == 9 else 9

            self.animation = QPropertyAnimation(self.left_container, b"maximumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(width)
            self.animation.setEndValue(newWidth)
            self.animation.setEasingCurve(QEasingCurve.InOutQuart)
            self.animation.start()
        
        def set_up_botoes(self, perfil):
            
            if perfil == "user":
                self.btn_inserir_user.setVisible(False)
            #Togle Button
            self.btn_toggle.clicked.connect(self.leftMenu)
            #Páginas do sistema
            self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
            self.btn_add.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_adicionar))
            self.btn_listar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_listar))
            self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_sobre))
            self.btn_inserir_user.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_inserir_user))
            self.btn_editarUsuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_alterar_usuario))
            self.btn_logout.clicked.connect(lambda: self.Pages.setCurrentWidget(Login()))
            
            #Botões de importação
            self.btn_ler.clicked.connect(self.leitura_img)
            self.btn_add_2.clicked.connect(self.inserir_dados_bd)
            self.btn_add_user.clicked.connect(self.criar_novo_usuario)
            self.btn_alterar_senha.clicked.connect(self.alterar_senha)
            self.btn_listar_vistos.clicked.connect(self.buscar_vistos)
            self.btn_exportar.clicked.connect(self.exportar_excel)
        
        def pop_up_success(self,titulo,texto):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Information)
            msg.setWindowTitle(titulo)
            msg.setText(texto)
            msg.exec()
        
        def pop_up_error(self,titulo,texto):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setWindowTitle(titulo)
            msg.setText(texto)
            msg.exec()
        
        def pop_up_restricoes(self,regra):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setWindowTitle(f"Visto tipo {self.dados_visto[5].upper()}")
            msg.setInformativeText(regra)
            
            # Define os botões e seus textos
            ok_button = msg.addButton(QMessageBox.Ok)
            ok_button.setText("\n Autorizar \n Embarque")
            discard_button = msg.addButton(QMessageBox.Discard)
            discard_button.setText("\n Negar \n Embarque")
            cancel_button = msg.addButton(QMessageBox.Cancel)
            cancel_button.setText("\n Cancelar")
            msg.setDefaultButton(QMessageBox.Cancel)
            msg.setFixedSize(200, 500)
                    
            layout = msg.layout()
            if isinstance(layout, QBoxLayout):
                layout.setAlignment(Qt.AlignTop)  # Alinha os botões ao topo
                layout.setSpacing(10)
            resp = msg.exec()
            
            if resp == QMessageBox.Ok:
                self.dados_atualizados("Aprovado")
                try:
                    func.inserir_dados(self.dados_visto, self.status_visto)
                    self.limpar_tela_visto()
                    self.pop_up_success('Visto inserido', 'Visto salvo com sucesso!')

                except Exception as e:
                    self.pop_up_success('Erro ao inserir visto', f'Erro ao inserir dados na tabela de vistos: {str(e)}')
            
            elif resp == QMessageBox.Discard:
                self.dados_atualizados("Negado")

                try:
                    func.inserir_dados(self.dados_visto, self.status_visto)
                    self.limpar_tela_visto()
                    self.pop_up_success('Visto inserido', 'Visto salvo com sucesso!')
                            
                except Exception as e:
                    self.pop_up_success('Erro ao inserir visto', f'Erro ao inserir dados na tabela de vistos: {str(e)}')
            
        def limpar_tela_visto(self):
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
                self.city_line.setText(self.dados_visto[6])
                self.nacionalidade_line.setText(self.dados_visto[2])
                self.num_visto_line.setText(self.dados_visto[7])

                pixmap = QPixmap(arquivo_path[0])
                self.img_space.setPixmap(pixmap.scaled(self.img_space.size(), Qt.KeepAspectRatio))
        
        def dados_atualizados(self, status):
        #Atualizar dados lidos com as edições feitas
            self.dados_visto[0] = self.nome_line.text()
            self.dados_visto[1] = self.passport_line.text()
            self.dados_visto[2] = self.nacionalidade_line.text()
            self.dados_visto[3] = self.date_nasc_line.text()
            self.dados_visto[4] = self.validade_line.text()
            self.dados_visto[5] = self.tipo_visto_line.text()                
            self.dados_visto[6] = self.city_line.text()
            self.dados_visto[7] = self.num_visto_line.text()
            self.status_visto = status
        
        def inserir_dados_bd(self):
            if self.dados_visto:
                regra = func.verificar_regras_embarque(self.dados_visto[5].lower(), self.dados_visto[3], self.dados_visto[4])
                
                # Se Visto estiver ok
                if regra:
                    self.pop_up_restricoes(regra)
                else:
                    self.dados_atualizados("Aprovado")
                    try:
                        func.inserir_dados(self.dados_visto, self.status_visto)
                        print(self.status_visto)
                        self.limpar_tela_visto()
                        self.pop_up_success('Visto inserido', 'Visto salvo com sucesso!')
                        
                    except Exception as e:
                            self.pop_up_success('Erro ao inserir visto', f'Erro ao inserir dados na tabela de vistos: {str(e)}')
        
        def buscar_vistos(self):
            self.tbl_vistos.setStyleSheet(u"QHeaderView::section{color:white;color:#fff;font-size: 15px;} QTableWidget{background-color:rgb(252, 252, 252);color:#430B78;}")
            func = Funcoes()
            result = func.listar_vistos_sys()
            self.tbl_vistos.clearContents()
            self.tbl_vistos.setRowCount(len(result))

            for row, text in enumerate(result):
                for column, data in enumerate(text):
                    self.tbl_vistos.setItem(row, column, QTableWidgetItem(str(data)))
        
        def criar_novo_usuario(self):
            nome = self.nome_user_line.text()
            cpf = self.cpf_line.text()
            email = self.email_user_line.text()
            senha = self.senha_add_user_ln.text()
            matricula = self.matricula_line.text()
            tipo_usuario = self.cb_perfil.currentText()
            
            sistema.criar_usuario(nome, cpf, email, senha, matricula, tipo_usuario)
            self.pop_up_success('Usuário inserido', 'Usuário inserido com sucesso!')
        
        def alterar_senha(self):
            email = self.emial_line.text()
            senha_atual = self.senha_atual_line.text()
            nova_senha = self.senha_line.text()
            nova_senha2 = self.senha_line_2.text()
            
            verificacao = sistema.alterar_senha(email, senha_atual, nova_senha, nova_senha2)
            
            if verificacao == "Verificado":
                self.emial_line.clear()
                self.senha_atual_line.clear()
                self.senha_line.clear()
                self.senha_line_2.clear()
                self.pop_up_success('Senha alterada', 'Senha alterada com sucesso!')
            else:
                self.pop_up_error('Erro ao alterar senha', verificacao)
        
        def exportar_excel(self):
            try:
                # Chamar o método listar_vistos_sys() na instância func da classe Funcoes
                resultados = func.listar_vistos_sys()
                # Converter os resultados para um DataFrame pandas
                df = pd.DataFrame(resultados, columns=['Nome', 'Passaporte', 'Status'])
                # Exportar para Excel
                df.to_excel('Lista_de_Vistos.xlsx', sheet_name='Vistos', index=False)

                self.pop_up_success('Download','Download efetuado com sucesso!')
                
            except Exception as e:
                print(f'Ocorreu um erro: {e}')
                result = func.listar_vistos_sys()
            

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()