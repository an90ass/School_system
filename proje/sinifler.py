# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sinifler.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Sinifler(object):
    def setupUi(self, Sinifler):
        Sinifler.setObjectName("Sinifler")
        Sinifler.resize(602, 563)
        self.centralwidget = QtWidgets.QWidget(Sinifler)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 1091, 651))
        self.widget.setStyleSheet("background-color: rgb(171, 216, 255);\n"
"background-color: rgb(234, 215, 187);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.widget.setObjectName("widget")
        self.table_getStudentByName = QtWidgets.QTableWidget(self.widget)
        self.table_getStudentByName.setGeometry(QtCore.QRect(60, 80, 491, 441))
        self.table_getStudentByName.setMinimumSize(QtCore.QSize(0, 0))
        self.table_getStudentByName.setObjectName("table_getStudentByName")
        self.table_getStudentByName.setColumnCount(2)
        self.table_getStudentByName.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_getStudentByName.setHorizontalHeaderItem(1, item)
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
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(180, 20, 241, 41))
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
        self.widget_4 = QtWidgets.QWidget(self.widget_3)
        self.widget_4.setGeometry(QtCore.QRect(-20, 0, 241, 41))
        self.widget_4.setStyleSheet("background-color: rgb(17, 57, 70);")
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(90, 0, 201, 41))
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.widget_5 = QtWidgets.QWidget(self.widget_4)
        self.widget_5.setGeometry(QtCore.QRect(80, 0, 151, 41))
        self.widget_5.setStyleSheet("background-color: rgb(17, 57, 70);")
        self.widget_5.setObjectName("widget_5")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(60, 0, 171, 41))
        self.label_5.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        Sinifler.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Sinifler)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 602, 21))
        self.menubar.setObjectName("menubar")
        Sinifler.setMenuBar(self.menubar)

        self.retranslateUi(Sinifler)
        QtCore.QMetaObject.connectSlotsByName(Sinifler)

    def retranslateUi(self, Sinifler):
        _translate = QtCore.QCoreApplication.translate
        Sinifler.setWindowTitle(_translate("Sinifler", "Sinifler"))
        item = self.table_getStudentByName.verticalHeaderItem(0)
        item.setText(_translate("Sinifler", "#"))
        item = self.table_getStudentByName.horizontalHeaderItem(0)
        item.setText(_translate("Sinifler", "Sınıf"))
        item = self.table_getStudentByName.horizontalHeaderItem(1)
        item.setText(_translate("Sinifler", "Sorumlu öğretmen"))
        __sortingEnabled = self.table_getStudentByName.isSortingEnabled()
        self.table_getStudentByName.setSortingEnabled(False)
        self.table_getStudentByName.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Sinifler", "Öğrenciler"))
        self.label_3.setText(_translate("Sinifler", "Sınıflar"))
        self.label_4.setText(_translate("Sinifler", "Öğrenciler"))
        self.label_5.setText(_translate("Sinifler", "Sınıflar"))
