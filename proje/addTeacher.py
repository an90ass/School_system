# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addTeacher.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddTeacher(object):
    def setupUi(self, AddTeacher):
        AddTeacher.setObjectName("AddTeacher")
        AddTeacher.resize(464, 495)
        self.centralwidget = QtWidgets.QWidget(AddTeacher)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 911, 641))
        self.widget.setStyleSheet("background-color: rgb(188, 163, 127);")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 140, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: rgb(234, 215, 187);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(40, 190, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(234, 215, 187);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(40, 250, 131, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(234, 215, 187);")
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setGeometry(QtCore.QRect(40, 330, 91, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("background-color: rgb(234, 215, 187);")
        self.label_4.setObjectName("label_4")
        self.teacher_name = QtWidgets.QTextEdit(self.widget)
        self.teacher_name.setGeometry(QtCore.QRect(180, 140, 261, 31))
        self.teacher_name.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(234, 215, 187);")
        self.teacher_name.setObjectName("teacher_name")
        self.teacher_surname = QtWidgets.QTextEdit(self.widget)
        self.teacher_surname.setGeometry(QtCore.QRect(180, 190, 261, 31))
        self.teacher_surname.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(234, 215, 187);")
        self.teacher_surname.setObjectName("teacher_surname")
        self.groupBox = QtWidgets.QGroupBox(self.widget)
        self.groupBox.setGeometry(QtCore.QRect(180, 280, 271, 101))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.erkek = QtWidgets.QRadioButton(self.groupBox)
        self.erkek.setGeometry(QtCore.QRect(20, 60, 82, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.erkek.setFont(font)
        self.erkek.setObjectName("erkek")
        self.kadin = QtWidgets.QRadioButton(self.groupBox)
        self.kadin.setGeometry(QtCore.QRect(150, 60, 111, 17))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.kadin.setFont(font)
        self.kadin.setObjectName("kadin")
        self.add_btn = QtWidgets.QPushButton(self.widget)
        self.add_btn.setGeometry(QtCore.QRect(150, 420, 201, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.add_btn.setFont(font)
        self.add_btn.setStyleSheet("background-color: rgb(0, 170, 0);\n"
"color: rgb(255, 255, 255);")
        self.add_btn.setObjectName("add_btn")
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setGeometry(QtCore.QRect(100, 10, 281, 41))
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet("background-color: rgb(234, 215, 187);")
        self.label_11.setObjectName("label_11")
        self.teacher_birthdate = QtWidgets.QDateTimeEdit(self.widget)
        self.teacher_birthdate.setGeometry(QtCore.QRect(180, 250, 261, 31))
        self.teacher_birthdate.setStyleSheet("background-color: rgb(234, 215, 187);\n"
"font: 75 14pt \"MS Shell Dlg 2\";")
        self.teacher_birthdate.setObjectName("teacher_birthdate")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 90, 101, 21))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(234, 215, 187);")
        self.label_6.setObjectName("label_6")
        self.teacher_number = QtWidgets.QTextEdit(self.widget)
        self.teacher_number.setGeometry(QtCore.QRect(180, 90, 261, 31))
        self.teacher_number.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(234, 215, 187);")
        self.teacher_number.setObjectName("teacher_number")
        AddTeacher.setCentralWidget(self.centralwidget)

        self.retranslateUi(AddTeacher)
        QtCore.QMetaObject.connectSlotsByName(AddTeacher)

    def retranslateUi(self, AddTeacher):
        _translate = QtCore.QCoreApplication.translate
        AddTeacher.setWindowTitle(_translate("AddTeacher", " Öğretmen Ekleme sayfası"))
        self.label.setText(_translate("AddTeacher", " Ad :"))
        self.label_2.setText(_translate("AddTeacher", " Soyad :"))
        self.label_3.setText(_translate("AddTeacher", " Doğum  tarihi :"))
        self.label_4.setText(_translate("AddTeacher", " Cinsiyet :"))
        self.erkek.setText(_translate("AddTeacher", "Erkek"))
        self.kadin.setText(_translate("AddTeacher", "Kadın"))
        self.add_btn.setText(_translate("AddTeacher", "Kaydet"))
        self.label_11.setText(_translate("AddTeacher", " Öğretmen Ekleme sayfası"))
        self.label_6.setText(_translate("AddTeacher", " Numara:"))
