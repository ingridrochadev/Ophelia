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
    QPushButton, QSizePolicy, QWidget)
import logo_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(494, 620)
        Form.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0.584, y1:0.466045, x2:1, y2:1, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(153, 0, 255, 255));")
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(90, 260, 331, 271))
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setStyleSheet(u"background-color: rgba(0,0,0,0.3)")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.email_line = QLineEdit(self.frame_2)
        self.email_line.setObjectName(u"email_line")
        self.email_line.setGeometry(QRect(20, 40, 300, 30))
        self.email_line.setMinimumSize(QSize(300, 30))
        font = QFont()
        font.setPointSize(11)
        self.email_line.setFont(font)
        self.email_line.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255,255,255);\n"
"border-color:rgb(255,255,255);\n"
"border-width: 1px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:5px; /* Define o estilo da borda como s\u00f3lido */\n"
"}")
        self.email_line.setAlignment(Qt.AlignCenter)
        self.senha_line = QLineEdit(self.frame_2)
        self.senha_line.setObjectName(u"senha_line")
        self.senha_line.setGeometry(QRect(20, 90, 300, 31))
        self.senha_line.setMinimumSize(QSize(300, 30))
        self.senha_line.setFont(font)
        self.senha_line.setStyleSheet(u"QLineEdit{\n"
"color: rgb(255,255,255);\n"
"border-color:rgb(255,255,255);\n"
"border-width: 1px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:5px; /* Define o estilo da borda como s\u00f3lido */\n"
"}")
        self.senha_line.setEchoMode(QLineEdit.Password)
        self.senha_line.setAlignment(Qt.AlignCenter)
        self.btn_entrar = QPushButton(self.frame_2)
        self.btn_entrar.setObjectName(u"btn_entrar")
        self.btn_entrar.setGeometry(QRect(70, 190, 200, 40))
        self.btn_entrar.setMinimumSize(QSize(200, 40))
        font1 = QFont()
        font1.setPointSize(12)
        self.btn_entrar.setFont(font1)
        self.btn_entrar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_entrar.setStyleSheet(u"QPushButton{\n"
"background-color:rgb(0,0,0);\n"
"color:rgb(255,255,255);\n"
"border-radius: 10px;\n"
"}\n"
"\n"
"QPushButton::hoover{\n"
"background-color:rgb(255,255,255);\n"
"color:rgb(0,0,0);\n"
"border-radius: 10px;\n"
"}")
        self.label = QLabel(Form)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(140, 40, 231, 221))
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setStyleSheet(u"        QFrame {\n"
"            background-color: rgba(231, 231, 231, 0); /* Define a cor de fundo como transparente */\n"
"        }")
        self.label.setPixmap(QPixmap(u":/logo/pages/icons/logo_nome_branco.png"))
        self.label.setScaledContents(True)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.email_line.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.senha_line.setPlaceholderText(QCoreApplication.translate("Form", u"Senha", None))
        self.btn_entrar.setText(QCoreApplication.translate("Form", u"Entrar", None))
        self.label.setText("")
    # retranslateUi

