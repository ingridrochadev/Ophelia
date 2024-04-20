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
from PySide6.QtWidgets import (QApplication, QFrame, QGridLayout, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QStackedWidget,
    QTableWidget, QTableWidgetItem, QToolBox, QVBoxLayout,
    QWidget)
import logo_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1017, 837)
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
        self.horizontalLayout.setSpacing(0)
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
        self.Vistos.setGeometry(QRect(0, 0, 122, 687))
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
        self.Usuario.setGeometry(QRect(0, 0, 114, 687))
        self.verticalLayout_9 = QVBoxLayout(self.Usuario)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
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
        self.pg_home = QWidget()
        self.pg_home.setObjectName(u"pg_home")
        self.verticalLayout_7 = QVBoxLayout(self.pg_home)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.logo = QLabel(self.pg_home)
        self.logo.setObjectName(u"logo")

        self.verticalLayout_7.addWidget(self.logo)

        self.Pages.addWidget(self.pg_home)
        self.pg_adicionar = QWidget()
        self.pg_adicionar.setObjectName(u"pg_adicionar")
        self.verticalLayout_10 = QVBoxLayout(self.pg_adicionar)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.frame_4 = QFrame(self.pg_adicionar)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255,255,255);\n"
"font: 10pt \"MS Shell Dig 2\"\n"
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
        self.verticalLayout_8 = QVBoxLayout(self.frame_3)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.ttl_add = QLabel(self.frame_3)
        self.ttl_add.setObjectName(u"ttl_add")
        self.ttl_add.setMinimumSize(QSize(0, 0))
        self.ttl_add.setLayoutDirection(Qt.LeftToRight)
        self.ttl_add.setStyleSheet(u"color:rgb(115,0,220);\n"
"background-color: rgb(249, 249, 249)")
        self.ttl_add.setAlignment(Qt.AlignCenter)

        self.verticalLayout_8.addWidget(self.ttl_add)

        self.frame_8 = QFrame(self.frame_3)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setStyleSheet(u"QFrame {\n"
"    border-radius: 4px\n"
"}")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_8)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.frame_6 = QFrame(self.frame_8)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setMinimumSize(QSize(0, 80))
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton = QPushButton(self.frame_6)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 30))
        self.pushButton.setMaximumSize(QSize(300, 16777215))
        self.pushButton.setSizeIncrement(QSize(0, 1))
        font4 = QFont()
        font4.setFamilies([u"Lato Bold"])
        font4.setPointSize(11)
        self.pushButton.setFont(font4)
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
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

        self.horizontalLayout_6.addWidget(self.pushButton)


        self.verticalLayout_6.addWidget(self.frame_6)

        self.nome_line = QLineEdit(self.frame_8)
        self.nome_line.setObjectName(u"nome_line")
        self.nome_line.setMinimumSize(QSize(0, 40))
        self.nome_line.setStyleSheet(u"QFrame {\n"
"    border-radius: 8px;\n"
"}")

        self.verticalLayout_6.addWidget(self.nome_line)

        self.date_nasc_line = QLineEdit(self.frame_8)
        self.date_nasc_line.setObjectName(u"date_nasc_line")
        self.date_nasc_line.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.date_nasc_line)

        self.nacionalidade_line = QLineEdit(self.frame_8)
        self.nacionalidade_line.setObjectName(u"nacionalidade_line")
        self.nacionalidade_line.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.nacionalidade_line)

        self.passport_line = QLineEdit(self.frame_8)
        self.passport_line.setObjectName(u"passport_line")
        self.passport_line.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.passport_line)

        self.gender_line = QLineEdit(self.frame_8)
        self.gender_line.setObjectName(u"gender_line")
        self.gender_line.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.gender_line)

        self.validade_line = QLineEdit(self.frame_8)
        self.validade_line.setObjectName(u"validade_line")
        self.validade_line.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.validade_line)

        self.tipo_visto_line = QLineEdit(self.frame_8)
        self.tipo_visto_line.setObjectName(u"tipo_visto_line")
        self.tipo_visto_line.setMinimumSize(QSize(0, 40))
        self.tipo_visto_line.setClearButtonEnabled(False)

        self.verticalLayout_6.addWidget(self.tipo_visto_line)

        self.num_visto_line = QLineEdit(self.frame_8)
        self.num_visto_line.setObjectName(u"num_visto_line")
        self.num_visto_line.setMinimumSize(QSize(0, 40))

        self.verticalLayout_6.addWidget(self.num_visto_line)


        self.verticalLayout_8.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_3)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setMinimumSize(QSize(0, 80))
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.gridLayout = QGridLayout(self.frame_9)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ctn_add = QPushButton(self.frame_9)
        self.ctn_add.setObjectName(u"ctn_add")
        self.ctn_add.setMinimumSize(QSize(100, 30))
        self.ctn_add.setMaximumSize(QSize(200, 16777215))
        self.ctn_add.setFont(font4)
        self.ctn_add.setCursor(QCursor(Qt.PointingHandCursor))
        self.ctn_add.setLayoutDirection(Qt.LeftToRight)
        self.ctn_add.setAutoFillBackground(False)
        self.ctn_add.setStyleSheet(u"QPushButton {\n"
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

        self.gridLayout.addWidget(self.ctn_add, 0, 0, 1, 1)


        self.verticalLayout_8.addWidget(self.frame_9)


        self.horizontalLayout_4.addWidget(self.frame_3)


        self.verticalLayout_10.addWidget(self.frame_4)

        self.Pages.addWidget(self.pg_adicionar)
        self.pg_listar = QWidget()
        self.pg_listar.setObjectName(u"pg_listar")
        self.horizontalLayout_8 = QHBoxLayout(self.pg_listar)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.frame_5 = QFrame(self.pg_listar)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.NoFrame)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.tableWidget_2 = QTableWidget(self.frame_5)
        if (self.tableWidget_2.columnCount() < 9):
            self.tableWidget_2.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setGeometry(QRect(5, 50, 589, 558))
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tableWidget_2.sizePolicy().hasHeightForWidth())
        self.tableWidget_2.setSizePolicy(sizePolicy1)
        self.tableWidget_2.setStyleSheet(u"QHeaderView::section{\n"
"background-color:rgb(148, 148, 148);\n"
"color:rgb(255,255,255);\n"
"font: 11pt \"Lato Heavy\";\n"
"}\n"
"QTableWidget{\n"
"background-color:rgb(252, 252, 252);\n"
"}")
        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setGeometry(QRect(600, 50, 100, 558))
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
        self.btn_ordenar = QPushButton(self.frame_7)
        self.btn_ordenar.setObjectName(u"btn_ordenar")
        self.btn_ordenar.setMinimumSize(QSize(0, 30))
        self.btn_ordenar.setCursor(QCursor(Qt.PointingHandCursor))
        self.btn_ordenar.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_12.addWidget(self.btn_ordenar)

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

        self.label_9 = QLabel(self.frame_5)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(210, 10, 301, 31))
        font5 = QFont()
        font5.setFamilies([u"Lato"])
        font5.setPointSize(14)
        font5.setBold(True)
        self.label_9.setFont(font5)
        self.label_9.setLayoutDirection(Qt.LeftToRight)
        self.label_9.setStyleSheet(u"color:rgb(255,255,255);")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.frame_5)

        self.Pages.addWidget(self.pg_listar)
        self.pg_sobre = QWidget()
        self.pg_sobre.setObjectName(u"pg_sobre")
        self.verticalLayout_13 = QVBoxLayout(self.pg_sobre)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.ttl_sobre = QLabel(self.pg_sobre)
        self.ttl_sobre.setObjectName(u"ttl_sobre")
        self.ttl_sobre.setMinimumSize(QSize(100, 30))
        font6 = QFont()
        font6.setFamilies([u"Lato"])
        font6.setPointSize(16)
        font6.setBold(True)
        self.ttl_sobre.setFont(font6)
        self.ttl_sobre.setAutoFillBackground(False)

        self.verticalLayout_13.addWidget(self.ttl_sobre)

        self.txt_sobre = QLabel(self.pg_sobre)
        self.txt_sobre.setObjectName(u"txt_sobre")
        sizePolicy.setHeightForWidth(self.txt_sobre.sizePolicy().hasHeightForWidth())
        self.txt_sobre.setSizePolicy(sizePolicy)
        self.txt_sobre.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.txt_sobre)

        self.Pages.addWidget(self.pg_sobre)
        self.pg_alterar_usuario = QWidget()
        self.pg_alterar_usuario.setObjectName(u"pg_alterar_usuario")
        self.frame_10 = QFrame(self.pg_alterar_usuario)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setGeometry(QRect(200, 90, 411, 491))
        self.frame_10.setStyleSheet(u"QLineEdit{\n"
"background-color: rgb(255,255,255);\n"
"font: 10pt \"MS Shell Dig 2\"\n"
"}\n"
"\n"
"QFrame{\n"
"background-color: rgb(231,231,231);	\n"
"border-radius: 8px\n"
"}\n"
"\n"
"")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.frame_10)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.frame_12 = QFrame(self.frame_10)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_12)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.ttl_add_2 = QLabel(self.frame_12)
        self.ttl_add_2.setObjectName(u"ttl_add_2")
        self.ttl_add_2.setMinimumSize(QSize(0, 0))
        self.ttl_add_2.setLayoutDirection(Qt.LeftToRight)
        self.ttl_add_2.setStyleSheet(u"color:rgb(115,0,220);\n"
"background-color: rgb(249, 249, 249)")
        self.ttl_add_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_14.addWidget(self.ttl_add_2)

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

        self.senha_line = QLineEdit(self.frame_13)
        self.senha_line.setObjectName(u"senha_line")
        self.senha_line.setMinimumSize(QSize(0, 40))
        self.senha_line.setAlignment(Qt.AlignCenter)

        self.verticalLayout_15.addWidget(self.senha_line)

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
        self.ctn_add_2 = QPushButton(self.btn_alterar)
        self.ctn_add_2.setObjectName(u"ctn_add_2")
        self.ctn_add_2.setMinimumSize(QSize(0, 30))
        self.ctn_add_2.setFont(font4)
        self.ctn_add_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.ctn_add_2.setLayoutDirection(Qt.LeftToRight)
        self.ctn_add_2.setAutoFillBackground(False)
        self.ctn_add_2.setStyleSheet(u"QPushButton {\n"
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

        self.verticalLayout_16.addWidget(self.ctn_add_2)


        self.verticalLayout_14.addWidget(self.btn_alterar)


        self.horizontalLayout_7.addWidget(self.frame_12)

        self.Pages.addWidget(self.pg_alterar_usuario)

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
        font7 = QFont()
        font7.setFamilies([u"Lato"])
        font7.setBold(True)
        self.label_2.setFont(font7)

        self.verticalLayout_2.addWidget(self.label_2)


        self.verticalLayout.addWidget(self.footer_frame)


        self.horizontalLayout.addWidget(self.main_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.toolBox.setCurrentIndex(0)
        self.Pages.setCurrentIndex(3)


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
        self.btn_editarUsuario.setText(QCoreApplication.translate("MainWindow", u"Editar Usu\u00e1rio", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.Usuario), QCoreApplication.translate("MainWindow", u"Usu\u00e1rio", None))
        self.btn_toggle.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Sistema de leitura de Documentos de Viagem", None))
        self.logo.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><img src=\":/logo/pages/icons/logo_nome_branco.png\"/></p></body></html>", None))
        self.ttl_add.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">VISTO</span></p></body></html>", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"       Buscar Arquivo       ", None))
        self.nome_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.date_nasc_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
        self.nacionalidade_line.setText("")
        self.nacionalidade_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Nacionalidade", None))
        self.passport_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Passaporte", None))
        self.gender_line.setText("")
        self.gender_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Cidade emitente", None))
        self.validade_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Validade do visto", None))
        self.tipo_visto_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Tipo de visto", None))
        self.num_visto_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"N\u00famero do visto", None))
        self.ctn_add.setText(QCoreApplication.translate("MainWindow", u"     Adicionar     ", None))
        ___qtablewidgetitem = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem1 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Passaporte ", None));
        ___qtablewidgetitem2 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Nacionalidade", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Sexo", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Data de validade", None));
        ___qtablewidgetitem6 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Tipo de visto", None));
        ___qtablewidgetitem7 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Cidade emitente", None));
        ___qtablewidgetitem8 = self.tableWidget_2.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"N\u00famero do visto", None));
        self.btn_ordenar.setText(QCoreApplication.translate("MainWindow", u"Listar", None))
        self.btn_alterar_2.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.btn_excluir.setText(QCoreApplication.translate("MainWindow", u"Excluir", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:24pt; font-weight:600;\">Vistos inseridos</span></p></body></html>", None))
        self.ttl_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\">SOBRE</p></body></html>", None))
        self.txt_sobre.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Esse sistema l\u00ea as informa\u00e7\u00f5es contidas nos vistos de passageiros viajando para os EUA e libera ou nega o embarque desses passageiros nos voos das companhias a\u00e9reas.</span></p></body></html>", None))
        self.ttl_add_2.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">USU\u00c1RIO</span></p></body></html>", None))
        self.emial_line.setText("")
        self.emial_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.senha_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Senha", None))
        self.ctn_add_2.setText(QCoreApplication.translate("MainWindow", u"Alterar", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u00a9 Ophelia 2024", None))
    # retranslateUi

