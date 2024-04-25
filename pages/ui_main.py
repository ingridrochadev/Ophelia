# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'cadastro.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QComboBox, QFrame,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPlainTextEdit, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QTableWidget, QTableWidgetItem,
    QToolBox, QVBoxLayout, QWidget)
import pages.logo_rc as logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1286, 794)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(115, 0, 200, 255));")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"border:none;\n"
"}\n"
"QLabel{\n"
"	color:rgb(255, 255, 255);\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 9, 0, 9)
        self.left_container = QFrame(self.centralwidget)
        self.left_container.setObjectName(u"left_container")
        self.left_container.setMinimumSize(QSize(9, 0))
        self.left_container.setMaximumSize(QSize(200, 16777215))
        self.left_container.setFrameShape(QFrame.StyledPanel)
        self.left_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.left_container)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(4, 4, 4, 4)
        self.frame = QFrame(self.left_container)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.txt_bemvindo = QLabel(self.frame)
        self.txt_bemvindo.setObjectName(u"txt_bemvindo")
        font = QFont()
        font.setFamilies([u"Lato"])
        font.setPointSize(11)
        font.setBold(True)
        self.txt_bemvindo.setFont(font)

        self.horizontalLayout_3.addWidget(self.txt_bemvindo)


        self.verticalLayout_3.addWidget(self.frame)

        self.frame_2 = QFrame(self.left_container)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.frame_2.setStyleSheet(u"QFrame{\n"
"background-color: rgb(30, 0, 50);\n"
"border-radius: 8px;\n"
"text-color: rgb(255,255,255)\n"
"}\n"
"\n"
"QToolBox{\n"
"text-align: left;\n"
"background-color: rgb(100,00,150);\n"
"text-color: rgb(255,255,255)\n"
"}\n"
"\n"
"QToolBox::tab{\n"
"border-radius: 5px;\n"
"text-align: left;\n"
"background-color: rgb(255,255,255);\n"
"text-color: rgb(255,255,255)\n"
"}")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(6, 6, 6, 6)
        self.toolBox = QToolBox(self.frame_2)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setMinimumSize(QSize(0, 30))
        font1 = QFont()
        font1.setPointSize(11)
        self.toolBox.setFont(font1)
        self.toolBox.setStyleSheet(u"QPushButton:hover {\n"
"    background-color: rgb(65, 65, 65);\n"
"    border-top-left-radius: 15px;\n"
"}\n"
"\n"
"QPushButton{\n"
"color:rgb(255,255,255);\n"
"font-family: \"Lato Black\", sans-serif;\n"
"font-weight: bold\n"
"}")
        self.Vistos = QWidget()
        self.Vistos.setObjectName(u"Vistos")
        self.Vistos.setGeometry(QRect(0, 0, 180, 658))
        self.verticalLayout_5 = QVBoxLayout(self.Vistos)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.btn_home = QPushButton(self.Vistos)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 30))
        font2 = QFont()
        font2.setFamilies([u"Lato Black"])
        font2.setPointSize(11)
        font2.setBold(True)
        self.btn_home.setFont(font2)
        self.btn_home.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_home)

        self.btn_add = QPushButton(self.Vistos)
        self.btn_add.setObjectName(u"btn_add")
        self.btn_add.setMinimumSize(QSize(0, 30))
        self.btn_add.setFont(font2)
        self.btn_add.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_add)

        self.btn_listar = QPushButton(self.Vistos)
        self.btn_listar.setObjectName(u"btn_listar")
        self.btn_listar.setMinimumSize(QSize(0, 30))
        self.btn_listar.setFont(font2)
        self.btn_listar.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_listar)

        self.btn_alterar_visto = QPushButton(self.Vistos)
        self.btn_alterar_visto.setObjectName(u"btn_alterar_visto")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(30)
        sizePolicy1.setHeightForWidth(self.btn_alterar_visto.sizePolicy().hasHeightForWidth())
        self.btn_alterar_visto.setSizePolicy(sizePolicy1)
        self.btn_alterar_visto.setMinimumSize(QSize(0, 30))
        self.btn_alterar_visto.setFont(font2)

        self.verticalLayout_5.addWidget(self.btn_alterar_visto)

        self.btn_sobre = QPushButton(self.Vistos)
        self.btn_sobre.setObjectName(u"btn_sobre")
        self.btn_sobre.setMinimumSize(QSize(0, 30))
        self.btn_sobre.setFont(font2)
        self.btn_sobre.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout_5.addWidget(self.btn_sobre)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_5.addItem(self.verticalSpacer)

        self.toolBox.addItem(self.Vistos, u"Vistos")
        self.Usuario = QWidget()
        self.Usuario.setObjectName(u"Usuario")
        self.Usuario.setGeometry(QRect(0, 0, 180, 658))
        self.verticalLayout_9 = QVBoxLayout(self.Usuario)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_inserir_user = QPushButton(self.Usuario)
        self.btn_inserir_user.setObjectName(u"btn_inserir_user")
        self.btn_inserir_user.setMinimumSize(QSize(0, 30))
        self.btn_inserir_user.setFont(font2)

        self.verticalLayout_9.addWidget(self.btn_inserir_user)

        self.btn_listar_usuarios = QPushButton(self.Usuario)
        self.btn_listar_usuarios.setObjectName(u"btn_listar_usuarios")
        self.btn_listar_usuarios.setMinimumSize(QSize(0, 30))
        self.btn_listar_usuarios.setFont(font2)

        self.verticalLayout_9.addWidget(self.btn_listar_usuarios)

        self.btn_alterar_usuario = QPushButton(self.Usuario)
        self.btn_alterar_usuario.setObjectName(u"btn_alterar_usuario")
        self.btn_alterar_usuario.setMinimumSize(QSize(0, 30))
        self.btn_alterar_usuario.setFont(font2)

        self.verticalLayout_9.addWidget(self.btn_alterar_usuario)

        self.btn_alterar_senha_2 = QPushButton(self.Usuario)
        self.btn_alterar_senha_2.setObjectName(u"btn_alterar_senha_2")
        self.btn_alterar_senha_2.setMinimumSize(QSize(0, 30))
        self.btn_alterar_senha_2.setFont(font2)

        self.verticalLayout_9.addWidget(self.btn_alterar_senha_2)

        self.btn_logout = QPushButton(self.Usuario)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(0, 30))
        self.btn_logout.setFont(font2)

        self.verticalLayout_9.addWidget(self.btn_logout)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_9.addItem(self.verticalSpacer_2)

        self.toolBox.addItem(self.Usuario, u"Usu\u00e1rio")

        self.verticalLayout_4.addWidget(self.toolBox)


        self.verticalLayout_3.addWidget(self.frame_2)


        self.horizontalLayout.addWidget(self.left_container)

        self.main_container = QFrame(self.centralwidget)
        self.main_container.setObjectName(u"main_container")
        self.main_container.setFrameShape(QFrame.StyledPanel)
        self.main_container.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.main_container)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.top_frame = QFrame(self.main_container)
        self.top_frame.setObjectName(u"top_frame")
        self.top_frame.setFrameShape(QFrame.StyledPanel)
        self.top_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.top_frame)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(self.top_frame)
        self.label.setObjectName(u"label")
        font3 = QFont()
        font3.setFamilies([u"Lato"])
        font3.setPointSize(11)
        self.label.setFont(font3)
        self.label.setStyleSheet(u"QLineEdit {\n"
"    font: 10pt \"Lato Regular\";\n"
"}")

        self.horizontalLayout_2.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)


        self.verticalLayout.addWidget(self.top_frame)

        self.main_frame = QFrame(self.main_container)
        self.main_frame.setObjectName(u"main_frame")
        sizePolicy.setHeightForWidth(self.main_frame.sizePolicy().hasHeightForWidth())
        self.main_frame.setSizePolicy(sizePolicy)
        self.main_frame.setFrameShape(QFrame.StyledPanel)
        self.main_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.main_frame)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Pages = QStackedWidget(self.main_frame)
        self.Pages.setObjectName(u"Pages")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.Pages.sizePolicy().hasHeightForWidth())
        self.Pages.setSizePolicy(sizePolicy2)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")
        self.logo.setPixmap(QPixmap(u":/icons/icons/logo_nome_branco.png"))
        self.logo.setScaledContents(False)
        self.logo.setAlignment(Qt.AlignCenter)

        self.verticalLayout_7.addWidget(self.logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_adicionar = QWidget()
        self.pg_adicionar.setObjectName(u"pg_adicionar")
        self.frame_4 = QFrame(self.pg_adicionar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(2, 1, 971, 651))
        sizePolicy2.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy2)
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"background-color: #F4E7FF;\n"
"font: 11pt \"Lato Heavy\"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:white;\n"
"border-radius:10px;\n"
"}")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.frame_13 = QFrame(self.frame_4)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setGeometry(QRect(9, 9, 941, 311))
        self.frame_13.setMinimumSize(QSize(400, 0))
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setStyleSheet(u"QFrame{\n"
"background-color:#F4E7FF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: white ;\n"
"font: 11pt \"Lato Heavy\"\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.btn_ler = QPushButton(self.frame_13)
        self.btn_ler.setObjectName(u"btn_ler")
        self.btn_ler.setGeometry(QRect(370, 270, 200, 35))
        sizePolicy2.setHeightForWidth(self.btn_ler.sizePolicy().hasHeightForWidth())
        self.btn_ler.setSizePolicy(sizePolicy2)
        self.btn_ler.setMinimumSize(QSize(200, 35))
        self.btn_ler.setMaximumSize(QSize(200, 35))
        self.btn_ler.setSizeIncrement(QSize(0, 1))
        font4 = QFont()
        font4.setFamilies([u"Lato Bold"])
        font4.setPointSize(11)
        self.btn_ler.setFont(font4)
        self.btn_ler.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ler.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(210, 210, 210);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: purple;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/icons/Icon (1) (c\u00f3pia).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ler.setIcon(icon)
        self.btn_ler.setIconSize(QSize(30, 30))
        self.img_space = QLabel(self.frame_13)
        self.img_space.setObjectName(u"img_space")
        self.img_space.setGeometry(QRect(270, 10, 401, 251))
        self.img_space.setMinimumSize(QSize(0, 0))
        self.img_space.setMaximumSize(QSize(16777215, 16777215))
        self.img_space.setStyleSheet(u"frame-radius:10px;")
        self.frame_23 = QFrame(self.frame_4)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setGeometry(QRect(20, 330, 927, 301))
        sizePolicy2.setHeightForWidth(self.frame_23.sizePolicy().hasHeightForWidth())
        self.frame_23.setSizePolicy(sizePolicy2)
        self.frame_23.setMinimumSize(QSize(0, 0))
        self.frame_23.setMaximumSize(QSize(16777215, 350))
        font5 = QFont()
        font5.setBold(False)
        self.frame_23.setFont(font5)
        self.frame_23.setMouseTracking(False)
        self.frame_23.setStyleSheet(u"QFrame {\n"
"    border-radius: 4px\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(80,80,80);\n"
"    font-size: 14px;\n"
"font:\"Lato Heavy\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.frame_23.setFrameShape(QFrame.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Raised)
        self.nacionalidade_line = QLineEdit(self.frame_23)
        self.nacionalidade_line.setObjectName(u"nacionalidade_line")
        self.nacionalidade_line.setGeometry(QRect(100, 90, 340, 30))
        self.nacionalidade_line.setMinimumSize(QSize(340, 30))
        self.nacionalidade_line.setMaximumSize(QSize(500, 30))
        self.lbl_nacionalidade_3 = QLabel(self.frame_23)
        self.lbl_nacionalidade_3.setObjectName(u"lbl_nacionalidade_3")
        self.lbl_nacionalidade_3.setGeometry(QRect(100, 70, 100, 17))
        self.date_nasc_line = QLineEdit(self.frame_23)
        self.date_nasc_line.setObjectName(u"date_nasc_line")
        self.date_nasc_line.setGeometry(QRect(480, 30, 340, 30))
        self.date_nasc_line.setMinimumSize(QSize(340, 30))
        self.date_nasc_line.setMaximumSize(QSize(500, 30))
        self.lbl_nome_3 = QLabel(self.frame_23)
        self.lbl_nome_3.setObjectName(u"lbl_nome_3")
        self.lbl_nome_3.setGeometry(QRect(100, 10, 42, 17))
        self.lbl_passaporte_3 = QLabel(self.frame_23)
        self.lbl_passaporte_3.setObjectName(u"lbl_passaporte_3")
        self.lbl_passaporte_3.setGeometry(QRect(480, 70, 77, 17))
        self.lbl_city = QLabel(self.frame_23)
        self.lbl_city.setObjectName(u"lbl_city")
        self.lbl_city.setGeometry(QRect(100, 130, 117, 17))
        self.lbl_tipo_visto_3 = QLabel(self.frame_23)
        self.lbl_tipo_visto_3.setObjectName(u"lbl_tipo_visto_3")
        self.lbl_tipo_visto_3.setGeometry(QRect(100, 190, 90, 17))
        self.tipo_visto_line = QLineEdit(self.frame_23)
        self.tipo_visto_line.setObjectName(u"tipo_visto_line")
        self.tipo_visto_line.setGeometry(QRect(100, 210, 340, 30))
        self.tipo_visto_line.setMinimumSize(QSize(340, 30))
        self.tipo_visto_line.setMaximumSize(QSize(500, 30))
        self.tipo_visto_line.setClearButtonEnabled(False)
        self.city_line = QLineEdit(self.frame_23)
        self.city_line.setObjectName(u"city_line")
        self.city_line.setGeometry(QRect(100, 150, 340, 30))
        self.city_line.setMinimumSize(QSize(340, 30))
        self.city_line.setMaximumSize(QSize(500, 30))
        self.lbl_exp_3 = QLabel(self.frame_23)
        self.lbl_exp_3.setObjectName(u"lbl_exp_3")
        self.lbl_exp_3.setGeometry(QRect(480, 130, 120, 17))
        self.nome_line = QLineEdit(self.frame_23)
        self.nome_line.setObjectName(u"nome_line")
        self.nome_line.setGeometry(QRect(100, 30, 340, 30))
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(20)
        sizePolicy3.setHeightForWidth(self.nome_line.sizePolicy().hasHeightForWidth())
        self.nome_line.setSizePolicy(sizePolicy3)
        self.nome_line.setMinimumSize(QSize(340, 30))
        self.nome_line.setMaximumSize(QSize(500, 30))
        font6 = QFont()
        font6.setFamilies([u"Lato Heavy"])
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        self.nome_line.setFont(font6)
        self.nome_line.setLayoutDirection(Qt.LeftToRight)
        self.nome_line.setStyleSheet(u"")
        self.lbl_dob_3 = QLabel(self.frame_23)
        self.lbl_dob_3.setObjectName(u"lbl_dob_3")
        self.lbl_dob_3.setGeometry(QRect(480, 10, 151, 17))
        self.passport_line = QLineEdit(self.frame_23)
        self.passport_line.setObjectName(u"passport_line")
        self.passport_line.setGeometry(QRect(480, 90, 340, 30))
        self.passport_line.setMinimumSize(QSize(340, 30))
        self.passport_line.setMaximumSize(QSize(500, 30))
        self.validade_line = QLineEdit(self.frame_23)
        self.validade_line.setObjectName(u"validade_line")
        self.validade_line.setGeometry(QRect(480, 150, 340, 30))
        self.validade_line.setMinimumSize(QSize(340, 30))
        self.validade_line.setMaximumSize(QSize(500, 30))
        self.num_visto_line = QLineEdit(self.frame_23)
        self.num_visto_line.setObjectName(u"num_visto_line")
        self.num_visto_line.setGeometry(QRect(480, 210, 340, 30))
        self.num_visto_line.setMinimumSize(QSize(340, 30))
        self.num_visto_line.setMaximumSize(QSize(500, 30))
        self.lbl_num_visto_3 = QLabel(self.frame_23)
        self.lbl_num_visto_3.setObjectName(u"lbl_num_visto_3")
        self.lbl_num_visto_3.setGeometry(QRect(480, 190, 116, 17))
        self.btn_add_2 = QPushButton(self.frame_23)
        self.btn_add_2.setObjectName(u"btn_add_2")
        self.btn_add_2.setGeometry(QRect(389, 260, 150, 35))
        self.btn_add_2.setMinimumSize(QSize(150, 35))
        self.btn_add_2.setMaximumSize(QSize(200, 35))
        self.btn_add_2.setFont(font4)
        self.btn_add_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_add_2.setAutoFillBackground(False)
        self.btn_add_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(210, 210, 210);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: purple;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        self.Pages.addWidget(self.pg_adicionar)
        self.pg_listar = QWidget()
        self.pg_listar.setObjectName(u"pg_listar")
        self.frame_5 = QFrame(self.pg_listar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setEnabled(True)
        self.frame_5.setGeometry(QRect(0, 0, 980, 651))
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setMaximumSize(QSize(980, 659))
        self.frame_5.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-radius:8px;\n"
"}")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.tbl_vistos = QTableWidget(self.frame_5)
        if (self.tbl_vistos.columnCount() < 3):
            self.tbl_vistos.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tbl_vistos.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tbl_vistos.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tbl_vistos.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tbl_vistos.setObjectName(u"tbl_vistos")
        self.tbl_vistos.setGeometry(QRect(10, 130, 841, 511))
        sizePolicy2.setHeightForWidth(self.tbl_vistos.sizePolicy().hasHeightForWidth())
        self.tbl_vistos.setSizePolicy(sizePolicy2)
        self.tbl_vistos.setStyleSheet(u"QHeaderView::section{\n"
"background-color:purple;\n"
"color:white;\n"
"color:#fff;\n"
"font-size: 15px;\n"
"}\n"
"QTableWidget{\n"
"background-color:rgb(252, 252, 252);\n"
"color:#430B78;\n"
"border:2px solid purple;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color: purple;\n"
"    height: 15px;\n"
"    margin: 2px 2px 0 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(230,230,230); \n"
"    min-width: 15px; \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background: none; /* Remove o bot\u00e3o de rolagem para baixo */\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none; /* Remove o bot\u00e3o de rolagem para cima */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: purple;\n"
"    height: 15px;\n"
"    margin: 2px 2px 0 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(230,230,230); \n"
"    min-width: 15px; \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"    background: none; /* Remove o b"
                        "ot\u00e3o de rolagem para baixo */\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: none; /* Remove o bot\u00e3o de rolagem para cima */\n"
"}")
        self.tbl_vistos.horizontalHeader().setDefaultSectionSize(274)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(859, 130, 111, 511))
        self.frame_7.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 15px;\n"
"    font-family: \"Lato heavy\", sans-serif;\n"
"    color: purple;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"    font-family: \"Lato Bold\", sans-serif;\n"
"    color: #fff;\n"
"    font-size: 15px; /* Defina o tamanho da fonte desejado */\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(230,230,230);\n"
"border-radius: 4px;\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_listar_vistos = QPushButton(self.frame_7)
        self.btn_listar_vistos.setObjectName(u"btn_listar_vistos")
        self.btn_listar_vistos.setMinimumSize(QSize(0, 30))
        self.btn_listar_vistos.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_listar_vistos.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.btn_listar_vistos)

        self.btn_exportar = QPushButton(self.frame_7)
        self.btn_exportar.setObjectName(u"btn_exportar")
        self.btn_exportar.setMinimumSize(QSize(0, 30))
        self.btn_exportar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportar.setStyleSheet(u"")

        self.verticalLayout_12.addWidget(self.btn_exportar)

        self.btn_excluir = QPushButton(self.frame_7)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 15px;\n"
"    font-family: \"Lato heavy\", sans-serif;\n"
"    color: purple;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"    font-family: \"Lato Bold\", sans-serif;\n"
"    color: #fff;\n"
"    font-size: 15px; /* Defina o tamanho da fonte desejado */\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_excluir)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.frame_22 = QFrame(self.frame_5)
        self.frame_22.setObjectName(u"frame_22")
        self.frame_22.setGeometry(QRect(10, 10, 961, 111))
        self.frame_22.setMinimumSize(QSize(400, 60))
        self.frame_22.setStyleSheet(u"QFrame{\n"
"background-color:#F4E7FF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: white ;\n"
"font: 11pt \"Lato Heavy\"\n"
"}")
        self.frame_22.setFrameShape(QFrame.StyledPanel)
        self.frame_22.setFrameShadow(QFrame.Raised)
        self.ttl_vistos = QLabel(self.frame_22)
        self.ttl_vistos.setObjectName(u"ttl_vistos")
        self.ttl_vistos.setGeometry(QRect(280, 20, 401, 51))
        font7 = QFont()
        font7.setFamilies([u"Lato Heavy"])
        font7.setPointSize(11)
        font7.setBold(False)
        font7.setItalic(False)
        font7.setKerning(True)
        self.ttl_vistos.setFont(font7)
        self.ttl_vistos.setLayoutDirection(Qt.LeftToRight)
        self.ttl_vistos.setStyleSheet(u"background-color: transparent;\n"
"color:purple;\n"
"border-radius:10px;")
        self.ttl_vistos.setLineWidth(1)
        self.ttl_vistos.setAlignment(Qt.AlignCenter)
        self.ttl_vistos.setIndent(-1)
        self.cb_perfil_2 = QComboBox(self.frame_22)
        self.cb_perfil_2.addItem("")
        self.cb_perfil_2.addItem("")
        self.cb_perfil_2.addItem("")
        self.cb_perfil_2.setObjectName(u"cb_perfil_2")
        self.cb_perfil_2.setGeometry(QRect(10, 70, 231, 30))
        self.cb_perfil_2.setMaximumSize(QSize(16777215, 35))
        font8 = QFont()
        font8.setPointSize(10)
        font8.setBold(False)
        font8.setItalic(False)
        self.cb_perfil_2.setFont(font8)
        self.cb_perfil_2.setStyleSheet(u"color:rgb(80,80,80);\n"
"background-color:white;\n"
"border: 2px solid purple;\n"
"border-radius:5px;\n"
"font: \"Lato Heavy\"")
        self.cb_perfil_2.setIconSize(QSize(16, 16))
        self.cb_aprovados = QCheckBox(self.frame_22)
        self.cb_aprovados.setObjectName(u"cb_aprovados")
        self.cb_aprovados.setGeometry(QRect(800, 80, 151, 21))
        self.cb_aprovados.setStyleSheet(u"QCheckBox {\n"
"    background-color: #F4E7FF; /* Define a cor de fundo */\n"
"    color: purple; /* Define a cor do texto */\n"
"    font-family: Lato; /* Define a fonte */\n"
"    font-size: 15px; /* Define o tamanho da fonte */\n"
"    font-weight: bold; /* Define a fonte em negrito */\n"
"}")
        self.checkBox_2 = QCheckBox(self.frame_22)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setGeometry(QRect(650, 80, 141, 21))
        self.checkBox_2.setStyleSheet(u"QCheckBox {\n"
"    background-color: #F4E7FF; /* Define a cor de fundo */\n"
"    color: purple; /* Define a cor do texto */\n"
"    font-family: Lato; /* Define a fonte */\n"
"    font-size: 15px; /* Define o tamanho da fonte */\n"
"    font-weight: bold; /* Define a fonte em negrito */\n"
"}\n"
"\n"
"")
        self.frame_22.raise_()
        self.tbl_vistos.raise_()
        self.frame_7.raise_()
        self.Pages.addWidget(self.pg_listar)
        self.pg_alterar_visto = QWidget()
        self.pg_alterar_visto.setObjectName(u"pg_alterar_visto")
        self.frame_16 = QFrame(self.pg_alterar_visto)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setGeometry(QRect(0, 0, 971, 651))
        self.frame_16.setStyleSheet(u"QLineEdit{\n"
"background-color: #F4E7FF;\n"
"font: 11pt \"Lato Heavy\"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:white;\n"
"border-radius:10px;\n"
"}")
        self.frame_16.setFrameShape(QFrame.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_16)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMinimumSize(QSize(400, 60))
        self.frame_17.setStyleSheet(u"QFrame{\n"
"background-color:#F4E7FF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: white ;\n"
"font: 11pt \"Lato Heavy\"\n"
"}")
        self.frame_17.setFrameShape(QFrame.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Raised)
        self.frame_10 = QFrame(self.frame_17)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(280, 80, 381, 41))
        self.frame_10.setStyleSheet(u"QFrame{\n"
"background-color: white;\n"
"border-radius:5px;\n"
"}\n"
"QLine Edit{\n"
"background-color: white;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"background-color: white;\n"
"border-radius:5px;\n"
"}")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.search_ln = QLineEdit(self.frame_10)
        self.search_ln.setObjectName(u"search_ln")
        self.search_ln.setGeometry(QRect(0, 0, 341, 40))
        self.search_ln.setMinimumSize(QSize(340, 40))
        self.search_ln.setMaximumSize(QSize(800, 16777215))
        self.search_ln.setStyleSheet(u"background-color: white;\n"
"border-radius:5px;")
        self.search_ln.setClearButtonEnabled(False)
        self.search_btn = QPushButton(self.frame_10)
        self.search_btn.setObjectName(u"search_btn")
        self.search_btn.setGeometry(QRect(350, 2, 31, 41))
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/Icon (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.search_btn.setIcon(icon1)
        self.search_btn.setIconSize(QSize(22, 22))
        self.ttl_vistos_2 = QLabel(self.frame_17)
        self.ttl_vistos_2.setObjectName(u"ttl_vistos_2")
        self.ttl_vistos_2.setGeometry(QRect(260, 20, 421, 51))
        self.ttl_vistos_2.setFont(font7)
        self.ttl_vistos_2.setLayoutDirection(Qt.LeftToRight)
        self.ttl_vistos_2.setStyleSheet(u"background-color: transparent;\n"
"color:purple;\n"
"border-radius:10px;")
        self.ttl_vistos_2.setLineWidth(1)
        self.ttl_vistos_2.setAlignment(Qt.AlignCenter)
        self.ttl_vistos_2.setIndent(-1)

        self.verticalLayout_6.addWidget(self.frame_17)

        self.frame_18 = QFrame(self.frame_16)
        self.frame_18.setObjectName(u"frame_18")
        sizePolicy2.setHeightForWidth(self.frame_18.sizePolicy().hasHeightForWidth())
        self.frame_18.setSizePolicy(sizePolicy2)
        self.frame_18.setMaximumSize(QSize(16777215, 470))
        self.frame_18.setFont(font5)
        self.frame_18.setMouseTracking(False)
        self.frame_18.setStyleSheet(u"QFrame {\n"
"    border-radius: 4px\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(80,80,80);\n"
"    font-size: 14px;\n"
"font:\"Lato Heavy\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.frame_18.setFrameShape(QFrame.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Raised)
        self.nacionalidade_line_2 = QLineEdit(self.frame_18)
        self.nacionalidade_line_2.setObjectName(u"nacionalidade_line_2")
        self.nacionalidade_line_2.setGeometry(QRect(530, 50, 340, 40))
        self.nacionalidade_line_2.setMinimumSize(QSize(340, 40))
        self.nacionalidade_line_2.setMaximumSize(QSize(500, 16777215))
        self.lbl_nacionalidade_2 = QLabel(self.frame_18)
        self.lbl_nacionalidade_2.setObjectName(u"lbl_nacionalidade_2")
        self.lbl_nacionalidade_2.setGeometry(QRect(530, 30, 100, 17))
        self.date_nasc_line_2 = QLineEdit(self.frame_18)
        self.date_nasc_line_2.setObjectName(u"date_nasc_line_2")
        self.date_nasc_line_2.setGeometry(QRect(70, 120, 340, 40))
        self.date_nasc_line_2.setMinimumSize(QSize(340, 40))
        self.date_nasc_line_2.setMaximumSize(QSize(500, 16777215))
        self.lbl_nome_2 = QLabel(self.frame_18)
        self.lbl_nome_2.setObjectName(u"lbl_nome_2")
        self.lbl_nome_2.setGeometry(QRect(70, 30, 42, 17))
        self.lbl_passaporte_2 = QLabel(self.frame_18)
        self.lbl_passaporte_2.setObjectName(u"lbl_passaporte_2")
        self.lbl_passaporte_2.setGeometry(QRect(530, 100, 77, 17))
        self.lbl_city_2 = QLabel(self.frame_18)
        self.lbl_city_2.setObjectName(u"lbl_city_2")
        self.lbl_city_2.setGeometry(QRect(530, 240, 117, 17))
        self.lbl_tipo_visto_2 = QLabel(self.frame_18)
        self.lbl_tipo_visto_2.setObjectName(u"lbl_tipo_visto_2")
        self.lbl_tipo_visto_2.setGeometry(QRect(70, 170, 90, 17))
        self.city_line_2 = QLineEdit(self.frame_18)
        self.city_line_2.setObjectName(u"city_line_2")
        self.city_line_2.setGeometry(QRect(530, 260, 340, 40))
        self.city_line_2.setMinimumSize(QSize(340, 40))
        self.city_line_2.setMaximumSize(QSize(500, 16777215))
        self.city_line_2.setClearButtonEnabled(False)
        self.tipo_visto_line_3 = QLineEdit(self.frame_18)
        self.tipo_visto_line_3.setObjectName(u"tipo_visto_line_3")
        self.tipo_visto_line_3.setGeometry(QRect(70, 190, 340, 40))
        self.tipo_visto_line_3.setMinimumSize(QSize(340, 40))
        self.tipo_visto_line_3.setMaximumSize(QSize(500, 16777215))
        self.lbl_exp_2 = QLabel(self.frame_18)
        self.lbl_exp_2.setObjectName(u"lbl_exp_2")
        self.lbl_exp_2.setGeometry(QRect(70, 240, 120, 17))
        self.nome_line_2 = QLineEdit(self.frame_18)
        self.nome_line_2.setObjectName(u"nome_line_2")
        self.nome_line_2.setGeometry(QRect(70, 50, 340, 40))
        self.nome_line_2.setMinimumSize(QSize(340, 40))
        self.nome_line_2.setMaximumSize(QSize(500, 16777215))
        self.nome_line_2.setFont(font6)
        self.nome_line_2.setLayoutDirection(Qt.LeftToRight)
        self.nome_line_2.setStyleSheet(u"")
        self.lbl_dob_2 = QLabel(self.frame_18)
        self.lbl_dob_2.setObjectName(u"lbl_dob_2")
        self.lbl_dob_2.setGeometry(QRect(70, 100, 151, 17))
        self.passport_line_2 = QLineEdit(self.frame_18)
        self.passport_line_2.setObjectName(u"passport_line_2")
        self.passport_line_2.setGeometry(QRect(530, 120, 340, 40))
        self.passport_line_2.setMinimumSize(QSize(340, 40))
        self.passport_line_2.setMaximumSize(QSize(500, 16777215))
        self.validade_line_2 = QLineEdit(self.frame_18)
        self.validade_line_2.setObjectName(u"validade_line_2")
        self.validade_line_2.setGeometry(QRect(70, 260, 340, 40))
        self.validade_line_2.setMinimumSize(QSize(340, 40))
        self.validade_line_2.setMaximumSize(QSize(500, 16777215))
        self.num_visto_line_2 = QLineEdit(self.frame_18)
        self.num_visto_line_2.setObjectName(u"num_visto_line_2")
        self.num_visto_line_2.setGeometry(QRect(530, 190, 340, 40))
        self.num_visto_line_2.setMinimumSize(QSize(340, 40))
        self.num_visto_line_2.setMaximumSize(QSize(500, 16777215))
        self.lbl_num_visto_2 = QLabel(self.frame_18)
        self.lbl_num_visto_2.setObjectName(u"lbl_num_visto_2")
        self.lbl_num_visto_2.setGeometry(QRect(530, 170, 116, 17))
        self.alterar_pax_btn = QPushButton(self.frame_18)
        self.alterar_pax_btn.setObjectName(u"alterar_pax_btn")
        self.alterar_pax_btn.setGeometry(QRect(630, 410, 200, 35))
        self.alterar_pax_btn.setMinimumSize(QSize(180, 35))
        self.alterar_pax_btn.setMaximumSize(QSize(200, 35))
        self.alterar_pax_btn.setFont(font4)
        self.alterar_pax_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.alterar_pax_btn.setLayoutDirection(Qt.LeftToRight)
        self.alterar_pax_btn.setAutoFillBackground(False)
        self.alterar_pax_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220, 220, 220);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: purple;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        self.excluir_pax_btn = QPushButton(self.frame_18)
        self.excluir_pax_btn.setObjectName(u"excluir_pax_btn")
        self.excluir_pax_btn.setGeometry(QRect(80, 410, 160, 35))
        self.excluir_pax_btn.setMinimumSize(QSize(160, 35))
        self.excluir_pax_btn.setMaximumSize(QSize(160, 28))
        self.excluir_pax_btn.setFont(font4)
        self.excluir_pax_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.excluir_pax_btn.setLayoutDirection(Qt.LeftToRight)
        self.excluir_pax_btn.setAutoFillBackground(False)
        self.excluir_pax_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"    color:purple;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        self.status_embarque_line = QLineEdit(self.frame_18)
        self.status_embarque_line.setObjectName(u"status_embarque_line")
        self.status_embarque_line.setGeometry(QRect(340, 340, 250, 40))
        self.status_embarque_line.setMinimumSize(QSize(250, 0))
        self.status_embarque_line.setMaximumSize(QSize(250, 16777215))
        self.status_embarque_line.setStyleSheet(u"background-color: rgb(231, 190, 244);")
        self.status_embarque_line.setClearButtonEnabled(False)
        self.lbl_city_3 = QLabel(self.frame_18)
        self.lbl_city_3.setObjectName(u"lbl_city_3")
        self.lbl_city_3.setGeometry(QRect(390, 320, 161, 17))
        font9 = QFont()
        font9.setBold(False)
        font9.setItalic(False)
        self.lbl_city_3.setFont(font9)
        self.lbl_city_3.setAlignment(Qt.AlignCenter)

        self.verticalLayout_6.addWidget(self.frame_18)

        self.Pages.addWidget(self.pg_alterar_visto)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.frame_3 = QFrame(self.page)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(-1, -1, 971, 651))
        self.frame_3.setStyleSheet(u"QLineEdit{\n"
"background-color: #F4E7FF;\n"
"font: 11pt \"Lato Heavy\"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:white;\n"
"border-radius:10px;\n"
"}")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.frame_6 = QFrame(self.frame_3)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setGeometry(QRect(0, 0, 971, 651))
        self.frame_6.setStyleSheet(u"QLineEdit{\n"
"background-color: #F4E7FF;\n"
"font: 11pt \"Lato Heavy\"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:white;\n"
"border-radius:10px;\n"
"}")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.txt_sobre = QLabel(self.frame_6)
        self.txt_sobre.setObjectName(u"txt_sobre")
        self.txt_sobre.setGeometry(QRect(180, 120, 611, 210))
        sizePolicy.setHeightForWidth(self.txt_sobre.sizePolicy().hasHeightForWidth())
        self.txt_sobre.setSizePolicy(sizePolicy)
        self.txt_sobre.setMinimumSize(QSize(0, 210))
        self.txt_sobre.setMaximumSize(QSize(800, 16777215))
        font10 = QFont()
        font10.setFamilies([u"Lato"])
        font10.setPointSize(15)
        font10.setBold(False)
        font10.setItalic(False)
        self.txt_sobre.setFont(font10)
        self.txt_sobre.setStyleSheet(u"color:purple;")
        self.txt_sobre.setAlignment(Qt.AlignCenter)
        self.txt_sobre.setWordWrap(True)
        self.txt_desenvolvedoras = QLabel(self.frame_6)
        self.txt_desenvolvedoras.setObjectName(u"txt_desenvolvedoras")
        self.txt_desenvolvedoras.setGeometry(QRect(300, 270, 371, 400))
        self.txt_desenvolvedoras.setMinimumSize(QSize(0, 400))
        self.txt_desenvolvedoras.setMaximumSize(QSize(800, 400))
        font11 = QFont()
        font11.setFamilies([u"Lato"])
        font11.setPointSize(25)
        font11.setBold(False)
        font11.setItalic(False)
        self.txt_desenvolvedoras.setFont(font11)
        self.txt_desenvolvedoras.setStyleSheet(u"color:purple;\n"
"background-color:transparent;")
        self.label_6 = QLabel(self.frame_6)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(-250, -180, 411, 391))
        self.label_6.setPixmap(QPixmap(u":/icons/icons/logo_roxa.png"))
        self.label_6.setScaledContents(True)
        self.ttl_sobre = QLabel(self.frame_6)
        self.ttl_sobre.setObjectName(u"ttl_sobre")
        self.ttl_sobre.setGeometry(QRect(400, 40, 161, 71))
        self.ttl_sobre.setMinimumSize(QSize(100, 30))
        font12 = QFont()
        font12.setFamilies([u"Lato"])
        font12.setPointSize(16)
        font12.setBold(False)
        font12.setItalic(False)
        self.ttl_sobre.setFont(font12)
        self.ttl_sobre.setAutoFillBackground(False)
        self.ttl_sobre.setStyleSheet(u"color:purple;")
        self.label_3 = QLabel(self.frame_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(690, 400, 411, 391))
        self.label_3.setPixmap(QPixmap(u":/icons/icons/logo_roxa.png"))
        self.label_3.setScaledContents(True)
        self.Pages.addWidget(self.page)
        self.pg_inserir_user = QWidget()
        self.pg_inserir_user.setObjectName(u"pg_inserir_user")
        self.frame_9 = QFrame(self.pg_inserir_user)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 971, 651))
        self.frame_9.setStyleSheet(u"QLineEdit{\n"
"background-color: #F4E7FF;\n"
"font: 11pt \"Lato Heavy\"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:white;\n"
"border-radius:10px;\n"
"}")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(460, 70, 451, 501))
        self.frame_14.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-color:#F4E7FF;\n"
"border-width:5px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color:purple;\n"
"    background-color: transparent;\n"
"    border-bottom: 2px solid purple; /* Adiciona uma borda somente na parte inferior */\n"
"	font-family: \"Lato Heavy\", serif;\n"
"    font-size: 16px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.matricula_line = QLineEdit(self.frame_14)
        self.matricula_line.setObjectName(u"matricula_line")
        self.matricula_line.setGeometry(QRect(70, 210, 350, 40))
        self.matricula_line.setMinimumSize(QSize(350, 40))
        self.matricula_line.setMaximumSize(QSize(350, 16777215))
        self.cpf_line = QLineEdit(self.frame_14)
        self.cpf_line.setObjectName(u"cpf_line")
        self.cpf_line.setGeometry(QRect(70, 160, 350, 40))
        self.cpf_line.setMinimumSize(QSize(350, 40))
        self.cpf_line.setMaximumSize(QSize(350, 16777215))
        self.senha_add_user_ln = QLineEdit(self.frame_14)
        self.senha_add_user_ln.setObjectName(u"senha_add_user_ln")
        self.senha_add_user_ln.setGeometry(QRect(70, 310, 350, 40))
        self.senha_add_user_ln.setMinimumSize(QSize(350, 40))
        self.senha_add_user_ln.setMaximumSize(QSize(350, 16777215))
        self.senha_add_user_ln.setEchoMode(QLineEdit.Password)
        self.nome_user_line = QLineEdit(self.frame_14)
        self.nome_user_line.setObjectName(u"nome_user_line")
        self.nome_user_line.setGeometry(QRect(70, 110, 350, 40))
        self.nome_user_line.setMinimumSize(QSize(350, 40))
        self.nome_user_line.setMaximumSize(QSize(350, 16777215))
        font13 = QFont()
        font13.setFamilies([u"Lato Heavy"])
        font13.setBold(False)
        font13.setItalic(False)
        self.nome_user_line.setFont(font13)
        self.nome_user_line.setLayoutDirection(Qt.LeftToRight)
        self.nome_user_line.setStyleSheet(u"QFrame {\n"
"    background-color: purple;\n"
"    border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.email_user_line = QLineEdit(self.frame_14)
        self.email_user_line.setObjectName(u"email_user_line")
        self.email_user_line.setGeometry(QRect(70, 260, 350, 40))
        self.email_user_line.setMinimumSize(QSize(350, 40))
        self.email_user_line.setMaximumSize(QSize(350, 16777215))
        self.btn_add_user = QPushButton(self.frame_14)
        self.btn_add_user.setObjectName(u"btn_add_user")
        self.btn_add_user.setGeometry(QRect(120, 390, 250, 40))
        self.btn_add_user.setMinimumSize(QSize(250, 40))
        self.btn_add_user.setMaximumSize(QSize(250, 40))
        font14 = QFont()
        font14.setFamilies([u"Lato Bold"])
        font14.setPointSize(15)
        self.btn_add_user.setFont(font14)
        self.btn_add_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_user.setLayoutDirection(Qt.LeftToRight)
        self.btn_add_user.setAutoFillBackground(False)
        self.btn_add_user.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(210, 210, 210);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: purple;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        self.lbl_perfil = QLabel(self.frame_14)
        self.lbl_perfil.setObjectName(u"lbl_perfil")
        self.lbl_perfil.setGeometry(QRect(60, 50, 111, 40))
        self.lbl_perfil.setMinimumSize(QSize(0, 35))
        self.lbl_perfil.setStyleSheet(u"color:purple;\n"
"font-family: \"Lato Heavy\", serif;\n"
"font-size: 16px;\n"
"border:2px solid white;")
        self.cb_perfil = QComboBox(self.frame_14)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setGeometry(QRect(170, 50, 241, 30))
        self.cb_perfil.setMaximumSize(QSize(16777215, 35))
        self.cb_perfil.setFont(font1)
        self.cb_perfil.setStyleSheet(u"QComboBox {\n"
"color:rgb(70,70,70);\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 1px solid purple;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"color: purple;\n"
"width: 16px; /* Largura da seta */\n"
"height: 16px; /* Altura da seta */\n"
"}")
        self.frame_19 = QFrame(self.frame_9)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setGeometry(QRect(60, 30, 451, 591))
        self.frame_19.setStyleSheet(u"QFrame{\n"
"background-color:#F4E7FF;\n"
"border-color:#F4E7FF;\n"
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
        self.frame_19.setFrameShape(QFrame.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_19)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 130, 411, 441))
        self.label_4.setPixmap(QPixmap(u":/icons/icons/Black Minimalist Outline Icons Icon Set.png"))
        self.label_4.setScaledContents(True)
        self.plainTextEdit_2 = QPlainTextEdit(self.frame_19)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(10, 10, 361, 131))
        font15 = QFont()
        font15.setFamilies([u"Lato"])
        font15.setPointSize(32)
        font15.setBold(True)
        self.plainTextEdit_2.setFont(font15)
        self.plainTextEdit_2.setStyleSheet(u"color: purple;")
        self.Pages.addWidget(self.pg_inserir_user)
        self.pg_listar_user = QWidget()
        self.pg_listar_user.setObjectName(u"pg_listar_user")
        self.frame_28 = QFrame(self.pg_listar_user)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setGeometry(QRect(0, 0, 971, 651))
        self.frame_28.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-radius:8px;\n"
"}")
        self.frame_28.setFrameShape(QFrame.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Raised)
        self.frame_8 = QFrame(self.frame_28)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setEnabled(True)
        self.frame_8.setGeometry(QRect(10, 10, 940, 640))
        sizePolicy2.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy2)
        self.frame_8.setMaximumSize(QSize(940, 640))
        self.frame_8.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-radius:8px;\n"
"}")
        self.frame_8.setFrameShape(QFrame.NoFrame)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.tbl_vistos_2 = QTableWidget(self.frame_8)
        if (self.tbl_vistos_2.columnCount() < 3):
            self.tbl_vistos_2.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tbl_vistos_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tbl_vistos_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignLeading|Qt.AlignVCenter);
        self.tbl_vistos_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tbl_vistos_2.setObjectName(u"tbl_vistos_2")
        self.tbl_vistos_2.setGeometry(QRect(10, 120, 811, 511))
        sizePolicy2.setHeightForWidth(self.tbl_vistos_2.sizePolicy().hasHeightForWidth())
        self.tbl_vistos_2.setSizePolicy(sizePolicy2)
        self.tbl_vistos_2.setStyleSheet(u"QHeaderView::section{\n"
"background-color:purple;\n"
"color:white;\n"
"color:#fff;\n"
"font-size: 15px;\n"
"}\n"
"QTableWidget{\n"
"background-color:rgb(252, 252, 252);\n"
"color:#430B78;\n"
"border:2px solid purple;\n"
"}\n"
"QScrollBar:vertical {\n"
"    background-color: purple;\n"
"    height: 15px;\n"
"    margin: 2px 2px 0 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:vertical {\n"
"    background-color: rgb(230,230,230); \n"
"    min-width: 15px; \n"
"}\n"
"\n"
"QScrollBar::add-line:vertical {\n"
"    background: none; /* Remove o bot\u00e3o de rolagem para baixo */\n"
"}\n"
"\n"
"QScrollBar::sub-line:vertical {\n"
"    background: none; /* Remove o bot\u00e3o de rolagem para cima */\n"
"}\n"
"\n"
"QScrollBar:horizontal {\n"
"    background-color: purple;\n"
"    height: 15px;\n"
"    margin: 2px 2px 0 2px;\n"
"}\n"
"\n"
"QScrollBar::handle:horizontal {\n"
"    background-color: rgb(230,230,230); \n"
"    min-width: 15px; \n"
"}\n"
"\n"
"QScrollBar::add-line:horizontal{\n"
"    background: none; /* Remove o b"
                        "ot\u00e3o de rolagem para baixo */\n"
"}\n"
"\n"
"QScrollBar::sub-line:horizontal {\n"
"    background: none; /* Remove o bot\u00e3o de rolagem para cima */\n"
"}")
        self.tbl_vistos_2.horizontalHeader().setDefaultSectionSize(274)
        self.frame_12 = QFrame(self.frame_8)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(830, 120, 111, 511))
        self.frame_12.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 15px;\n"
"    font-family: \"Lato heavy\", sans-serif;\n"
"    color: purple;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"    font-family: \"Lato Bold\", sans-serif;\n"
"    color: #fff;\n"
"    font-size: 15px; /* Defina o tamanho da fonte desejado */\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(230,230,230);\n"
"border-radius: 4px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_12)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.btn_listar_vistos_2 = QPushButton(self.frame_12)
        self.btn_listar_vistos_2.setObjectName(u"btn_listar_vistos_2")
        self.btn_listar_vistos_2.setMinimumSize(QSize(0, 30))
        self.btn_listar_vistos_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_listar_vistos_2.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_listar_vistos_2)

        self.btn_exportar_2 = QPushButton(self.frame_12)
        self.btn_exportar_2.setObjectName(u"btn_exportar_2")
        self.btn_exportar_2.setMinimumSize(QSize(0, 30))
        self.btn_exportar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportar_2.setStyleSheet(u"")

        self.verticalLayout_13.addWidget(self.btn_exportar_2)

        self.btn_alterar_user = QPushButton(self.frame_12)
        self.btn_alterar_user.setObjectName(u"btn_alterar_user")
        self.btn_alterar_user.setMinimumSize(QSize(0, 30))
        self.btn_alterar_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_user.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 15px;\n"
"    font-family: \"Lato heavy\", sans-serif;\n"
"    color: purple;\n"
"    font-size: 15px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"    font-family: \"Lato Bold\", sans-serif;\n"
"    color: #fff;\n"
"    font-size: 15px; /* Defina o tamanho da fonte desejado */\n"
"}")

        self.verticalLayout_13.addWidget(self.btn_alterar_user)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_13.addItem(self.verticalSpacer_4)

        self.frame_27 = QFrame(self.frame_8)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setGeometry(QRect(10, 0, 931, 111))
        self.frame_27.setMinimumSize(QSize(400, 60))
        self.frame_27.setStyleSheet(u"QFrame{\n"
"background-color:#F4E7FF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: white ;\n"
"font: 11pt \"Lato Heavy\"\n"
"}")
        self.frame_27.setFrameShape(QFrame.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Raised)
        self.ttl_vistos_4 = QLabel(self.frame_27)
        self.ttl_vistos_4.setObjectName(u"ttl_vistos_4")
        self.ttl_vistos_4.setGeometry(QRect(260, 20, 401, 51))
        self.ttl_vistos_4.setFont(font7)
        self.ttl_vistos_4.setLayoutDirection(Qt.LeftToRight)
        self.ttl_vistos_4.setStyleSheet(u"background-color: transparent;\n"
"color:purple;\n"
"border-radius:10px;")
        self.ttl_vistos_4.setLineWidth(1)
        self.ttl_vistos_4.setAlignment(Qt.AlignCenter)
        self.ttl_vistos_4.setIndent(-1)
        self.cb_perfil_listar = QComboBox(self.frame_27)
        self.cb_perfil_listar.addItem("")
        self.cb_perfil_listar.addItem("")
        self.cb_perfil_listar.addItem("")
        self.cb_perfil_listar.setObjectName(u"cb_perfil_listar")
        self.cb_perfil_listar.setGeometry(QRect(10, 70, 231, 30))
        self.cb_perfil_listar.setMaximumSize(QSize(16777215, 35))
        self.cb_perfil_listar.setFont(font8)
        self.cb_perfil_listar.setStyleSheet(u"color:rgb(80,80,80);\n"
"background-color:white;\n"
"border: 2px solid purple;\n"
"border-radius:5px;\n"
"font: \"Lato Heavy\"")
        self.cb_perfil_listar.setIconSize(QSize(16, 16))
        self.cb_agentes = QCheckBox(self.frame_27)
        self.cb_agentes.setObjectName(u"cb_agentes")
        self.cb_agentes.setGeometry(QRect(790, 80, 151, 21))
        self.cb_agentes.setStyleSheet(u"QCheckBox {\n"
"    background-color: #F4E7FF; /* Define a cor de fundo */\n"
"    color: purple; /* Define a cor do texto */\n"
"    font-family: Lato; /* Define a fonte */\n"
"    font-size: 15px; /* Define o tamanho da fonte */\n"
"    font-weight: bold; /* Define a fonte em negrito */\n"
"}")
        self.cb_supervisores = QCheckBox(self.frame_27)
        self.cb_supervisores.setObjectName(u"cb_supervisores")
        self.cb_supervisores.setGeometry(QRect(610, 80, 171, 21))
        self.cb_supervisores.setStyleSheet(u"QCheckBox {\n"
"    background-color: #F4E7FF; /* Define a cor de fundo */\n"
"    color: purple; /* Define a cor do texto */\n"
"    font-family: Lato; /* Define a fonte */\n"
"    font-size: 15px; /* Define o tamanho da fonte */\n"
"    font-weight: bold; /* Define a fonte em negrito */\n"
"}\n"
"\n"
"")
        self.Pages.addWidget(self.pg_listar_user)
        self.pg_alterar_user = QWidget()
        self.pg_alterar_user.setObjectName(u"pg_alterar_user")
        self.frame_24 = QFrame(self.pg_alterar_user)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setGeometry(QRect(0, 0, 971, 651))
        self.frame_24.setStyleSheet(u"QLineEdit{\n"
"background-color: #F4E7FF;\n"
"font: 11pt \"Lato Heavy\"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:white;\n"
"border-radius:10px;\n"
"}")
        self.frame_24.setFrameShape(QFrame.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_24)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.frame_25 = QFrame(self.frame_24)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMinimumSize(QSize(400, 60))
        self.frame_25.setStyleSheet(u"QFrame{\n"
"background-color:#F4E7FF;\n"
"border-radius:10px;\n"
"}\n"
"\n"
"QLabel{\n"
"background-color: white ;\n"
"font: 11pt \"Lato Heavy\"\n"
"}")
        self.frame_25.setFrameShape(QFrame.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Raised)
        self.frame_11 = QFrame(self.frame_25)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setGeometry(QRect(280, 80, 381, 41))
        self.frame_11.setStyleSheet(u"QFrame{\n"
"background-color: white;\n"
"border-radius:5px;\n"
"}\n"
"QLine Edit{\n"
"background-color: white;\n"
"border-radius:5px;\n"
"}\n"
"QPushButton{\n"
"background-color: white;\n"
"border-radius:5px;\n"
"}")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.search_ln_2 = QLineEdit(self.frame_11)
        self.search_ln_2.setObjectName(u"search_ln_2")
        self.search_ln_2.setGeometry(QRect(0, 0, 341, 40))
        self.search_ln_2.setMinimumSize(QSize(340, 40))
        self.search_ln_2.setMaximumSize(QSize(800, 16777215))
        self.search_ln_2.setStyleSheet(u"background-color: white;\n"
"border-radius:5px;")
        self.search_ln_2.setClearButtonEnabled(False)
        self.search_btn_2 = QPushButton(self.frame_11)
        self.search_btn_2.setObjectName(u"search_btn_2")
        self.search_btn_2.setGeometry(QRect(350, 2, 31, 41))
        self.search_btn_2.setIcon(icon1)
        self.search_btn_2.setIconSize(QSize(22, 22))
        self.ttl_vistos_3 = QLabel(self.frame_25)
        self.ttl_vistos_3.setObjectName(u"ttl_vistos_3")
        self.ttl_vistos_3.setGeometry(QRect(300, 20, 341, 51))
        self.ttl_vistos_3.setFont(font7)
        self.ttl_vistos_3.setLayoutDirection(Qt.LeftToRight)
        self.ttl_vistos_3.setStyleSheet(u"background-color: transparent;\n"
"color:purple;\n"
"border-radius:10px;")
        self.ttl_vistos_3.setLineWidth(1)
        self.ttl_vistos_3.setAlignment(Qt.AlignCenter)
        self.ttl_vistos_3.setIndent(-1)

        self.verticalLayout_8.addWidget(self.frame_25)

        self.frame_26 = QFrame(self.frame_24)
        self.frame_26.setObjectName(u"frame_26")
        sizePolicy2.setHeightForWidth(self.frame_26.sizePolicy().hasHeightForWidth())
        self.frame_26.setSizePolicy(sizePolicy2)
        self.frame_26.setMaximumSize(QSize(16777215, 470))
        self.frame_26.setFont(font5)
        self.frame_26.setMouseTracking(False)
        self.frame_26.setStyleSheet(u"QFrame {\n"
"    border-radius: 4px\n"
"}\n"
"\n"
"QLabel {\n"
"    color: rgb(80,80,80);\n"
"    font-size: 14px;\n"
"font:\"Lato Heavy\";\n"
"}\n"
"\n"
"QLineEdit{\n"
"border-radius:5px;\n"
"}")
        self.frame_26.setFrameShape(QFrame.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Raised)
        self.alterar_user_btn = QPushButton(self.frame_26)
        self.alterar_user_btn.setObjectName(u"alterar_user_btn")
        self.alterar_user_btn.setGeometry(QRect(510, 390, 200, 35))
        self.alterar_user_btn.setMinimumSize(QSize(180, 35))
        self.alterar_user_btn.setMaximumSize(QSize(200, 35))
        self.alterar_user_btn.setFont(font4)
        self.alterar_user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.alterar_user_btn.setLayoutDirection(Qt.LeftToRight)
        self.alterar_user_btn.setAutoFillBackground(False)
        self.alterar_user_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220, 220, 220);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: purple;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        self.excluir_user_btn = QPushButton(self.frame_26)
        self.excluir_user_btn.setObjectName(u"excluir_user_btn")
        self.excluir_user_btn.setGeometry(QRect(240, 390, 200, 35))
        self.excluir_user_btn.setMinimumSize(QSize(200, 35))
        self.excluir_user_btn.setMaximumSize(QSize(200, 28))
        self.excluir_user_btn.setFont(font4)
        self.excluir_user_btn.setCursor(QCursor(Qt.PointingHandCursor))
        self.excluir_user_btn.setLayoutDirection(Qt.LeftToRight)
        self.excluir_user_btn.setAutoFillBackground(False)
        self.excluir_user_btn.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(220,220,220);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"    color:purple;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        self.lbl_perfil_2 = QLabel(self.frame_26)
        self.lbl_perfil_2.setObjectName(u"lbl_perfil_2")
        self.lbl_perfil_2.setGeometry(QRect(300, 320, 111, 40))
        self.lbl_perfil_2.setMinimumSize(QSize(0, 35))
        self.lbl_perfil_2.setStyleSheet(u"color:purple;\n"
"font-family: \"Lato Heavy\", serif;\n"
"font-size: 16px;\n"
"border:2px solid white;")
        self.cb_perfil_alterar = QComboBox(self.frame_26)
        self.cb_perfil_alterar.addItem("")
        self.cb_perfil_alterar.addItem("")
        self.cb_perfil_alterar.setObjectName(u"cb_perfil_alterar")
        self.cb_perfil_alterar.setGeometry(QRect(410, 320, 241, 30))
        self.cb_perfil_alterar.setMaximumSize(QSize(16777215, 35))
        self.cb_perfil_alterar.setFont(font1)
        self.cb_perfil_alterar.setStyleSheet(u"QComboBox {\n"
"color:rgb(70,70,70);\n"
"background-color:white;\n"
"border-radius:5px;\n"
"border: 1px solid purple;\n"
"}\n"
"\n"
"QComboBox::down-arrow {\n"
"color: purple;\n"
"width: 16px; /* Largura da seta */\n"
"height: 16px; /* Altura da seta */\n"
"}")
        self.nome_user_line_2 = QLineEdit(self.frame_26)
        self.nome_user_line_2.setObjectName(u"nome_user_line_2")
        self.nome_user_line_2.setGeometry(QRect(300, 20, 350, 40))
        self.nome_user_line_2.setMinimumSize(QSize(350, 40))
        self.nome_user_line_2.setMaximumSize(QSize(350, 16777215))
        self.nome_user_line_2.setFont(font6)
        self.nome_user_line_2.setLayoutDirection(Qt.LeftToRight)
        self.nome_user_line_2.setStyleSheet(u"QFrame {\n"
"    background-color: purple;\n"
"    border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.cpf_line_2 = QLineEdit(self.frame_26)
        self.cpf_line_2.setObjectName(u"cpf_line_2")
        self.cpf_line_2.setGeometry(QRect(300, 80, 350, 40))
        self.cpf_line_2.setMinimumSize(QSize(350, 40))
        self.cpf_line_2.setMaximumSize(QSize(350, 16777215))
        self.matricula_line_2 = QLineEdit(self.frame_26)
        self.matricula_line_2.setObjectName(u"matricula_line_2")
        self.matricula_line_2.setGeometry(QRect(300, 140, 350, 40))
        self.matricula_line_2.setMinimumSize(QSize(350, 40))
        self.matricula_line_2.setMaximumSize(QSize(350, 16777215))
        self.email_user_line_2 = QLineEdit(self.frame_26)
        self.email_user_line_2.setObjectName(u"email_user_line_2")
        self.email_user_line_2.setGeometry(QRect(300, 200, 350, 40))
        self.email_user_line_2.setMinimumSize(QSize(350, 40))
        self.email_user_line_2.setMaximumSize(QSize(350, 16777215))
        self.senha_add_user_ln_2 = QLineEdit(self.frame_26)
        self.senha_add_user_ln_2.setObjectName(u"senha_add_user_ln_2")
        self.senha_add_user_ln_2.setGeometry(QRect(300, 260, 350, 40))
        self.senha_add_user_ln_2.setMinimumSize(QSize(350, 40))
        self.senha_add_user_ln_2.setMaximumSize(QSize(350, 16777215))
        self.senha_add_user_ln_2.setEchoMode(QLineEdit.Password)

        self.verticalLayout_8.addWidget(self.frame_26)

        self.Pages.addWidget(self.pg_alterar_user)
        self.pg_alterar_senha = QWidget()
        self.pg_alterar_senha.setObjectName(u"pg_alterar_senha")
        self.frame_15 = QFrame(self.pg_alterar_senha)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 0, 971, 651))
        self.frame_15.setStyleSheet(u"QLineEdit{\n"
"background-color: #F4E7FF;\n"
"font: 11pt \"Lato Heavy\"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color:white;\n"
"border-radius:10px;\n"
"}")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.frame_20 = QFrame(self.frame_15)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setGeometry(QRect(80, 40, 431, 561))
        self.frame_20.setStyleSheet(u"QFrame{\n"
"background-color:#F4E7FF;\n"
"border-color:#F4E7FF;\n"
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
        self.frame_20.setFrameShape(QFrame.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_20)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(10, 110, 411, 441))
        self.label_5.setPixmap(QPixmap(u":/icons/icons/Black Minimalist Outline Icons Icon Set (1).png"))
        self.label_5.setScaledContents(True)
        self.plainTextEdit_3 = QPlainTextEdit(self.frame_20)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(10, 10, 411, 131))
        self.plainTextEdit_3.setFont(font15)
        self.plainTextEdit_3.setStyleSheet(u"color: purple;")
        self.frame_21 = QFrame(self.frame_15)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setGeometry(QRect(460, 80, 411, 481))
        self.frame_21.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-color:#F4E7FF;\n"
"border-width:5px; /* Define a largura da borda para 2 pixels */\n"
"border-style: solid;\n"
"border-radius:10px; /* Define o estilo da borda como s\u00f3lido */\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color:purple;\n"
"    background-color: transparent;\n"
"    border-bottom: 2px solid purple; /* Adiciona uma borda somente na parte inferior */\n"
"	font-family: \"Lato Heavy\", serif;\n"
"    font-size: 16px;\n"
"}")
        self.frame_21.setFrameShape(QFrame.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Raised)
        self.emial_line = QLineEdit(self.frame_21)
        self.emial_line.setObjectName(u"emial_line")
        self.emial_line.setGeometry(QRect(70, 110, 315, 40))
        self.emial_line.setMinimumSize(QSize(0, 40))
        self.emial_line.setStyleSheet(u"QFrame {\n"
"    background-color: purple;\n"
"    border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.emial_line.setAlignment(Qt.AlignCenter)
        self.senha_atual_line = QLineEdit(self.frame_21)
        self.senha_atual_line.setObjectName(u"senha_atual_line")
        self.senha_atual_line.setGeometry(QRect(70, 160, 315, 40))
        self.senha_atual_line.setMinimumSize(QSize(0, 40))
        self.senha_atual_line.setEchoMode(QLineEdit.Password)
        self.senha_atual_line.setAlignment(Qt.AlignCenter)
        self.senha_line = QLineEdit(self.frame_21)
        self.senha_line.setObjectName(u"senha_line")
        self.senha_line.setGeometry(QRect(70, 210, 315, 40))
        self.senha_line.setMinimumSize(QSize(0, 40))
        self.senha_line.setEchoMode(QLineEdit.Password)
        self.senha_line.setAlignment(Qt.AlignCenter)
        self.senha_line_2 = QLineEdit(self.frame_21)
        self.senha_line_2.setObjectName(u"senha_line_2")
        self.senha_line_2.setGeometry(QRect(70, 260, 315, 40))
        self.senha_line_2.setMinimumSize(QSize(0, 40))
        self.senha_line_2.setEchoMode(QLineEdit.Password)
        self.senha_line_2.setAlignment(Qt.AlignCenter)
        self.btn_alterar_senha = QPushButton(self.frame_21)
        self.btn_alterar_senha.setObjectName(u"btn_alterar_senha")
        self.btn_alterar_senha.setGeometry(QRect(140, 380, 200, 35))
        self.btn_alterar_senha.setMinimumSize(QSize(200, 35))
        self.btn_alterar_senha.setMaximumSize(QSize(200, 16777215))
        self.btn_alterar_senha.setFont(font4)
        self.btn_alterar_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_senha.setLayoutDirection(Qt.LeftToRight)
        self.btn_alterar_senha.setAutoFillBackground(False)
        self.btn_alterar_senha.setStyleSheet(u"QPushButton {\n"
"	Color:purple;\n"
"    background-color: rgb(220, 220, 220);\n"
"    border-radius: 17px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 20px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        self.frame_21.raise_()
        self.frame_20.raise_()
        self.Pages.addWidget(self.pg_alterar_senha)

        self.horizontalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.footer_frame.sizePolicy().hasHeightForWidth())
        self.footer_frame.setSizePolicy(sizePolicy4)
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        font16 = QFont()
        font16.setFamilies([u"Lato"])
        font16.setBold(True)
        self.label_2.setFont(font16)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)
        self.Pages.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_bemvindo.setText(QCoreApplication.translate("MainWindow", u"Bem-vindo(a), {nome_usuario}!", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Adicionar Visto", None))
        self.btn_listar.setText(QCoreApplication.translate("MainWindow", u"Listar Vistos", None))
        self.btn_alterar_visto.setText(QCoreApplication.translate("MainWindow", u"Alterar Visto", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Vistos), QCoreApplication.translate("MainWindow", u"Vistos", None))
        self.btn_inserir_user.setText(QCoreApplication.translate("MainWindow", u"Inserir Usu\u00e1rio", None))
        self.btn_listar_usuarios.setText(QCoreApplication.translate("MainWindow", u"Listar Usu\u00e1rios", None))
        self.btn_alterar_usuario.setText(QCoreApplication.translate("MainWindow", u"Alterar Usu\u00e1rio", None))
        self.btn_alterar_senha_2.setText(QCoreApplication.translate("MainWindow", u"Alterar Senha", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Usuario), QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de leitura de Documentos de Viagem", None))
        self.logo.setText("")
        self.btn_ler.setText(QCoreApplication.translate("MainWindow", u"Carregar Visto", None))
        self.img_space.setText("")
        self.nacionalidade_line.setText("")
        self.nacionalidade_line.setPlaceholderText("")
        self.lbl_nacionalidade_3.setText(QCoreApplication.translate("MainWindow", u"Nacionalidade", None))
        self.date_nasc_line.setPlaceholderText("")
        self.lbl_nome_3.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_passaporte_3.setText(QCoreApplication.translate("MainWindow", u"Passaporte", None))
        self.lbl_city.setText(QCoreApplication.translate("MainWindow", u"Cidade emitente", None))
        self.lbl_tipo_visto_3.setText(QCoreApplication.translate("MainWindow", u"Tipo de visto", None))
        self.tipo_visto_line.setPlaceholderText("")
        self.city_line.setText("")
        self.city_line.setPlaceholderText("")
        self.lbl_exp_3.setText(QCoreApplication.translate("MainWindow", u"Validade do visto", None))
        self.nome_line.setText("")
        self.nome_line.setPlaceholderText("")
        self.lbl_dob_3.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento  ", None))
        self.passport_line.setPlaceholderText("")
        self.validade_line.setPlaceholderText("")
        self.num_visto_line.setPlaceholderText("")
        self.lbl_num_visto_3.setText(QCoreApplication.translate("MainWindow", u"N\u00famero do visto", None))
        self.btn_add_2.setText(QCoreApplication.translate("MainWindow", u"     Adicionar     ", None))
        ___qtablewidgetitem = self.tbl_vistos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tbl_vistos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Passaporte", None));
        ___qtablewidgetitem2 = self.tbl_vistos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status Embarque", None));
        self.btn_listar_vistos.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
        self.btn_exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.ttl_vistos.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lato'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">PASSAGEIROS</span></p></body></html>", None))
        self.cb_perfil_2.setItemText(0, QCoreApplication.translate("MainWindow", u"Ordenar por:", None))
        self.cb_perfil_2.setItemText(1, QCoreApplication.translate("MainWindow", u"                     A-Z", None))
        self.cb_perfil_2.setItemText(2, QCoreApplication.translate("MainWindow", u"                     Z-A", None))

        self.cb_aprovados.setText(QCoreApplication.translate("MainWindow", u"Apenas Aprovados", None))
        self.checkBox_2.setText(QCoreApplication.translate("MainWindow", u"Apenas Negados", None))
        self.search_ln.setText("")
        self.search_ln.setPlaceholderText(QCoreApplication.translate("MainWindow", u" N\u00famero do passaporte", None))
        self.search_btn.setText("")
        self.ttl_vistos_2.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lato'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">ALTERAR PASSAGEIROS</span></p></body></html>", None))
        self.nacionalidade_line_2.setText("")
        self.nacionalidade_line_2.setPlaceholderText("")
        self.lbl_nacionalidade_2.setText(QCoreApplication.translate("MainWindow", u"Nacionalidade", None))
        self.date_nasc_line_2.setPlaceholderText("")
        self.lbl_nome_2.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_passaporte_2.setText(QCoreApplication.translate("MainWindow", u"Passaporte", None))
        self.lbl_city_2.setText(QCoreApplication.translate("MainWindow", u"Cidade emitente", None))
        self.lbl_tipo_visto_2.setText(QCoreApplication.translate("MainWindow", u"Tipo de visto", None))
        self.city_line_2.setPlaceholderText("")
        self.tipo_visto_line_3.setText("")
        self.tipo_visto_line_3.setPlaceholderText("")
        self.lbl_exp_2.setText(QCoreApplication.translate("MainWindow", u"Validade do visto", None))
        self.nome_line_2.setPlaceholderText("")
        self.lbl_dob_2.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento  ", None))
        self.passport_line_2.setPlaceholderText("")
        self.validade_line_2.setPlaceholderText("")
        self.num_visto_line_2.setPlaceholderText("")
        self.lbl_num_visto_2.setText(QCoreApplication.translate("MainWindow", u"N\u00famero do visto", None))
        self.alterar_pax_btn.setText(QCoreApplication.translate("MainWindow", u"Alterar passageiro", None))
        self.excluir_pax_btn.setText(QCoreApplication.translate("MainWindow", u"Excluir Passageiro", None))
        self.status_embarque_line.setPlaceholderText("")
        self.lbl_city_3.setText(QCoreApplication.translate("MainWindow", u"Status de Embarque", None))
        self.txt_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt;\">Esse sistema l\u00ea os dados do visto e, al\u00e9m de salv\u00e1-los para envio \u00e0 imigra\u00e7\u00e3o dos EUA por parte da companhia a\u00e9rea, ele tamb\u00e9m emite um alerta para o agente de aeroporto informando se o passageiro est\u00e1 apto a viajar com aquele visto ou se \u00e9 necess\u00e1rio alguma documenta\u00e7\u00e3o extra.</span></p></body></html>", None))
        self.txt_desenvolvedoras.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">DESENVOLVEDORAS:</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">BIANCA YURI</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">DJULLIE CAROLINE</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">INGRID ROCHA</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">TAYNARA MORAIS</span></p><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">YASMIM FERREIRA</span></p></body></html>", None))
        self.label_6.setText("")
        self.ttl_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">SOBRE</span></p></body></html>", None))
        self.label_3.setText("")
        self.matricula_line.setText("")
        self.matricula_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.cpf_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.senha_add_user_ln.setText("")
        self.senha_add_user_ln.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.nome_user_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.email_user_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.btn_add_user.setText(QCoreApplication.translate("MainWindow", u"Adicionar Usu\u00e1rio", None))
        self.lbl_perfil.setText(QCoreApplication.translate("MainWindow", u"Tipo de Perfil", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Agente de Aeroporto", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Supervisor", None))

        self.label_4.setText("")
        self.plainTextEdit_2.setPlainText(QCoreApplication.translate("MainWindow", u"CADASTRAR USU\u00c1RIO", None))
        ___qtablewidgetitem3 = self.tbl_vistos_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem4 = self.tbl_vistos_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None));
        ___qtablewidgetitem5 = self.tbl_vistos_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Fun\u00e7\u00e3o", None));
        self.btn_listar_vistos_2.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
        self.btn_exportar_2.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.btn_alterar_user.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.ttl_vistos_4.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lato'; font-size:14pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">COLABORADORES</span></p></body></html>", None))
        self.cb_perfil_listar.setItemText(0, QCoreApplication.translate("MainWindow", u"Ordenar por:", None))
        self.cb_perfil_listar.setItemText(1, QCoreApplication.translate("MainWindow", u"                     A-Z", None))
        self.cb_perfil_listar.setItemText(2, QCoreApplication.translate("MainWindow", u"                     Z-A", None))

        self.cb_agentes.setText(QCoreApplication.translate("MainWindow", u"Apenas Agentes", None))
        self.cb_supervisores.setText(QCoreApplication.translate("MainWindow", u"Apenas Supervisores", None))
        self.search_ln_2.setText("")
        self.search_ln_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Matr\u00edcula do colaborador", None))
        self.search_btn_2.setText("")
        self.ttl_vistos_3.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lato'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">ALTERAR USU\u00c1RIO</span></p></body></html>", None))
        self.alterar_user_btn.setText(QCoreApplication.translate("MainWindow", u"Alterar Usu\u00e1rio", None))
        self.excluir_user_btn.setText(QCoreApplication.translate("MainWindow", u"Excluir Usu\u00e1rio", None))
        self.lbl_perfil_2.setText(QCoreApplication.translate("MainWindow", u"Tipo de Perfil", None))
        self.cb_perfil_alterar.setItemText(0, QCoreApplication.translate("MainWindow", u"Agente de Aeroporto", None))
        self.cb_perfil_alterar.setItemText(1, QCoreApplication.translate("MainWindow", u"Supervisor", None))

        self.nome_user_line_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Nome", None))
        self.cpf_line_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" CPF", None))
        self.matricula_line_2.setText("")
        self.matricula_line_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Matr\u00edcula", None))
        self.email_user_line_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Email", None))
        self.senha_add_user_ln_2.setText("")
        self.senha_add_user_ln_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u" Senha", None))
        self.label_5.setText("")
        self.plainTextEdit_3.setPlainText(QCoreApplication.translate("MainWindow", u"ALTERAR SENHA", None))
        self.emial_line.setText("")
        self.emial_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.senha_atual_line.setText("")
        self.senha_atual_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha Atual", None))
        self.senha_line.setText("")
        self.senha_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nova Senha", None))
        self.senha_line_2.setText("")
        self.senha_line_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmar Senha", None))
        self.btn_alterar_senha.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Ophelia 2024", None))
    # retranslateUi

