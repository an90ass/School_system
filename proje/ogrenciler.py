# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ogrenciler.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Ogrenciler(object):
    def setupUi(self, Ogrenciler):
        Ogrenciler.setObjectName("Ogrenciler")
        Ogrenciler.resize(1092, 610)
        self.centralwidget = QtWidgets.QWidget(Ogrenciler)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1091, 651))
        self.widget.setStyleSheet("background-color: rgb(171, 216, 255);\n"
"background-color: rgb(234, 215, 187);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.widget.setObjectName("widget")
        self.table_getStudentByName = QtWidgets.QTableWidget(self.widget)
        self.table_getStudentByName.setGeometry(QtCore.QRect(30, 110, 1051, 441))
        self.table_getStudentByName.setMinimumSize(QtCore.QSize(0, 0))
        self.table_getStudentByName.setObjectName("table_getStudentByName")
        self.table_getStudentByName.setColumnCount(6)
        self.table_getStudentByName.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable)
        self.table_getStudentByName.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable)
        self.table_getStudentByName.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable)
        self.table_getStudentByName.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setFlags(QtCore.Qt.ItemIsSelectable)
        self.table_getStudentByName.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        item.setFont(font)
        item.setFlags(QtCore.Qt.ItemIsSelectable)
        self.table_getStudentByName.setItem(0, 4, item)
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(380, 20, 241, 41))
        self.widget_2.setStyleSheet("background-color: rgb(17, 57, 70);")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(90, 0, 201, 41))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.widget_3 = QtWidgets.QWidget(self.widget_2)
        self.widget_3.setGeometry(QtCore.QRect(80, 0, 151, 41))
        self.widget_3.setStyleSheet("background-color: rgb(17, 57, 70);")
        self.widget_3.setObjectName("widget_3")
        self.label_3 = QtWidgets.QLabel(self.widget_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 201, 41))
        self.label_3.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        Ogrenciler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ogrenciler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1092, 21))
        self.menubar.setObjectName("menubar")
        Ogrenciler.setMenuBar(self.menubar)

        self.retranslateUi(Ogrenciler)
        QtCore.QMetaObject.connectSlotsByName(Ogrenciler)

    def retranslateUi(self, Ogrenciler):
        _translate = QtCore.QCoreApplication.translate
        Ogrenciler.setWindowTitle(_translate("Ogrenciler", "Ogrenciler"))
        item = self.table_getStudentByName.verticalHeaderItem(0)
        item.setText(_translate("Ogrenciler", "#"))
        item = self.table_getStudentByName.horizontalHeaderItem(0)
        item.setText(_translate("Ogrenciler", "Öğrenci numarası"))
        item = self.table_getStudentByName.horizontalHeaderItem(1)
        item.setText(_translate("Ogrenciler", "Ad"))
        item = self.table_getStudentByName.horizontalHeaderItem(2)
        item.setText(_translate("Ogrenciler", "Soyad"))
        item = self.table_getStudentByName.horizontalHeaderItem(3)
        item.setText(_translate("Ogrenciler", "Doğum tarihi"))
        item = self.table_getStudentByName.horizontalHeaderItem(4)
        item.setText(_translate("Ogrenciler", "Cinsiyet"))
        item = self.table_getStudentByName.horizontalHeaderItem(5)
        item.setText(_translate("Ogrenciler", "Sınıf adı"))
        __sortingEnabled = self.table_getStudentByName.isSortingEnabled()
        self.table_getStudentByName.setSortingEnabled(False)
        self.table_getStudentByName.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Ogrenciler", "Öğrenciler"))
        self.label_3.setText(_translate("Ogrenciler", "Öğrenciler"))
