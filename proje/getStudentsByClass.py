# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'getStudentsByClass.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_GetStudents(object):
    def setupUi(self, GetStudents):
        GetStudents.setObjectName("GetStudents")
        GetStudents.resize(800, 644)
        self.centralwidget = QtWidgets.QWidget(GetStudents)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(-1, 0, 801, 651))
        self.widget.setToolTipDuration(-1)
        self.widget.setStyleSheet("background-color: rgb(234, 215, 187);")
        self.widget.setObjectName("widget")
        self.get_students_comboBox = QtWidgets.QComboBox(self.widget)
        self.get_students_comboBox.setGeometry(QtCore.QRect(220, 120, 211, 41))
        self.get_students_comboBox.setToolTipDuration(-1)
        self.get_students_comboBox.setStyleSheet("background-color: rgb(234, 215, 187);\n"
"font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 242, 216);")
        self.get_students_comboBox.setCurrentText("")
        self.get_students_comboBox.setObjectName("get_students_comboBox")
        self.get_students_table = QtWidgets.QTableWidget(self.widget)
        self.get_students_table.setGeometry(QtCore.QRect(20, 250, 741, 311))
        self.get_students_table.setStyleSheet("font: 75 10pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 242, 216);\n"
"font: 75 12pt \"MS Shell Dlg 2\";")
        self.get_students_table.setObjectName("get_students_table")
        self.get_students_table.setColumnCount(5)
        self.get_students_table.setRowCount(1)
        item = QtWidgets.QTableWidgetItem()
        self.get_students_table.setVerticalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.get_students_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.get_students_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.get_students_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.get_students_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.get_students_table.setHorizontalHeaderItem(4, item)
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(90, 220, 47, 13))
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.rehberlik_hoca_lbl = QtWidgets.QLabel(self.widget)
        self.rehberlik_hoca_lbl.setGeometry(QtCore.QRect(380, 580, 261, 51))
        self.rehberlik_hoca_lbl.setStyleSheet("font: 75 20pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(17, 57, 70);\n"
"color: rgb(255, 255, 255);")
        self.rehberlik_hoca_lbl.setObjectName("rehberlik_hoca_lbl")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(180, 20, 401, 51))
        self.widget_2.setStyleSheet("background-color: rgb(17, 57, 70);")
        self.widget_2.setObjectName("widget_2")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(20, 10, 371, 31))
        self.label_5.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 20pt \"MS Shell Dlg 2\";\n"
"")
        self.label_5.setObjectName("label_5")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(50, 120, 151, 41))
        self.widget_3.setStyleSheet("background-color: rgb(17, 57, 70);")
        self.widget_3.setObjectName("widget_3")
        self.label = QtWidgets.QLabel(self.widget_3)
        self.label.setGeometry(QtCore.QRect(10, -10, 151, 61))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(25)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);\n"
"font: 75 25pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(30, 210, 391, 31))
        self.widget_4.setStyleSheet("background-color: rgb(17, 57, 70);")
        self.widget_4.setObjectName("widget_4")
        self.label_4 = QtWidgets.QLabel(self.widget_4)
        self.label_4.setGeometry(QtCore.QRect(0, -10, 381, 51))
        font = QtGui.QFont()
        font.setFamily("MS Shell Dlg 2")
        font.setPointSize(12)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(9)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("font: 75 12pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_4.setObjectName("label_4")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(50, 580, 311, 51))
        self.widget_5.setStyleSheet("background-color: rgb(17, 57, 70);")
        self.widget_5.setObjectName("widget_5")
        self.label_2 = QtWidgets.QLabel(self.widget_5)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 311, 51))
        self.label_2.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        GetStudents.setCentralWidget(self.centralwidget)

        self.retranslateUi(GetStudents)
        self.get_students_comboBox.setCurrentIndex(-1)
        QtCore.QMetaObject.connectSlotsByName(GetStudents)

    def retranslateUi(self, GetStudents):
        _translate = QtCore.QCoreApplication.translate
        GetStudents.setWindowTitle(_translate("GetStudents", "Sınıf öğrencileri arama sayfası"))
        item = self.get_students_table.horizontalHeaderItem(0)
        item.setText(_translate("GetStudents", "Numara"))
        item = self.get_students_table.horizontalHeaderItem(1)
        item.setText(_translate("GetStudents", "Ad"))
        item = self.get_students_table.horizontalHeaderItem(2)
        item.setText(_translate("GetStudents", "Soyad"))
        item = self.get_students_table.horizontalHeaderItem(3)
        item.setText(_translate("GetStudents", "Doğum tarihi"))
        item = self.get_students_table.horizontalHeaderItem(4)
        item.setText(_translate("GetStudents", "Cinsiyet"))
        self.rehberlik_hoca_lbl.setText(_translate("GetStudents", " "))
        self.label_5.setText(_translate("GetStudents", "Sınıf öğrencileri arama sayfası"))
        self.label.setText(_translate("GetStudents", "Sınıflar :"))
        self.label_4.setText(_translate("GetStudents", " Belirlediğiniz sınıfa göre tüm öğrencilerin bilgileri :"))
        self.label_2.setText(_translate("GetStudents", " Bu sınıftan sorumlu öğretmen :"))
