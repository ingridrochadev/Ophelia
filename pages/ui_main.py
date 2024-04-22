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
from PySide6.QtWidgets import (QApplication, QComboBox, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QSpacerItem,
    QStackedWidget, QTableWidget, QTableWidgetItem, QToolBox,
    QVBoxLayout, QWidget)
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1030, 807)
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
        self.left_container.setMinimumSize(QSize(7, 0))
        self.left_container.setMaximumSize(QSize(9, 16777215))
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
        self.Vistos.setGeometry(QRect(0, 0, 122, 657))
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
        self.Usuario.setGeometry(QRect(0, 0, 117, 657))
        self.verticalLayout_9 = QVBoxLayout(self.Usuario)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.btn_inserir_user = QPushButton(self.Usuario)
        self.btn_inserir_user.setObjectName(u"btn_inserir_user")
        self.btn_inserir_user.setMinimumSize(QSize(0, 30))
        self.btn_inserir_user.setFont(font2)

        self.verticalLayout_9.addWidget(self.btn_inserir_user)

        self.btn_editarUsuario = QPushButton(self.Usuario)
        self.btn_editarUsuario.setObjectName(u"btn_editarUsuario")
        self.btn_editarUsuario.setMinimumSize(QSize(0, 30))
        self.btn_editarUsuario.setFont(font2)

        self.verticalLayout_9.addWidget(self.btn_editarUsuario)

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
        self.btn_toggle = QPushButton(self.top_frame)
        self.btn_toggle.setObjectName(u"btn_toggle")
        icon = QIcon()
        icon.addFile(u":/logo/pages/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_toggle.setIcon(icon)
        self.btn_toggle.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_toggle, 0, Qt.AlignLeft)

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
        self.pg_adicionar = QWidget()
        self.pg_adicionar.setObjectName(u"pg_adicionar")
        self.verticalLayout_10 = QVBoxLayout(self.pg_adicionar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.pg_adicionar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255,255,255);\n"
"font: 11pt \"Lato Heavy\"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(231,231,231);	\n"
"border-radius: 8px\n"
"}\n"
"\n"
"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.frame_3 = QFrame(self.frame_4)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_11 = QFrame(self.frame_3)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(400, 60))
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_11)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalSpacer_7 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_7)

        self.img_space = QLabel(self.frame_11)
        self.img_space.setObjectName(u"img_space")
        self.img_space.setMinimumSize(QSize(0, 300))
        self.img_space.setMaximumSize(QSize(600, 300))
        self.img_space.setStyleSheet(u"background-color:rgb(255,255,255);\n"
"frame-radius:10px;")

        self.verticalLayout_8.addWidget(self.img_space)

        self.btn_ler = QPushButton(self.frame_11)
        self.btn_ler.setObjectName(u"btn_ler")
        self.btn_ler.setMinimumSize(QSize(100, 40))
        self.btn_ler.setMaximumSize(QSize(120, 100))
        self.btn_ler.setSizeIncrement(QSize(0, 1))
        font4 = QFont()
        font4.setFamilies([u"Lato Bold"])
        font4.setPointSize(11)
        self.btn_ler.setFont(font4)
        self.btn_ler.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ler.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(190, 190, 190);\n"
"    border-radius: 20px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 20px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/logo/pages/icons/Black Minimalist Outline Icons Icon Set (2).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_ler.setIcon(icon1)
        self.btn_ler.setIconSize(QSize(70, 70))

        self.verticalLayout_8.addWidget(self.btn_ler, 0, Qt.AlignHCenter)

        self.verticalSpacer_6 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_8.addItem(self.verticalSpacer_6)


        self.horizontalLayout_6.addWidget(self.frame_11)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        font5 = QFont()
        font5.setBold(False)
        self.frame_8.setFont(font5)
        self.frame_8.setMouseTracking(False)
        self.frame_8.setStyleSheet(u"QFrame {\n"
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
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_8)
        self.gridLayout.setObjectName(u"gridLayout")
        self.nacionalidade_line = QLineEdit(self.frame_8)
        self.nacionalidade_line.setObjectName(u"nacionalidade_line")
        self.nacionalidade_line.setMinimumSize(QSize(340, 40))
        self.nacionalidade_line.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.nacionalidade_line, 3, 1, 1, 1)

        self.lbl_nacionalidade = QLabel(self.frame_8)
        self.lbl_nacionalidade.setObjectName(u"lbl_nacionalidade")

        self.gridLayout.addWidget(self.lbl_nacionalidade, 3, 0, 1, 1)

        self.date_nasc_line = QLineEdit(self.frame_8)
        self.date_nasc_line.setObjectName(u"date_nasc_line")
        self.date_nasc_line.setMinimumSize(QSize(340, 40))
        self.date_nasc_line.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.date_nasc_line, 2, 1, 1, 1)

        self.lbl_nome = QLabel(self.frame_8)
        self.lbl_nome.setObjectName(u"lbl_nome")

        self.gridLayout.addWidget(self.lbl_nome, 0, 0, 1, 1)

        self.lbl_passaporte = QLabel(self.frame_8)
        self.lbl_passaporte.setObjectName(u"lbl_passaporte")

        self.gridLayout.addWidget(self.lbl_passaporte, 4, 0, 1, 1)

        self.lbl_city = QLabel(self.frame_8)
        self.lbl_city.setObjectName(u"lbl_city")

        self.gridLayout.addWidget(self.lbl_city, 5, 0, 1, 1)

        self.lbl_tipo_visto = QLabel(self.frame_8)
        self.lbl_tipo_visto.setObjectName(u"lbl_tipo_visto")

        self.gridLayout.addWidget(self.lbl_tipo_visto, 7, 0, 1, 1)

        self.tipo_visto_line = QLineEdit(self.frame_8)
        self.tipo_visto_line.setObjectName(u"tipo_visto_line")
        self.tipo_visto_line.setMinimumSize(QSize(340, 40))
        self.tipo_visto_line.setMaximumSize(QSize(500, 16777215))
        self.tipo_visto_line.setClearButtonEnabled(False)

        self.gridLayout.addWidget(self.tipo_visto_line, 7, 1, 1, 1)

        self.city_line = QLineEdit(self.frame_8)
        self.city_line.setObjectName(u"city_line")
        self.city_line.setMinimumSize(QSize(340, 40))
        self.city_line.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.city_line, 5, 1, 1, 1)

        self.lbl_exp = QLabel(self.frame_8)
        self.lbl_exp.setObjectName(u"lbl_exp")

        self.gridLayout.addWidget(self.lbl_exp, 6, 0, 1, 1)

        self.nome_line = QLineEdit(self.frame_8)
        self.nome_line.setObjectName(u"nome_line")
        self.nome_line.setMinimumSize(QSize(340, 40))
        self.nome_line.setMaximumSize(QSize(500, 16777215))
        font6 = QFont()
        font6.setFamilies([u"Lato Heavy"])
        font6.setPointSize(11)
        font6.setBold(False)
        font6.setItalic(False)
        self.nome_line.setFont(font6)
        self.nome_line.setLayoutDirection(Qt.LeftToRight)
        self.nome_line.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")

        self.gridLayout.addWidget(self.nome_line, 0, 1, 1, 2)

        self.lbl_dob = QLabel(self.frame_8)
        self.lbl_dob.setObjectName(u"lbl_dob")

        self.gridLayout.addWidget(self.lbl_dob, 2, 0, 1, 1)

        self.passport_line = QLineEdit(self.frame_8)
        self.passport_line.setObjectName(u"passport_line")
        self.passport_line.setMinimumSize(QSize(340, 40))
        self.passport_line.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.passport_line, 4, 1, 1, 1)

        self.validade_line = QLineEdit(self.frame_8)
        self.validade_line.setObjectName(u"validade_line")
        self.validade_line.setMinimumSize(QSize(340, 40))
        self.validade_line.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.validade_line, 6, 1, 1, 1)

        self.num_visto_line = QLineEdit(self.frame_8)
        self.num_visto_line.setObjectName(u"num_visto_line")
        self.num_visto_line.setMinimumSize(QSize(340, 40))
        self.num_visto_line.setMaximumSize(QSize(500, 16777215))

        self.gridLayout.addWidget(self.num_visto_line, 8, 1, 1, 1)

        self.lbl_num_visto = QLabel(self.frame_8)
        self.lbl_num_visto.setObjectName(u"lbl_num_visto")

        self.gridLayout.addWidget(self.lbl_num_visto, 8, 0, 1, 1)

        self.btn_add_2 = QPushButton(self.frame_8)
        self.btn_add_2.setObjectName(u"btn_add_2")
        self.btn_add_2.setMinimumSize(QSize(100, 30))
        self.btn_add_2.setMaximumSize(QSize(200, 16777215))
        self.btn_add_2.setFont(font4)
        self.btn_add_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_2.setLayoutDirection(Qt.LeftToRight)
        self.btn_add_2.setAutoFillBackground(False)
        self.btn_add_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(190, 190, 190);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")

        self.gridLayout.addWidget(self.btn_add_2, 9, 1, 1, 1, Qt.AlignHCenter)


        self.horizontalLayout_6.addWidget(self.frame_8)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.Pages.addWidget(self.pg_adicionar)
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_7.addWidget(self.logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_listar = QWidget()
        self.pg_listar.setObjectName(u"pg_listar")
        self.horizontalLayout_8 = QHBoxLayout(self.pg_listar)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_5 = QFrame(self.pg_listar)
        self.frame_5.setObjectName(u"frame_5")
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
        self.tbl_vistos.setGeometry(QRect(0, 70, 821, 558))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tbl_vistos.sizePolicy().hasHeightForWidth())
        self.tbl_vistos.setSizePolicy(sizePolicy1)
        self.tbl_vistos.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148, 148, 148);\n"
"color:rgb(255,255,255);\n"
"font: 11pt \"Lato Heavy\";\n"
"}\n"
"QTableWidget{\n"
"background-color:rgb(252, 252, 252);\n"
"}")
        self.tbl_vistos.horizontalHeader().setDefaultSectionSize(274)
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(840, 70, 100, 558))
        self.frame_7.setStyleSheet(u"QPushButton{\n"
"border-radius: 15px;\n"
"background-color: rgb(255,255,255);\n"
"font: 11pt \"Lato Heavy\";\n"
"color: rgb(0,24,74)\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(230,230,230);\n"
"}")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_7)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.btn_exportar = QPushButton(self.frame_7)
        self.btn_exportar.setObjectName(u"btn_exportar")
        self.btn_exportar.setMinimumSize(QSize(0, 30))
        self.btn_exportar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_exportar.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Heavy\", sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Heavy\", sans-serif;\n"
"	color: #fff\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_exportar)

        self.btn_alterar_2 = QPushButton(self.frame_7)
        self.btn_alterar_2.setObjectName(u"btn_alterar_2")
        self.btn_alterar_2.setMinimumSize(QSize(0, 30))
        self.btn_alterar_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_2.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Heavy\", sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Heavy\", sans-serif;\n"
"	color: #fff\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_alterar_2)

        self.btn_excluir = QPushButton(self.frame_7)
        self.btn_excluir.setObjectName(u"btn_excluir")
        self.btn_excluir.setMinimumSize(QSize(0, 30))
        self.btn_excluir.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_excluir.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Heavy\", sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Heavy\", sans-serif;\n"
"	color: #fff\n"
"}")

        self.verticalLayout_12.addWidget(self.btn_excluir)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_12.addItem(self.verticalSpacer_3)

        self.ttl_vistos = QLabel(self.frame_5)
        self.ttl_vistos.setObjectName(u"ttl_vistos")
        self.ttl_vistos.setGeometry(QRect(350, 10, 250, 50))
        font7 = QFont()
        font7.setFamilies([u"Lato"])
        font7.setPointSize(12)
        font7.setBold(True)
        font7.setKerning(True)
        self.ttl_vistos.setFont(font7)
        self.ttl_vistos.setLayoutDirection(Qt.LeftToRight)
        self.ttl_vistos.setStyleSheet(u"background-color: transparent;\n"
"color:rgb(255,255,255);\n"
"border-radius:10px;")
        self.ttl_vistos.setLineWidth(1)
        self.ttl_vistos.setAlignment(Qt.AlignCenter)
        self.ttl_vistos.setIndent(-1)

        self.horizontalLayout_8.addWidget(self.frame_5)

        self.Pages.addWidget(self.pg_listar)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.gridLayout_2 = QGridLayout(self.pg_sobre)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.frame_6 = QFrame(self.pg_sobre)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setStyleSheet(u"background-color:white;")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.txt_sobre = QLabel(self.frame_6)
        self.txt_sobre.setObjectName(u"txt_sobre")
        self.txt_sobre.setGeometry(QRect(240, 90, 500, 210))
        sizePolicy.setHeightForWidth(self.txt_sobre.sizePolicy().hasHeightForWidth())
        self.txt_sobre.setSizePolicy(sizePolicy)
        self.txt_sobre.setMinimumSize(QSize(0, 210))
        self.txt_sobre.setMaximumSize(QSize(500, 16777215))
        font8 = QFont()
        font8.setFamilies([u"Lato"])
        font8.setPointSize(15)
        font8.setBold(False)
        font8.setItalic(False)
        self.txt_sobre.setFont(font8)
        self.txt_sobre.setStyleSheet(u"color:purple;")
        self.txt_sobre.setAlignment(Qt.AlignCenter)
        self.txt_sobre.setWordWrap(True)
        self.txt_desenvolvedoras = QLabel(self.frame_6)
        self.txt_desenvolvedoras.setObjectName(u"txt_desenvolvedoras")
        self.txt_desenvolvedoras.setGeometry(QRect(310, 263, 371, 400))
        self.txt_desenvolvedoras.setMinimumSize(QSize(0, 400))
        self.txt_desenvolvedoras.setMaximumSize(QSize(800, 400))
        font9 = QFont()
        font9.setFamilies([u"Lato"])
        font9.setPointSize(25)
        font9.setBold(False)
        font9.setItalic(False)
        self.txt_desenvolvedoras.setFont(font9)
        self.txt_desenvolvedoras.setStyleSheet(u"color:purple;\n"
"background-color:transparent;")
        self.ttl_sobre = QLabel(self.frame_6)
        self.ttl_sobre.setObjectName(u"ttl_sobre")
        self.ttl_sobre.setGeometry(QRect(410, 20, 161, 71))
        self.ttl_sobre.setMinimumSize(QSize(100, 30))
        font10 = QFont()
        font10.setFamilies([u"Lato"])
        font10.setPointSize(16)
        font10.setBold(False)
        font10.setItalic(False)
        self.ttl_sobre.setFont(font10)
        self.ttl_sobre.setAutoFillBackground(False)
        self.ttl_sobre.setStyleSheet(u"color:purple;")
        self.label_7 = QLabel(self.frame_6)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(200, -150, 761, 801))
        self.label_7.setPixmap(QPixmap(u":/logo/pages/icons/Fundo.png"))
        self.label_7.setScaledContents(True)
        self.label_7.raise_()
        self.txt_desenvolvedoras.raise_()
        self.txt_sobre.raise_()
        self.ttl_sobre.raise_()

        self.gridLayout_2.addWidget(self.frame_6, 0, 0, 2, 1)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_alterar_usuario = QWidget()
        self.pg_alterar_usuario.setObjectName(u"pg_alterar_usuario")
        self.frame_15 = QFrame(self.pg_alterar_usuario)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setGeometry(QRect(0, 0, 971, 651))
        self.frame_15.setStyleSheet(u"background-color: transparent;")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.label_5 = QLabel(self.frame_15)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(270, 50, 471, 51))
        font11 = QFont()
        font11.setFamilies([u"Lato"])
        font11.setPointSize(34)
        font11.setBold(False)
        font11.setItalic(False)
        self.label_5.setFont(font11)
        self.label_5.setStyleSheet(u"background-color: transparent;")
        self.label_6 = QLabel(self.frame_15)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(40, 150, 431, 431))
        self.label_6.setPixmap(QPixmap(u":/logo/pages/icons/Black Minimalist Outline Icons Icon Set (1).png"))
        self.label_6.setScaledContents(True)
        self.frame_12 = QFrame(self.frame_15)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setGeometry(QRect(550, 200, 351, 353))
        self.frame_12.setStyleSheet(u"QFrame{\n"
"background-color:white;\n"
"border-radius:5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color:grey;\n"
"    border-bottom: 2px solid grey; /* Adiciona uma borda somente na parte inferior */\n"
"	font-family: \"Lato Heavy\", serif;\n"
"    font-size: 16px;\n"
"}")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy)
        self.frame_13.setStyleSheet(u"QFrame {\n"
"    border-radius: 4px\n"
"}")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_13)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_4)

        self.emial_line = QLineEdit(self.frame_13)
        self.emial_line.setObjectName(u"emial_line")
        self.emial_line.setMinimumSize(QSize(0, 40))
        self.emial_line.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.emial_line)

        self.senha_atual_line = QLineEdit(self.frame_13)
        self.senha_atual_line.setObjectName(u"senha_atual_line")
        self.senha_atual_line.setMinimumSize(QSize(0, 40))
        self.senha_atual_line.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.senha_atual_line.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.senha_atual_line)

        self.senha_line = QLineEdit(self.frame_13)
        self.senha_line.setObjectName(u"senha_line")
        self.senha_line.setMinimumSize(QSize(0, 40))
        self.senha_line.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.senha_line.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.senha_line)

        self.senha_line_2 = QLineEdit(self.frame_13)
        self.senha_line_2.setObjectName(u"senha_line_2")
        self.senha_line_2.setMinimumSize(QSize(0, 40))
        self.senha_line_2.setEchoMode(QLineEdit.PasswordEchoOnEdit)
        self.senha_line_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.senha_line_2)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_15.addItem(self.verticalSpacer_5)


        self.verticalLayout_14.addWidget(self.frame_13)

        self.btn_alterar = QFrame(self.frame_12)
        self.btn_alterar.setObjectName(u"btn_alterar")
        self.btn_alterar.setMinimumSize(QSize(0, 30))
        self.btn_alterar.setFrameShape(QFrame.StyledPanel)
        self.btn_alterar.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.btn_alterar)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.btn_alterar_senha = QPushButton(self.btn_alterar)
        self.btn_alterar_senha.setObjectName(u"btn_alterar_senha")
        self.btn_alterar_senha.setMinimumSize(QSize(200, 35))
        self.btn_alterar_senha.setMaximumSize(QSize(200, 16777215))
        self.btn_alterar_senha.setFont(font4)
        self.btn_alterar_senha.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_alterar_senha.setLayoutDirection(Qt.LeftToRight)
        self.btn_alterar_senha.setAutoFillBackground(False)
        self.btn_alterar_senha.setStyleSheet(u"QPushButton {\n"
"    background-color: rgb(190, 190, 190);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")

        self.verticalLayout_16.addWidget(self.btn_alterar_senha)


        self.verticalLayout_14.addWidget(self.btn_alterar, 0, Qt.AlignHCenter)

        self.Pages.addWidget(self.pg_alterar_usuario)
        self.pg_inserir_user = QWidget()
        self.pg_inserir_user.setObjectName(u"pg_inserir_user")
        self.frame_9 = QFrame(self.pg_inserir_user)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setGeometry(QRect(0, 0, 971, 651))
        self.frame_9.setStyleSheet(u"background-color: transparent;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.label_3 = QLabel(self.frame_9)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(260, 50, 471, 51))
        self.label_3.setFont(font11)
        self.label_3.setStyleSheet(u"background-color: transparent;")
        self.label_4 = QLabel(self.frame_9)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 140, 501, 481))
        self.label_4.setPixmap(QPixmap(u":/logo/pages/icons/Black Minimalist Outline Icons Icon Set.png"))
        self.label_4.setScaledContents(True)
        self.frame_14 = QFrame(self.frame_9)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setGeometry(QRect(510, 190, 431, 481))
        self.frame_14.setStyleSheet(u"QFrame {\n"
"    border-radius: 4px\n"
"}\n"
"\n"
"QLineEdit {\n"
"    color:white;\n"
"    background-color: transparent;\n"
"    border-bottom: 2px solid white; /* Adiciona uma borda somente na parte inferior */\n"
"	font-family: \"Lato Heavy\", serif;\n"
"    font-size: 16px;\n"
"}")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.matricula_line = QLineEdit(self.frame_14)
        self.matricula_line.setObjectName(u"matricula_line")
        self.matricula_line.setGeometry(QRect(9, 101, 400, 40))
        self.matricula_line.setMinimumSize(QSize(400, 40))
        self.matricula_line.setMaximumSize(QSize(500, 16777215))
        self.cpf_line = QLineEdit(self.frame_14)
        self.cpf_line.setObjectName(u"cpf_line")
        self.cpf_line.setGeometry(QRect(9, 55, 400, 40))
        self.cpf_line.setMinimumSize(QSize(400, 40))
        self.cpf_line.setMaximumSize(QSize(500, 16777215))
        self.senha_add_user_ln = QLineEdit(self.frame_14)
        self.senha_add_user_ln.setObjectName(u"senha_add_user_ln")
        self.senha_add_user_ln.setGeometry(QRect(9, 193, 400, 40))
        self.senha_add_user_ln.setMinimumSize(QSize(400, 40))
        self.senha_add_user_ln.setMaximumSize(QSize(500, 16777215))
        self.senha_add_user_ln.setEchoMode(QLineEdit.Password)
        self.nome_user_line = QLineEdit(self.frame_14)
        self.nome_user_line.setObjectName(u"nome_user_line")
        self.nome_user_line.setGeometry(QRect(9, 9, 400, 40))
        self.nome_user_line.setMinimumSize(QSize(400, 40))
        self.nome_user_line.setMaximumSize(QSize(500, 16777215))
        font12 = QFont()
        font12.setFamilies([u"Lato Heavy"])
        font12.setBold(False)
        font12.setItalic(False)
        self.nome_user_line.setFont(font12)
        self.nome_user_line.setLayoutDirection(Qt.LeftToRight)
        self.nome_user_line.setStyleSheet(u"QFrame {\n"
"    background-color: transparent;\n"
"    border-radius: 8px;\n"
"    border: 2px solid white;\n"
"}")
        self.email_user_line = QLineEdit(self.frame_14)
        self.email_user_line.setObjectName(u"email_user_line")
        self.email_user_line.setGeometry(QRect(9, 147, 400, 40))
        self.email_user_line.setMinimumSize(QSize(400, 40))
        self.email_user_line.setMaximumSize(QSize(500, 16777215))
        self.btn_add_user = QPushButton(self.frame_14)
        self.btn_add_user.setObjectName(u"btn_add_user")
        self.btn_add_user.setGeometry(QRect(130, 340, 150, 50))
        self.btn_add_user.setMinimumSize(QSize(100, 30))
        self.btn_add_user.setMaximumSize(QSize(200, 16777215))
        font13 = QFont()
        font13.setFamilies([u"Lato Bold"])
        font13.setPointSize(15)
        self.btn_add_user.setFont(font13)
        self.btn_add_user.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_add_user.setLayoutDirection(Qt.LeftToRight)
        self.btn_add_user.setAutoFillBackground(False)
        self.btn_add_user.setStyleSheet(u"QPushButton {\n"
"    background-color: white;\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background-color: rgb(115, 0, 200);\n"
"    border-radius: 15px;\n"
"	font-family: \"Lato Bold\", sans-serif;\n"
"	color: #fff\n"
"}")
        self.lbl_perfil = QLabel(self.frame_14)
        self.lbl_perfil.setObjectName(u"lbl_perfil")
        self.lbl_perfil.setGeometry(QRect(9, 240, 111, 40))
        self.lbl_perfil.setMinimumSize(QSize(0, 35))
        self.lbl_perfil.setStyleSheet(u"color:white;\n"
"	font-family: \"Lato Heavy\", serif;\n"
"    font-size: 16px;")
        self.cb_perfil = QComboBox(self.frame_14)
        self.cb_perfil.addItem("")
        self.cb_perfil.addItem("")
        self.cb_perfil.setObjectName(u"cb_perfil")
        self.cb_perfil.setGeometry(QRect(170, 240, 241, 30))
        self.cb_perfil.setMaximumSize(QSize(16777215, 35))
        self.cb_perfil.setStyleSheet(u"color:rgb(70,70,70);\n"
"background-color:white;\n"
"border-radius:5px;")
        self.Pages.addWidget(self.pg_inserir_user)

        self.horizontalLayout_5.addWidget(self.Pages)


        self.verticalLayout.addWidget(self.main_frame)

        self.footer_frame = QFrame(self.main_container)
        self.footer_frame.setObjectName(u"footer_frame")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.footer_frame.sizePolicy().hasHeightForWidth())
        self.footer_frame.setSizePolicy(sizePolicy2)
        self.footer_frame.setFrameShape(QFrame.StyledPanel)
        self.footer_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.footer_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.label_2 = QLabel(self.footer_frame)
        self.label_2.setObjectName(u"label_2")
        font14 = QFont()
        font14.setFamilies([u"Lato"])
        font14.setBold(True)
        self.label_2.setFont(font14)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(1)
        self.Pages.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.txt_bemvindo.setText(QCoreApplication.translate("MainWindow", u"Bem-vindo(a)!", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_add.setText(QCoreApplication.translate("MainWindow", u"Adicionar Visto", None))
        self.btn_listar.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
        self.btn_sobre.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Vistos), QCoreApplication.translate("MainWindow", u"Vistos", None))
        self.btn_inserir_user.setText(QCoreApplication.translate("MainWindow", u"Inserir Usu\u00e1rio", None))
        self.btn_editarUsuario.setText(QCoreApplication.translate("MainWindow", u"Alterar Senha", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Usuario), QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de leitura de Documentos de Viagem", None))
        self.img_space.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
        self.btn_ler.setText("")
        self.nacionalidade_line.setText("")
        self.nacionalidade_line.setPlaceholderText("")
        self.lbl_nacionalidade.setText(QCoreApplication.translate("MainWindow", u"Nacionalidade", None))
        self.date_nasc_line.setPlaceholderText("")
        self.lbl_nome.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.lbl_passaporte.setText(QCoreApplication.translate("MainWindow", u"Passaporte", None))
        self.lbl_city.setText(QCoreApplication.translate("MainWindow", u"Cidade emitente", None))
        self.lbl_tipo_visto.setText(QCoreApplication.translate("MainWindow", u"Tipo de visto", None))
        self.tipo_visto_line.setPlaceholderText("")
        self.city_line.setText("")
        self.city_line.setPlaceholderText("")
        self.lbl_exp.setText(QCoreApplication.translate("MainWindow", u"Validade do visto", None))
        self.nome_line.setPlaceholderText("")
        self.lbl_dob.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento  ", None))
        self.passport_line.setPlaceholderText("")
        self.validade_line.setPlaceholderText("")
        self.num_visto_line.setPlaceholderText("")
        self.lbl_num_visto.setText(QCoreApplication.translate("MainWindow", u"N\u00famero do visto", None))
        self.btn_add_2.setText(QCoreApplication.translate("MainWindow", u"     Adicionar     ", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/logo/pages/icons/logo_nome_branco.png\"/></p></body></html>", None))
        ___qtablewidgetitem = self.tbl_vistos.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tbl_vistos.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Passaporte", None));
        ___qtablewidgetitem2 = self.tbl_vistos.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Status Embarque", None));
        self.btn_exportar.setText(QCoreApplication.translate("MainWindow", u"Exportar", None))
        self.btn_alterar_2.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.ttl_vistos.setText(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Lato'; font-size:12pt; font-weight:600; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:28pt;\">VISTOS</span></p></body></html>", None))
        self.txt_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:22pt;\"><br/>Esse sistema l\u00ea as informa\u00e7\u00f5es contidas nos vistos de passageiros viajando para os EUA e libera ou nega o embarque desses passageiros nos voos das companhias a\u00e9reas.</span></p></body></html>", None))
        self.txt_desenvolvedoras.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:28pt; font-weight:600;\">DESENVOLVEDORAS:</span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">BIANCA YURI</span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">DJULLIE CAROLINE</span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">INGRID ROCHA</span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">TAYNARA MORAIS</span></p><p align=\"center\"><span style=\" font-size:22pt; font-weight:600;\">YASMIM FERREIRA</span></p></body></html>", None))
        self.ttl_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">SOBRE</span></p></body></html>", None))
        self.label_7.setText("")
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Alterar Senha</span></p></body></html>", None))
        self.label_6.setText("")
        self.emial_line.setText("")
        self.emial_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.senha_atual_line.setText("")
        self.senha_atual_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha Atual", None))
        self.senha_line.setText("")
        self.senha_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nova Senha", None))
        self.senha_line_2.setText("")
        self.senha_line_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Confirmar Senha", None))
        self.btn_alterar_senha.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:36pt;\">Cadastro de Usu\u00e1rio</span></p></body></html>", None))
        self.label_4.setText("")
        self.matricula_line.setText("")
        self.matricula_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Matr\u00edcula", None))
        self.cpf_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"CPF", None))
        self.senha_add_user_ln.setText("")
        self.senha_add_user_ln.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.nome_user_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.email_user_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.btn_add_user.setText(QCoreApplication.translate("MainWindow", u"     Adicionar     ", None))
        self.lbl_perfil.setText(QCoreApplication.translate("MainWindow", u"Tipo de Perfil", None))
        self.cb_perfil.setItemText(0, QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.cb_perfil.setItemText(1, QCoreApplication.translate("MainWindow", u"Administrador", None))

        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Ophelia 2024", None))
    # retranslateUi

