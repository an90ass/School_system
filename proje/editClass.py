# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editClass.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_edit_class(object):
    def setupUi(self, edit_class):
        edit_class.setObjectName("edit_class")
        edit_class.resize(530, 392)
        self.centralwidget = QtWidgets.QWidget(edit_class)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 551, 641))
        self.widget.setStyleSheet("background-color: rgb(230, 255, 107);\n"
"background-color: rgb(234, 215, 187);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(10, 10, 511, 371))
        self.widget_2.setStyleSheet("background-color: rgb(188, 163, 127);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(50, 120, 101, 16))
        self.label.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.class_combo = QtWidgets.QComboBox(self.widget_2)
        self.class_combo.setGeometry(QtCore.QRect(260, 120, 151, 21))
        self.class_combo.setObjectName("class_combo")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(150, 280, 221, 31))
        self.pushButton.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 170, 0);")
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(150, 10, 271, 61))
        self.label_4.setStyleSheet("font: 75 16pt \"MS Shell Dlg 2\";")
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(40, 200, 131, 16))
        self.label_5.setStyleSheet("font: 75 14pt \"MS Shell Dlg 2\";")
        self.label_5.setObjectName("label_5")
        self.new_class_name = QtWidgets.QPlainTextEdit(self.widget_2)
        self.new_class_name.setGeometry(QtCore.QRect(260, 190, 141, 21))
        self.new_class_name.setObjectName("new_class_name")
        edit_class.setCentralWidget(self.centralwidget)

        self.retranslateUi(edit_class)
        QtCore.QMetaObject.connectSlotsByName(edit_class)

    def retranslateUi(self, edit_class):
        _translate = QtCore.QCoreApplication.translate
        edit_class.setWindowTitle(_translate("edit_class", "Sınıf degistirme"))
        self.label.setText(_translate("edit_class", "Sınıf adı :"))
        self.pushButton.setText(_translate("edit_class", "Degistir"))
        self.label_4.setText(_translate("edit_class", "Sinif değistirme sayfasi"))
        self.label_5.setText(_translate("edit_class", "Yeni Sınıf adı :"))