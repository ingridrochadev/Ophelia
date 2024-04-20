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
from PySide6.QtWidgets import (QApplication, QFormLayout, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(982, 620)
        MainWindow.setStyleSheet(u"background-color: rgb(102, 0, 185);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(400, 600))
        self.label_4.setMaximumSize(QSize(10000, 16777215))
        self.label_4.setStyleSheet(u"image: url(:img/Ophelia purple.png);\n"
"background-color: rgb(249, 249, 249);")

        self.horizontalLayout.addWidget(self.label_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(50, 150, -1, -1)
        self.bemvindo = QLabel(self.centralwidget)
        self.bemvindo.setObjectName(u"bemvindo")
        self.bemvindo.setMinimumSize(QSize(0, 0))
        self.bemvindo.setMaximumSize(QSize(16777215, 200))
        self.bemvindo.setSizeIncrement(QSize(0, 0))
        self.bemvindo.setLayoutDirection(Qt.LeftToRight)
        self.bemvindo.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")

        self.verticalLayout.addWidget(self.bemvindo)

        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.login = QHBoxLayout()
        self.login.setObjectName(u"login")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_2.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.login.addWidget(self.label_2)


        self.formLayout.setLayout(0, QFormLayout.LabelRole, self.login)

        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(100, 20))
        self.lineEdit.setMaximumSize(QSize(200, 20))
        self.lineEdit.setBaseSize(QSize(0, 0))
        self.lineEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.lineEdit.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.formLayout.setWidget(0, QFormLayout.FieldRole, self.lineEdit)

        self.senha = QHBoxLayout()
        self.senha.setObjectName(u"senha")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"color: rgb(255, 255, 255);\n"
"")
        self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.senha.addWidget(self.label_3)


        self.formLayout.setLayout(1, QFormLayout.LabelRole, self.senha)

        self.lineEdit_2 = QLineEdit(self.centralwidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMinimumSize(QSize(100, 20))
        self.lineEdit_2.setMaximumSize(QSize(200, 20))
        self.lineEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(1, QFormLayout.FieldRole, self.lineEdit_2)

        self.botoes = QHBoxLayout()
        self.botoes.setObjectName(u"botoes")

        self.formLayout.setLayout(2, QFormLayout.LabelRole, self.botoes)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(100, 20))
        self.pushButton.setMaximumSize(QSize(100, 16777215))
        self.pushButton.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.formLayout.setWidget(2, QFormLayout.FieldRole, self.pushButton)


        self.verticalLayout.addLayout(self.formLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_4.setText("")
        self.bemvindo.setText(QCoreApplication.translate("MainWindow", u"Bem-vindo(a)", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite seu login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.lineEdit_2.setText("")
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Digite sua senha", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Entrar", None))
    # retranslateUi

