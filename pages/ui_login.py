# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 6.7.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QPlainTextEdit, QPushButton, QSizePolicy, QStackedWidget,
    QWidget)
import pages.logo_rc as logo_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(909, 655)
        Form.setStyleSheet(u"background-color: white;")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(10, 0, 901, 661))
        self.page_login = QWidget()
        self.page_login.setObjectName(u"page_login")
        self.frame_2 = QFrame(self.page_login)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(-10, 0, 911, 661))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.frame = QFrame(self.frame_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(440, 60, 391, 521))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-color:#480070;\n"
"border-width:5px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"}\n"
"\n"
"QLabel{\n"
"border-color:white;\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btn_entrar = QPushButton(self.frame)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(150, 390, 160, 40))
        self.btn_entrar.setMinimumSize(QSize(160, 40))
        self.btn_entrar.setMaximumSize(QSize(160, 16777215))
        font = QFont()
        font.setPointSize(12)
        self.btn_entrar.setFont(font)
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"QPushButton{\n"
"background-color:#480070;\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #D589FF;\n"
"color: #480070;\n"
"border-radius: 10px;\n"
"}")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(120, 40, 201, 201))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"        QFrame {\n"
"            background-color: rgba(231, 231, 231, 0); /* Define a cor de fundo como transparente */\n"
"        }")
        self.label.setPixmap(QPixmap(u":/icons/pages/icons/logo_roxa.png"))
        self.label.setScaledContents(True)
        self.email_line = QLineEdit(self.frame)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setGeometry(QRect(100, 260, 250, 35))
        self.email_line.setMinimumSize(QSize(250, 35))
        self.email_line.setMaximumSize(QSize(250, 35))
        font1 = QFont()
        font1.setFamilies([u"Lato Heavy"])
        font1.setPointSize(11)
        font1.setBold(False)
        font1.setItalic(False)
        self.email_line.setFont(font1)
        self.email_line.setLayoutDirection(Qt.LeftToRight)
        self.email_line.setStyleSheet(u"background-color: rgba(0, 0 , 0, 0);\n"
"border: 2.5px solid rgba(0,0,0,0);\n"
"border-bottom-color: #480070;\n"
"color: #480070;\n"
"padding-bottom: 8px;\n"
"border-radius: 0px;\n"
"font: 11pt \"Lato Heavy\";")
        self.email_line.setAlignment(Qt.AlignCenter)
        self.senha_line = QLineEdit(self.frame)
        self.senha_line.setObjectName(u"senha_line")
        self.senha_line.setGeometry(QRect(100, 320, 250, 35))
        self.senha_line.setMinimumSize(QSize(250, 35))
        self.senha_line.setMaximumSize(QSize(250, 35))
        self.senha_line.setFont(font1)
        self.senha_line.setLayoutDirection(Qt.LeftToRight)
        self.senha_line.setStyleSheet(u"background-color: rgba(0, 0 , 0, 0);\n"
"border: 2.5px solid rgba(0,0,0,0);\n"
"border-bottom-color: #480070;\n"
"color: #480070;\n"
"padding-bottom: 8px;\n"
"border-radius: 0px;\n"
"font: 11pt \"Lato Heavy\";")
        self.senha_line.setEchoMode(QLineEdit.Password)
        self.senha_line.setAlignment(Qt.AlignCenter)
        self.btn_esquecer_senha = QPushButton(self.frame)
        self.btn_esquecer_senha.setObjectName(u"btn_esquecer_senha")
        self.btn_esquecer_senha.setGeometry(QRect(150, 430, 160, 25))
        self.btn_esquecer_senha.setMinimumSize(QSize(160, 25))
        self.btn_esquecer_senha.setMaximumSize(QSize(160, 25))
        font2 = QFont()
        font2.setFamilies([u"Lato Heavy"])
        font2.setPointSize(11)
        font2.setBold(False)
        font2.setItalic(False)
        font2.setUnderline(True)
        self.btn_esquecer_senha.setFont(font2)
        self.btn_esquecer_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_esquecer_senha.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0 , 0, 0);\n"
"color: #480070;\n"
"border-radius: 0px;\n"
"font: 11pt \"Lato Heavy\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #D589FF;\n"
"}")
        self.frame_3 = QFrame(self.frame_2)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(170, 170, 120, 80))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_4 = QFrame(self.frame_2)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(70, 30, 431, 581))
        self.frame_4.setStyleSheet(u"QFrame{\n"
"background-color:#480070;\n"
"border-color:#480070;\n"
"border-width:5px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"}\n"
"QLineEdit{\n"
"color: rgb(255,255,255);\n"
"border-color:rgb(255,255,255);\n"
"border-width: 1px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:5px; /* Define o estilo da borda como s\u00f3lido */\n"
"}\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.label_2 = QLabel(self.frame_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 220, 351, 331))
        self.label_2.setPixmap(QPixmap(u":/icons/pages/icons/Black Minimalist Outline Icons Icon Set (4).png"))
        self.label_2.setScaledContents(True)
        self.plainTextEdit = QPlainTextEdit(self.frame_4)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(20, 90, 401, 151))
        font3 = QFont()
        font3.setFamilies([u"Lato"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.plainTextEdit.setFont(font3)
        self.plainTextEdit.setStyleSheet(u"color: white;")
        self.plainTextEdit_2 = QPlainTextEdit(self.frame_4)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(20, 30, 211, 61))
        font4 = QFont()
        font4.setFamilies([u"Lato"])
        font4.setPointSize(21)
        font4.setBold(True)
        self.plainTextEdit_2.setFont(font4)
        self.plainTextEdit_2.setStyleSheet(u"color: white;")
        self.stackedWidget.addWidget(self.page_login)
        self.pg_email_esqueci = QWidget()
        self.pg_email_esqueci.setObjectName(u"pg_email_esqueci")
        self.pg_email_esqueci.setStyleSheet(u"background-color:white;")
        self.frame_5 = QFrame(self.pg_email_esqueci)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setGeometry(QRect(-10, 0, 921, 671))
        self.frame_5.setStyleSheet(u"background-color:white;\n"
"corder color: white;")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(240, 0, 671, 661))
        self.label_3.setPixmap(QPixmap(u":/icons/pages/icons/Fundo.png"))
        self.label_3.setScaledContents(True)
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(280, 130, 361, 261))
        sizePolicy1.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy1)
        self.frame_6.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-color:#480070;\n"
"border-width:5px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"}\n"
"\n"
"QLabel{\n"
"border-color:white;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.btn_send_email_esqueci = QPushButton(self.frame_6)
        self.btn_send_email_esqueci.setObjectName(u"btn_send_email_esqueci")
        self.btn_send_email_esqueci.setGeometry(QRect(100, 200, 160, 40))
        self.btn_send_email_esqueci.setMinimumSize(QSize(160, 40))
        self.btn_send_email_esqueci.setMaximumSize(QSize(160, 16777215))
        self.btn_send_email_esqueci.setFont(font)
        self.btn_send_email_esqueci.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send_email_esqueci.setStyleSheet(u"QPushButton{\n"
"background-color:#480070;\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #D589FF;\n"
"color: #480070;\n"
"border-radius: 10px;\n"
"}")
        self.ln_email_esqueci = QLineEdit(self.frame_6)
        self.ln_email_esqueci.setObjectName(u"ln_email_esqueci")
        self.ln_email_esqueci.setGeometry(QRect(60, 150, 250, 35))
        self.ln_email_esqueci.setMinimumSize(QSize(250, 35))
        self.ln_email_esqueci.setMaximumSize(QSize(250, 35))
        self.ln_email_esqueci.setFont(font1)
        self.ln_email_esqueci.setLayoutDirection(Qt.LeftToRight)
        self.ln_email_esqueci.setStyleSheet(u"background-color:white;\n"
"border-color:#480070;\n"
"color:#480070;\n"
"border-width:2px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"")
        self.ln_email_esqueci.setAlignment(Qt.AlignCenter)
        self.btn_voltar1 = QPushButton(self.frame_6)
        self.btn_voltar1.setObjectName(u"btn_voltar1")
        self.btn_voltar1.setGeometry(QRect(10, 10, 40, 40))
        self.btn_voltar1.setMinimumSize(QSize(40, 40))
        self.btn_voltar1.setMaximumSize(QSize(40, 40))
        font5 = QFont()
        font5.setFamilies([u"Lato Heavy"])
        font5.setPointSize(36)
        font5.setBold(False)
        font5.setItalic(False)
        font5.setUnderline(False)
        self.btn_voltar1.setFont(font5)
        self.btn_voltar1.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar1.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0 , 0, 0);\n"
"color: #480070;\n"
"border-radius: 0px;\n"
"font: 36pt \"Lato Heavy\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #D589FF;\n"
"}")
        self.plainTextEdit_3 = QPlainTextEdit(self.frame_6)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(50, 20, 221, 41))
        self.plainTextEdit_3.setFont(font3)
        self.plainTextEdit_3.setStyleSheet(u"border: none;\n"
"color: #480070;")
        self.plainTextEdit_4 = QPlainTextEdit(self.frame_6)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(50, 80, 291, 51))
        font6 = QFont()
        font6.setFamilies([u"Lato"])
        font6.setPointSize(11)
        font6.setBold(False)
        self.plainTextEdit_4.setFont(font6)
        self.plainTextEdit_4.setStyleSheet(u"border: none;\n"
"color: #480070;")
        self.plainTextEdit_4.setReadOnly(True)
        self.plainTextEdit_4.setCenterOnScroll(False)
        self.plainTextEdit_5 = QPlainTextEdit(self.frame_6)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(60, 130, 281, 31))
        font7 = QFont()
        font7.setFamilies([u"Lato"])
        font7.setPointSize(11)
        font7.setBold(True)
        self.plainTextEdit_5.setFont(font7)
        self.plainTextEdit_5.setStyleSheet(u"border: none;\n"
"color: #480070;\n"
"background-color: transparent;")
        self.plainTextEdit_5.setReadOnly(True)
        self.stackedWidget.addWidget(self.pg_email_esqueci)
        self.pg_codigo_2 = QWidget()
        self.pg_codigo_2.setObjectName(u"pg_codigo_2")
        self.frame_7 = QFrame(self.pg_codigo_2)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(-10, 0, 921, 671))
        self.frame_7.setStyleSheet(u"background-color:white;")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_7)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(250, 20, 661, 641))
        self.label_4.setPixmap(QPixmap(u":/icons/pages/icons/Fundo.png"))
        self.label_4.setScaledContents(True)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setGeometry(QRect(280, 130, 361, 261))
        sizePolicy1.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy1)
        self.frame_8.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-color:#480070;\n"
"border-width:5px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"}\n"
"\n"
"QLabel{\n"
"border-color:white;\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.btn_send_email_esqueci_2 = QPushButton(self.frame_8)
        self.btn_send_email_esqueci_2.setObjectName(u"btn_send_email_esqueci_2")
        self.btn_send_email_esqueci_2.setGeometry(QRect(100, 200, 160, 40))
        self.btn_send_email_esqueci_2.setMinimumSize(QSize(160, 40))
        self.btn_send_email_esqueci_2.setMaximumSize(QSize(160, 16777215))
        self.btn_send_email_esqueci_2.setFont(font)
        self.btn_send_email_esqueci_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_send_email_esqueci_2.setStyleSheet(u"QPushButton{\n"
"background-color:#480070;\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #D589FF;\n"
"color: #480070;\n"
"border-radius: 10px;\n"
"}")
        self.ln_codigo = QLineEdit(self.frame_8)
        self.ln_codigo.setObjectName(u"ln_codigo")
        self.ln_codigo.setGeometry(QRect(60, 150, 250, 35))
        self.ln_codigo.setMinimumSize(QSize(250, 35))
        self.ln_codigo.setMaximumSize(QSize(250, 35))
        self.ln_codigo.setFont(font1)
        self.ln_codigo.setLayoutDirection(Qt.LeftToRight)
        self.ln_codigo.setStyleSheet(u"background-color:white;\n"
"border-color:#480070;\n"
"color:#480070;\n"
"border-width:2px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"")
        self.ln_codigo.setAlignment(Qt.AlignCenter)
        self.btn_voltar1_2 = QPushButton(self.frame_8)
        self.btn_voltar1_2.setObjectName(u"btn_voltar1_2")
        self.btn_voltar1_2.setGeometry(QRect(10, 10, 40, 40))
        self.btn_voltar1_2.setMinimumSize(QSize(40, 40))
        self.btn_voltar1_2.setMaximumSize(QSize(40, 40))
        self.btn_voltar1_2.setFont(font5)
        self.btn_voltar1_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar1_2.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0 , 0, 0);\n"
"color: #480070;\n"
"border-radius: 0px;\n"
"font: 36pt \"Lato Heavy\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #D589FF;\n"
"}")
        self.plainTextEdit_6 = QPlainTextEdit(self.frame_8)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(50, 20, 311, 41))
        self.plainTextEdit_6.setFont(font3)
        self.plainTextEdit_6.setStyleSheet(u"border: none;\n"
"color: #480070;\n"
"background-color: transparent;")
        self.plainTextEdit_7 = QPlainTextEdit(self.frame_8)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setGeometry(QRect(50, 60, 291, 71))
        self.plainTextEdit_7.setFont(font6)
        self.plainTextEdit_7.setStyleSheet(u"border: none;\n"
"color: #480070;")
        self.plainTextEdit_7.setReadOnly(True)
        self.plainTextEdit_7.setCenterOnScroll(False)
        self.plainTextEdit_8 = QPlainTextEdit(self.frame_8)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setGeometry(QRect(60, 130, 281, 31))
        self.plainTextEdit_8.setFont(font7)
        self.plainTextEdit_8.setStyleSheet(u"border: none;\n"
"color: #480070;\n"
"background-color: transparent;")
        self.plainTextEdit_8.setReadOnly(True)
        self.stackedWidget.addWidget(self.pg_codigo_2)
        self.pg_mudar_senha = QWidget()
        self.pg_mudar_senha.setObjectName(u"pg_mudar_senha")
        self.frame_9 = QFrame(self.pg_mudar_senha)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(-40, 0, 951, 671))
        self.frame_9.setStyleSheet(u"background-color:white;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_9)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(220, 20, 721, 641))
        self.label_5.setPixmap(QPixmap(u":/icons/pages/icons/Fundo.png"))
        self.label_5.setScaledContents(True)
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(320, 120, 341, 361))
        sizePolicy1.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy1)
        self.frame_10.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-color:#480070;\n"
"border-width:5px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"}\n"
"\n"
"QLabel{\n"
"border-color:white;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.btn_redefinir_senha = QPushButton(self.frame_10)
        self.btn_redefinir_senha.setObjectName(u"btn_redefinir_senha")
        self.btn_redefinir_senha.setGeometry(QRect(100, 270, 150, 40))
        self.btn_redefinir_senha.setMinimumSize(QSize(150, 40))
        self.btn_redefinir_senha.setMaximumSize(QSize(150, 16777215))
        self.btn_redefinir_senha.setFont(font)
        self.btn_redefinir_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_redefinir_senha.setStyleSheet(u"QPushButton{\n"
"background-color:#480070;\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"background-color: #D589FF;\n"
"color: #480070;\n"
"border-radius: 10px;\n"
"}")
        self.ln_nova_Senha = QLineEdit(self.frame_10)
        self.ln_nova_Senha.setObjectName(u"ln_nova_Senha")
        self.ln_nova_Senha.setGeometry(QRect(50, 140, 250, 35))
        self.ln_nova_Senha.setMinimumSize(QSize(250, 35))
        self.ln_nova_Senha.setMaximumSize(QSize(250, 35))
        self.ln_nova_Senha.setFont(font1)
        self.ln_nova_Senha.setLayoutDirection(Qt.LeftToRight)
        self.ln_nova_Senha.setStyleSheet(u"background-color:white;\n"
"border-color:#480070;\n"
"color:#480070;\n"
"border-width:2px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"")
        self.ln_nova_Senha.setEchoMode(QLineEdit.Password)
        self.ln_nova_Senha.setAlignment(Qt.AlignCenter)
        self.btn_voltar1_3 = QPushButton(self.frame_10)
        self.btn_voltar1_3.setObjectName(u"btn_voltar1_3")
        self.btn_voltar1_3.setGeometry(QRect(10, 10, 40, 40))
        self.btn_voltar1_3.setMinimumSize(QSize(40, 40))
        self.btn_voltar1_3.setMaximumSize(QSize(40, 40))
        self.btn_voltar1_3.setFont(font5)
        self.btn_voltar1_3.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_voltar1_3.setStyleSheet(u"QPushButton{\n"
"background-color: rgba(0, 0 , 0, 0);\n"
"color: #480070;\n"
"border-radius: 0px;\n"
"font: 36pt \"Lato Heavy\";\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"color: #D589FF;\n"
"}")
        self.plainTextEdit_9 = QPlainTextEdit(self.frame_10)
        self.plainTextEdit_9.setObjectName(u"plainTextEdit_9")
        self.plainTextEdit_9.setGeometry(QRect(80, 20, 311, 41))
        self.plainTextEdit_9.setFont(font3)
        self.plainTextEdit_9.setStyleSheet(u"border: none;\n"
"color: #480070;\n"
"background-color: transparent;")
        self.plainTextEdit_10 = QPlainTextEdit(self.frame_10)
        self.plainTextEdit_10.setObjectName(u"plainTextEdit_10")
        self.plainTextEdit_10.setGeometry(QRect(50, 70, 271, 51))
        self.plainTextEdit_10.setFont(font6)
        self.plainTextEdit_10.setStyleSheet(u"border: none;\n"
"color: #480070;")
        self.plainTextEdit_10.setReadOnly(True)
        self.plainTextEdit_10.setCenterOnScroll(False)
        self.plainTextEdit_11 = QPlainTextEdit(self.frame_10)
        self.plainTextEdit_11.setObjectName(u"plainTextEdit_11")
        self.plainTextEdit_11.setGeometry(QRect(50, 120, 281, 31))
        self.plainTextEdit_11.setFont(font7)
        self.plainTextEdit_11.setStyleSheet(u"border: none;\n"
"color: #480070;\n"
"background-color: transparent;")
        self.plainTextEdit_11.setReadOnly(True)
        self.plainTextEdit_12 = QPlainTextEdit(self.frame_10)
        self.plainTextEdit_12.setObjectName(u"plainTextEdit_12")
        self.plainTextEdit_12.setGeometry(QRect(50, 190, 281, 31))
        self.plainTextEdit_12.setFont(font7)
        self.plainTextEdit_12.setStyleSheet(u"border: none;\n"
"color: #480070;\n"
"background-color: transparent;")
        self.plainTextEdit_12.setReadOnly(True)
        self.ln_conf_nova_senha = QLineEdit(self.frame_10)
        self.ln_conf_nova_senha.setObjectName(u"ln_conf_nova_senha")
        self.ln_conf_nova_senha.setGeometry(QRect(50, 210, 250, 35))
        self.ln_conf_nova_senha.setMinimumSize(QSize(250, 35))
        self.ln_conf_nova_senha.setMaximumSize(QSize(250, 35))
        self.ln_conf_nova_senha.setFont(font1)
        self.ln_conf_nova_senha.setLayoutDirection(Qt.LeftToRight)
        self.ln_conf_nova_senha.setStyleSheet(u"background-color:white;\n"
"border-color:#480070;\n"
"color:#480070;\n"
"border-width:2px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"")
        self.ln_conf_nova_senha.setEchoMode(QLineEdit.Password)
        self.ln_conf_nova_senha.setAlignment(Qt.AlignCenter)
        self.stackedWidget.addWidget(self.pg_mudar_senha)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btn_entrar.setText(QCoreApplication.translate("Form", u"Entrar", None))
        self.label.setText("")
        self.email_line.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.senha_line.setText("")
        self.senha_line.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.btn_esquecer_senha.setText(QCoreApplication.translate("Form", u"Esqueceu a senha?", None))
        self.label_2.setText("")
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Form", u"Ol\u00e1, caro colaborador, seja bem-vindo novamente!\n"
"\n"
"Caso ainda n\u00e3o tenha um login, contate seu supervisor para cri\u00e1-lo.", None))
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("Form", u"OPHELIA", None))
        self.label_3.setText("")
        self.btn_send_email_esqueci.setText(QCoreApplication.translate("Form", u"Enviar mensagem", None))
        self.ln_email_esqueci.setText("")
        self.ln_email_esqueci.setPlaceholderText("")
        self.btn_voltar1.setText(QCoreApplication.translate("Form", u"<", None))
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("Form", u"Esqueceu sua senha?", None))
        self.plainTextEdit_4.setPlainText(QCoreApplication.translate("Form", u"N\u00e3o se preocupe, vamos enviar uma mensagem para voc\u00ea redefinir sua senha.", None))
        self.plainTextEdit_5.setPlainText(QCoreApplication.translate("Form", u"E-mail", None))
        self.label_4.setText("")
        self.btn_send_email_esqueci_2.setText(QCoreApplication.translate("Form", u"Continuar", None))
        self.ln_codigo.setText("")
        self.ln_codigo.setPlaceholderText("")
        self.btn_voltar1_2.setText(QCoreApplication.translate("Form", u"<", None))
        self.plainTextEdit_6.setPlainText(QCoreApplication.translate("Form", u"Queremos saber se \u00e9 voc\u00ea mesmo", None))
        self.plainTextEdit_7.setPlainText(QCoreApplication.translate("Form", u"\u00daltimo passo! Para proteger a sua conta, insira o c\u00f3digo que acabamos de enviar para o seu e-mail.", None))
        self.plainTextEdit_8.setPlainText(QCoreApplication.translate("Form", u"C\u00f3digo", None))
        self.label_5.setText("")
        self.btn_redefinir_senha.setText(QCoreApplication.translate("Form", u"Definir Senha", None))
        self.ln_nova_Senha.setText("")
        self.ln_nova_Senha.setPlaceholderText("")
        self.btn_voltar1_3.setText(QCoreApplication.translate("Form", u"<", None))
        self.plainTextEdit_9.setPlainText(QCoreApplication.translate("Form", u"Redefina a sua senha", None))
        self.plainTextEdit_10.setPlainText(QCoreApplication.translate("Form", u"Defina uma nova senha para a sua conta.", None))
        self.plainTextEdit_11.setPlainText(QCoreApplication.translate("Form", u"Nova senha", None))
        self.plainTextEdit_12.setPlainText(QCoreApplication.translate("Form", u"Confirmar nova senha", None))
        self.ln_conf_nova_senha.setText("")
        self.ln_conf_nova_senha.setPlaceholderText("")
    # retranslateUi

