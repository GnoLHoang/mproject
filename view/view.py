# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'view.ui'
#
# Created by: PyQt5 UI code generator 5.15.11
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from googletrans import LANGCODES, LANGUAGES

class Ui_TranslateApp(object):
    def setupUi(self, TranslateApp):
        TranslateApp.setObjectName("TranslateApp")
        TranslateApp.resize(1280, 720)
        TranslateApp.setMinimumSize(QtCore.QSize(1, 1))
        TranslateApp.setMaximumSize(QtCore.QSize(1280, 720))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        TranslateApp.setFont(font)
        TranslateApp.setAutoFillBackground(False)
        TranslateApp.setStyleSheet("background-color: rgb(159, 199, 240);")
        TranslateApp.setProperty("fa", "")
        self.centralwidget = QtWidgets.QWidget(TranslateApp)
        self.centralwidget.setObjectName("centralwidget")
        self.name = QtWidgets.QLabel(self.centralwidget)
        self.name.setGeometry(QtCore.QRect(480, 20, 301, 61))
        self.name.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Noto Sans Condensed")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferAntialias)
        self.name.setFont(font)
        self.name.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.name.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.name.setFrameShadow(QtWidgets.QFrame.Plain)
        self.name.setTextFormat(QtCore.Qt.AutoText)
        self.name.setAlignment(QtCore.Qt.AlignCenter)
        self.name.setObjectName("name")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(40, 230, 561, 301))
        self.textEdit.setStyleSheet("QTextEdit {\n"
"    border: 2px solid rgb(255, 255, 255); \n"
"    border-radius: 20px;\n"
"    background-color: rgb(255, 255, 255);\n"
"    padding-left: 20px;\n"
"    padding-right: 20px;\n"
"}\n"
"")
        self.textEdit.setLineWrapMode(QtWidgets.QTextEdit.WidgetWidth)
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_2.setGeometry(QtCore.QRect(680, 230, 561, 301))
        self.textEdit_2.setStyleSheet("QTextEdit {\n"
"    border: 2px solid rgb(255, 255, 255); \n"
"    border-radius: 20px;\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.textEdit_2.setPlaceholderText("")
        self.textEdit_2.setObjectName("textEdit_2")
        self.reverse = QtWidgets.QPushButton(self.centralwidget)
        self.reverse.setGeometry(QtCore.QRect(600, 150, 81, 61))
        self.reverse.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/new/sync (2).png);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/new/sync (2) - Copy.png);\n"
"}")
        self.reverse.setText("")
        self.reverse.setObjectName("reverse")
        self.loa = QtWidgets.QPushButton(self.centralwidget)
        self.loa.setGeometry(QtCore.QRect(520, 460, 71, 61))
        self.loa.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/new/louder.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/new/louder - Copy.png);\n"
"}")
        self.loa.setText("")
        self.loa.setObjectName("loa")
        self.copy = QtWidgets.QPushButton(self.centralwidget)
        self.copy.setGeometry(QtCore.QRect(530, 240, 51, 51))
        self.copy.setStyleSheet("QPushButton {\n"
"    \n"
"    border-image: url(:/new/copy.png);\n"
"    background-color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover {\n"
"    \n"
"    border-image: url(:/new/copy - Copy.png);\n"
"}")
        self.copy.setText("")
        self.copy.setObjectName("copy")
        self.menu = QtWidgets.QPushButton(self.centralwidget)
        self.menu.setGeometry(QtCore.QRect(20, 10, 91, 71))
        self.menu.setStyleSheet("QPushButton {\n"
"    border-image: url(:/new/tab.png);\n"
"}\n"
"QPushButton:hover {\n"
"    background-color: rgb(200, 200, 200);\n"
"}")
        self.menu.setText("")
        self.menu.setObjectName("menu")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(550, 570, 171, 61))
        font = QtGui.QFont()
        font.setPointSize(22)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet("background-color: rgb(74, 136, 199);")
        self.pushButton.setObjectName("pushButton")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(220, 140, 161, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox.setFont(font)
        self.comboBox.setStyleSheet("QComboBox {\n"
"    \n"
"    background-color: rgb(74, 136, 199);\n"
"    border-radius: 15px\n"
"}")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("Tiếng Anh")
        self.comboBox.addItem("Tiếng Việt")
        self.comboBox.addItem("Tiếng Trung")
        self.comboBox.addItem("Tiếng Nhật")
        self.comboBox.addItem("Tiếng Hàn")
        self.comboBox_2 = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox_2.setGeometry(QtCore.QRect(910, 140, 261, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.comboBox_2.setFont(font)
        self.comboBox_2.setStyleSheet("QComboBox {\n"
"    \n"
"    background-color: rgb(74, 136, 199);\n"
"    border-radius: 15px\n"
"}")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("Tiếng Anh")
        self.comboBox_2.addItem("Tiếng Việt")
        self.comboBox_2.addItem("Tiếng Trung")
        self.comboBox_2.addItem("Tiếng Nhật")
        self.comboBox_2.addItem("Tiếng Hàn")
        TranslateApp.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(TranslateApp)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName("menubar")
        TranslateApp.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(TranslateApp)
        self.statusbar.setObjectName("statusbar")
        TranslateApp.setStatusBar(self.statusbar)

        self.retranslateUi(TranslateApp)
        QtCore.QMetaObject.connectSlotsByName(TranslateApp)

    def retranslateUi(self, TranslateApp):
        _translate = QtCore.QCoreApplication.translate
        TranslateApp.setWindowTitle(_translate("TranslateApp", "TranslateApp"))
        TranslateApp.setWhatsThis(_translate("TranslateApp", "<html><head/><body><p align=\"center\">wfeawefwaefwaefawef</p></body></html>"))
        self.name.setText(_translate("TranslateApp", "Translate App"))
        self.textEdit.setHtml(_translate("TranslateApp", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.textEdit.setPlaceholderText(_translate("TranslateApp", "Enter text"))
        self.pushButton.setText(_translate("TranslateApp", "Dịch"))
        self.comboBox.setItemText(0, _translate("TranslateApp", "Tiếng Anh"))
        self.comboBox.setItemText(1, _translate("TranslateApp", "Tiếng Việt"))
        self.comboBox.setItemText(2, _translate("TranslateApp", "Tiếng Trung"))
        self.comboBox.setItemText(3, _translate("TranslateApp", "Tiếng Nhật"))
        self.comboBox.setItemText(4, _translate("TranslateApp", "Tiếng Hàn"))
        self.comboBox_2.setItemText(0, _translate("TranslateApp", "Tiếng Anh"))
        self.comboBox_2.setItemText(1, _translate("TranslateApp", "Tiếng Việt"))
        self.comboBox_2.setItemText(2, _translate("TranslateApp", "Tiếng Trung"))
        self.comboBox_2.setItemText(3, _translate("TranslateApp", "Tiếng Nhật"))
        self.comboBox_2.setItemText(4, _translate("TranslateApp", "Tiếng Hàn"))

from . import new_rc