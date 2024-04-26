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
        self.set_initial_fields()
                
    def set_up_botoes_login(self):
        self.btn_esquecer_senha.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_email_esqueci))
        self.btn_send_email_esqueci.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.pg_codigo_2))
        self.btn_voltar1.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_login))
        self.btn_voltar1_2.clicked.connect(lambda: self.stackedWidget.setCurrentWidget(self.page_login))
        
        # #Botões de importação
        self.btn_send_email_esqueci.clicked.connect(self.enviar_email_confirmacao)
        self.btn_redefinir_senha.clicked.connect(self.redefinir_senha)
        
    def set_initial_fields(self):
        self.email = ""
        self.senha= ""
        self.perfil = ""
        self.nome = ""
        self.email_fornecido = ""
        self.codigo = ""
        self.nova_senha = ""
        self.conf_nova_senha = ""
        
    def enviar_email_confirmacao(self):
        self.email_fornecido = self.ln_email_esqueci.text()
        sistema.enviar_confirmacao(self.email_fornecido)
        
    def redefinir_senha(self):
        self.codigo = self.ln_codigo.text()
        self.nova_senha = self.ln_nova_Senha.text()
        self.conf_nova_senha = self.ln_conf_nova_senha.text()
        
        confirmacao_codigo = sistema.redefinir_senha(self.email_fornecido, self.codigo, self.nova_senha, self.conf_nova_senha)
        mw = MainWindow(self.perfil, self.nome)

        if confirmacao_codigo == "Senha alterada com sucesso!":
            mw.pop_up_success("Código Verificado", confirmacao_codigo)
            self.stackedWidget.setCurrentWidget(self.page_login)
            self.ln_codigo.clear()
        else:
            mw.pop_up_error("Código incorreto", confirmacao_codigo)
            self.ln_codigo.clear()
            self.btn_redefinir_senha.connect(self.page_login)
        
    def open_system(self):
        self.email = self.email_line.text()  # Obtém o texto digitado no campo de email
        self.senha = self.senha_line.text()
        usuario_verificado = sistema.fazer_login(self.email, self.senha)
        self.perfil, self.nome = sistema.verificar_tipo_e_nome_perfil(self.email)
        mw = MainWindow(self.perfil, self.nome)
        
        if usuario_verificado:
            self.w = MainWindow(self.perfil, self.nome)
            self.w.show()
            self.close()
            return usuario_verificado
        else:
            if self.tentativas < 3:
                mw.pop_up_warning("Acesso inválido!" f'Verifique se o email e/ou senha estão corretos. \n \n Tentativa: {self.tentativas +1} de 3.')
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setWindowTitle('Acesso inválido!')
                msg.setText(f'Verifique se o email e/ou senha estão corretos. \n \n Tentativa: {self.tentativas +1} de 3.')
                msg.exec()
                self.tentativas += 1
            if self.tentativas == 3:
                sys.exit(0)

    
class MainWindow(QMainWindow, Ui_MainWindow):
        def __init__(self, perfil, nome):
            super(MainWindow, self).__init__()
            self.setupUi(self)
            self.setWindowTitle("Ophelia")
            self.resize(1222, 794)
            appIcon = QIcon(u"pages/icons/logo_branca.png")
            self.setWindowIcon(appIcon)
            self.txt_bemvindo.setText(QCoreApplication.translate("MainWindow", f"Bem-vindo(a), {nome}!", None))
            # Define a página inicial como 'pg_home'
            self.Pages.setCurrentWidget(self.pg_home)
            # Armazenar os dados do visto
            self.dados_visto = None
            self.status_visto = None
            self.set_up_botoes(perfil)
        
        
        def set_up_botoes(self, perfil):
            #Páginas do sistema
            self.btn_home.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_home))
            self.btn_add.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_adicionar))
            self.btn_listar.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_listar))
            self.btn_alterar_visto.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_alterar_visto))
            self.btn_sobre.clicked.connect(lambda: self.Pages.setCurrentWidget(self.page))
            self.btn_inserir_user.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_inserir_user))
            self.btn_listar_usuarios.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_listar_user))
            self.btn_alterar_usuario.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_alterar_user))
            self.btn_alterar_senha_2.clicked.connect(lambda: self.Pages.setCurrentWidget(self.pg_alterar_senha))
            self.btn_logout.clicked.connect(lambda: self.Pages.setCurrentWidget(sys.exit(0)))
            
            #Botões de importação
            self.btn_ler.clicked.connect(self.leitura_img)
            self.btn_add_2.clicked.connect(self.inserir_dados_bd)
            self.btn_add_user.clicked.connect(self.criar_novo_usuario)
            self.btn_alterar_senha.clicked.connect(self.alterar_senha)
            self.btn_listar_vistos.clicked.connect(self.listar_vistos)
            self.btn_exportar.clicked.connect(self.exportar_excel)
            self.btn_listar_vistos_2.clicked.connect(self.listar_usuarios)
            self.btn_exportar_2.clicked.connect(self.exportar_excel_usuarios)
            # self.search_btn.clicked.connect(self.buscar_pax)
            # self.search_btn_2.clicked.connect(self.buscar_user)
            
            if perfil == "user":
                self.btn_inserir_user.setVisible(False)
                self.btn_listar_usuarios.setVisible(False)
                self.btn_alterar_usuario.setVisible(False)
                self.excluir_pax_btn.setVisible(False)
        
        
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
        
        
        def pop_up_warning(self,titulo,texto):
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
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
                self.atualizar_dados("Aprovado")
                try:
                    func.inserir_dados(self.dados_visto, self.status_visto)
                    self.limpar_tela_visto()
                    self.pop_up_success('Visto inserido', 'Visto salvo com sucesso!')

                except Exception as e:
                    self.pop_up_success('Erro ao inserir visto', f'Erro ao inserir dados na tabela de vistos: {str(e)}')
            
            elif resp == QMessageBox.Discard:
                self.atualizar_dados("Negado")

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
        
        
        def atualizar_dados(self, status):
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
                regra = func.verificar_regras_embarque(self.dados_visto[5].lower(), self.dados_visto[3], self.dados_visto[4], self.dados_visto[7])
                
                if regra == "O visto informado já existe no banco de dados": # Se já existe -> não será inserido
                    self.pop_up_warning("Visto já adicionado", "O visto informado já existe no banco de dados")
                elif regra != "Sem regras adicionais": # Se há algum tipo de restrição -> Vai ser inserido, mas com o status Negado
                    self.pop_up_restricoes(regra)
                else:
                    self.atualizar_dados("Aprovado")
                    try:
                        func.inserir_dados(self.dados_visto, self.status_visto)
                        self.limpar_tela_visto()
                        self.pop_up_success('Visto inserido', 'Visto não possui restrições. Salvo com sucesso!')
                        
                    except Exception as e:
                            self.pop_up_success('Erro ao inserir visto', f'Erro ao inserir dados na tabela de vistos: {str(e)}')
        
        
        def gerar_tabela(self, result):
            self.tbl_vistos.clearContents()
            self.tbl_vistos.setRowCount(len(result))

            for row, text in enumerate(result):
                for column, data in enumerate(text):
                    self.tbl_vistos_2.setItem(row, column, QTableWidgetItem(str(data)))
                    
                    
        def gerar_tabela_users(self, result):
            self.tbl_vistos_2.clearContents()
            self.tbl_vistos_2.setRowCount(len(result))

            for row, text in enumerate(result):
                for column, data in enumerate(text):
                    self.tbl_vistos_2.setItem(row, column, QTableWidgetItem(str(data)))

        
        def listar_vistos(self):
            ordenacao = self.cb_perfil_2.currentText()
            apenas_aprovados = self.cb_aprovados.isChecked()
            apenas_negados = self.checkBox_2.isChecked()

            # Determina a função de consulta com base nos parâmetros
            if apenas_aprovados:
                if ordenacao == "Ordenar por:":
                    result = func.listar_vistos_aprovados()
                elif ordenacao == "                     A-Z":
                    result = func.listar_vistos_aprovados_asc()
                elif ordenacao == "                     Z-A":
                    result = func.listar_vistos_aprovados_desc()
            elif apenas_negados:
                if ordenacao == "Ordenar por:":
                    result = func.listar_vistos_negados()
                elif ordenacao == "                     A-Z":
                    result = func.listar_vistos_negados_asc()
                elif ordenacao == "                     Z-A":
                    result = func.listar_vistos_negados_desc()
            else:
                if ordenacao == "Ordenar por:":
                    result = func.listar_vistos_sys()
                elif ordenacao == "                     A-Z":
                    result = func.listar_vistos_asc()
                elif ordenacao == "                     Z-A":
                    result = func.listar_vistos_desc()
            # Gerar a tabela com base no resultado da consulta
            self.gerar_tabela(result)

        
        def listar_usuarios(self):
            ordenacao = self.cb_perfil_listar.currentText()
            apenas_supervisores = self.cb_supervisores.isChecked()
            apenas_agentes = self.cb_agentes.isChecked()

            # Determina a função de consulta com base nos parâmetros
            if apenas_supervisores:
                if ordenacao == "Ordenar por:":
                    result = sistema.listar_usuarios_supervisor()
                elif ordenacao == "                     A-Z":
                    result = sistema.listar_usuarios_supervisor_asc()
                elif ordenacao == "                     Z-A":
                    result = sistema.listar_usuarios_supervisor_desc()
            elif apenas_agentes:
                if ordenacao == "Ordenar por:":
                    result = sistema.listar_usuarios_agente()
                elif ordenacao == "                     A-Z":
                    result = sistema.listar_usuarios_agente_asc()
                elif ordenacao == "                     Z-A":
                    result = sistema.listar_usuarios_agente_desc()
            else:
                if ordenacao == "Ordenar por:":
                    result = sistema.listar_usuarios_default()
                elif ordenacao == "                     A-Z":
                    result = sistema.listar_usuarios_asc()
                elif ordenacao == "                     Z-A":
                    result = sistema.listar_usuarios_desc()
            # Gerar a tabela com base no resultado da consulta
            self.gerar_tabela_users(result)
        
        
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
                self.pop_up_warning('Erro ao alterar senha', verificacao)
        
        
        def exportar_excel(self):
            try:
                resultados = func.listar_vistos_sys()
                # Converter os resultados para um DataFrame pandas
                df = pd.DataFrame(resultados, columns=['Nome', 'Passaporte', 'Status'])
                # Exportar para Excel
                df.to_excel('Lista_de_Vistos.xlsx', sheet_name='Vistos', index=False)

                self.pop_up_success('Download','Download efetuado com sucesso!')
                
            except Exception as e:
                print(f'Ocorreu um erro: {e}')
                result = func.listar_vistos_sys()
                
        
        def exportar_excel_usuarios(self):
            try:
                resultados = sistema.listar_usuarios_default()
                # Converter os resultados para um DataFrame pandas
                df = pd.DataFrame(resultados, columns=['Nome', 'Passaporte', 'Status'])
                # Exportar para Excel
                df.to_excel('Lista_de_Vistos.xlsx', sheet_name='Vistos', index=False)

                self.pop_up_success('Download','Download efetuado com sucesso!')
                
            except Exception as e:
                print(f'Ocorreu um erro: {e}')
                result = sistema.listar_usuarios_default()
            
            
        # def buscar_pax(self):
        #     self.passaporte = self.search_ln.text()
        #     self.dados_pax = "array da funcao"
        #     # Preenche os QLineEdit com os dados obtidos do OCR
        #     self.nome_line_2.setText(self.dados_pax[0])
        #     self.date_nasc_line_2.setText(self.dados_pax[1])
        #     self.nacionalidade_line_2.setText(self.dados_pax[2])
        #     self.tipo_visto_line_3.setText(self.dados_pax[3])
        #     self.num_visto_line_2.setText(self.dados_pax[4])
        #     self.validade_line_2.setText(self.dados_pax[5])
        #     self.city_line_2.setText(self.dados_pax[6])
        #     self.status_embarque_line.setText(self.dados_pax[7])
            
        # def editar_pax(self):
        #     #Tranforma o conteúdo das linhas editáveis em um array de retorno:
        #     self.dados_pax[1] = self.nome_line_2.text()
        #     self.dados_pax[1] = self.date_nasc_line_2.text()
        #     self.dados_pax[1] = self.nacionalidade_line_2.text()
        #     self.dados_pax[1] = self.tipo_visto_line_3.text()
        #     self.dados_pax[1] = self.num_visto_line_2.text()
        #     self.dados_pax[1] = self.validade_line_2.text()                
        #     self.dados_pax[1] = self.city_line_2.text()
        #     self.dados_pax[1] = self.status_embarque_line.text()

        #     self.alterar_user_btn.clicked.connect(func.editar_dados( self.passaporte, self.nome_line_2.text(), nacionalidade = None, data_nascimento = None, numero_visto = None, tipo_visto = None, local_emissor = None, data_validade = None, status = None))
        
        # def buscar_user(self):
        #     self.dados_user = "array da funcao"
        #     # Preenche os QLineEdit com os dados obtidos do OCR
        #     self.nome_user_line_2.setText(self.dados_user[0])
        #     self.cpf_line_2.setText(self.dados_user[1])
        #     self.email_user_line_2.setText(self.dados_user[2])
        #     self.senha_add_user_ln_2.setText(self.dados_user[3])
        #     pass
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Login()
    window.show()
    app.exec()