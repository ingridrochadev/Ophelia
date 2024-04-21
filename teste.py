from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Selecionar Arquivo")
        self.setGeometry(100, 100, 400, 200)

        self.button = QPushButton("Selecionar Arquivo", self)
        self.button.clicked.connect(self.open_file_dialog)
        self.button.setGeometry(100, 50, 200, 50)

    def open_file_dialog(self):
        file_dialog = QFileDialog(self)
        file_dialog.setWindowTitle("Selecionar Arquivo")
        file_dialog.setFileMode(QFileDialog.ExistingFile)
        file_dialog.setViewMode(QFileDialog.Detail)

        if file_dialog.exec():
            selected_files = file_dialog.selectedFiles()
            for file_name in selected_files:
                print("Arquivo selecionado:", file_name)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

import os
import xml.etree.ElementTree as et
from Ophelia.src.image_processing.Versao_Final_OCR import read_visto


class ler_img():
    def __init__(self, directory):
        self.directory = directory
    
    def all_files(self):
        return [os.path.join(self.directory, arq) for arq in os.listdir(self.directory)]
    
    def nfe_data(self, xml):
        lista_vistos = []
        
        root = et.parse(xml).getroot()
        nome = self.check_none(root.find(, ))
        data_nasc = self.check_none(root.find(, ))
        nacionalidade = self.check_none(root.find(, ))
        passaporte = self.check_none(root.find(, ))
        cidade_emitente = self.check_none(root.find(, ))
        validade_visto = self.check_none(root.find(, ))
        tipo_visto = self.check_none(root.find(, ))
        num_visto = self.check_none(root.find(, ))
        
        dados = [nome, data_nasc, nacionalidade, passaporte, cidade_emitente, validade_visto, tipo_visto, num_visto]
        
        lista_vistos.append(dados)
        
    def check_none(self, var):
        if var == None:
            return ""
        else:
            try:
                return var.text
            except:
                return var.text
            
if __name__ == "__main__":
    img = ler_img("/home/tecno/Área de trabalho/Programmation/AlphaEdtech/Trilha 1/Desafio/Ophelia/src/image_processing/docs")
    all = img.all_files()
    
    for i in all:
        result = img.nfe_data
        
        print(result)
    
    