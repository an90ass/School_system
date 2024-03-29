# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'egitmen_dersleri.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ogretmenDersleri(object):
    def setupUi(self, ogretmenDersleri):
        ogretmenDersleri.setObjectName("ogretmenDersleri")
        ogretmenDersleri.resize(578, 584)
        self.centralwidget = QtWidgets.QWidget(ogretmenDersleri)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 921, 611))
        self.widget.setStyleSheet("background-color: rgb(188, 163, 127);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(50, 100, 211, 41))
        self.label.setStyleSheet("background-color: rgb(234, 215, 187);\n"
"font: 75 16pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.teacher_number_text = QtWidgets.QPlainTextEdit(self.widget)
        self.teacher_number_text.setGeometry(QtCore.QRect(280, 100, 231, 41))
        self.teacher_number_text.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(234, 215, 187);")
        self.teacher_number_text.setObjectName("teacher_number_text")
        self.gosterbtn = QtWidgets.QPushButton(self.widget)
        self.gosterbtn.setGeometry(QtCore.QRect(210, 520, 151, 41))
        self.gosterbtn.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.gosterbtn.setObjectName("gosterbtn")
        self.teacherDersTable = QtWidgets.QTableWidget(self.widget)
        self.teacherDersTable.setGeometry(QtCore.QRect(50, 170, 491, 321))
        self.teacherDersTable.setStyleSheet("font: 75 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(234, 215, 187);")
        self.teacherDersTable.setObjectName("teacherDersTable")
        self.teacherDersTable.setColumnCount(2)
        self.teacherDersTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.teacherDersTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.teacherDersTable.setHorizontalHeaderItem(1, item)
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(210, 20, 231, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(234, 215, 187);")
        self.label_2.setObjectName("label_2")
        ogretmenDersleri.setCentralWidget(self.centralwidget)

        self.retranslateUi(ogretmenDersleri)
        QtCore.QMetaObject.connectSlotsByName(ogretmenDersleri)

    def retranslateUi(self, ogretmenDersleri):
        _translate = QtCore.QCoreApplication.translate
        ogretmenDersleri.setWindowTitle(_translate("ogretmenDersleri", "Öğretmen derslerini"))
        self.label.setText(_translate("ogretmenDersleri", " Öğretmen numarası :"))
        self.gosterbtn.setText(_translate("ogretmenDersleri", "Göster"))
        item = self.teacherDersTable.horizontalHeaderItem(0)
        item.setText(_translate("ogretmenDersleri", "Ders"))
        item = self.teacherDersTable.horizontalHeaderItem(1)
        item.setText(_translate("ogretmenDersleri", "Sınıf"))
        self.label_2.setText(_translate("ogretmenDersleri", " Öğretmen dersleri"))
