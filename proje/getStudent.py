# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getStudent.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GetStudent(object):
    def setupUi(self, GetStudent):
        GetStudent.setObjectName("GetStudent")
        GetStudent.resize(800, 375)
        self.centralwidget = QtWidgets.QWidget(GetStudent)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 0, 801, 371))
        self.widget.setStyleSheet("background-color: rgb(171, 216, 255);\n"
"background-color: rgb(234, 215, 187);\n"
"font: 14pt \"MS Shell Dlg 2\";")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 90, 301, 41))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(14)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.student_name = QtWidgets.QTextEdit(self.widget)
        self.student_name.setGeometry(QtCore.QRect(350, 100, 261, 31))
        self.student_name.setObjectName("student_name")
        self.Ok = QtWidgets.QPushButton(self.widget)
        self.Ok.setGeometry(QtCore.QRect(320, 320, 131, 31))
        self.Ok.setStyleSheet("background-color: rgb(17, 57, 70);\n"
"color: rgb(255, 255, 255);")
        self.Ok.setObjectName("Ok")
        self.table_getStudentByName = QtWidgets.QTableWidget(self.widget)
        self.table_getStudentByName.setGeometry(QtCore.QRect(30, 180, 741, 111))
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
        self.widget_2.setGeometry(QtCore.QRect(300, 20, 301, 41))
        self.widget_2.setStyleSheet("background-color: rgb(17, 57, 70);")
        self.widget_2.setObjectName("widget_2")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(50, 0, 201, 41))
        self.label_2.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"font: 75 16pt \"MS Shell Dlg 2\";\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        GetStudent.setCentralWidget(self.centralwidget)

        self.retranslateUi(GetStudent)
        QtCore.QMetaObject.connectSlotsByName(GetStudent)

    def retranslateUi(self, GetStudent):
        _translate = QtCore.QCoreApplication.translate
        GetStudent.setWindowTitle(_translate("GetStudent", "Tek öğrenci için arama"))
        self.label.setText(_translate("GetStudent", "Öğrencinin adı (ya da numarası) :"))
        self.Ok.setText(_translate("GetStudent", "Ara"))
        item = self.table_getStudentByName.verticalHeaderItem(0)
        item.setText(_translate("GetStudent", "#"))
        item = self.table_getStudentByName.horizontalHeaderItem(0)
        item.setText(_translate("GetStudent", "Öğrenci numarası"))
        item = self.table_getStudentByName.horizontalHeaderItem(1)
        item.setText(_translate("GetStudent", "Ad"))
        item = self.table_getStudentByName.horizontalHeaderItem(2)
        item.setText(_translate("GetStudent", "Soyad"))
        item = self.table_getStudentByName.horizontalHeaderItem(3)
        item.setText(_translate("GetStudent", "Doğum tarihi"))
        item = self.table_getStudentByName.horizontalHeaderItem(4)
        item.setText(_translate("GetStudent", "Cinsiyet"))
        item = self.table_getStudentByName.horizontalHeaderItem(5)
        item.setText(_translate("GetStudent", "Sınıf adı"))
        __sortingEnabled = self.table_getStudentByName.isSortingEnabled()
        self.table_getStudentByName.setSortingEnabled(False)
        self.table_getStudentByName.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("GetStudent", "Öğrenci arama sayfası"))
