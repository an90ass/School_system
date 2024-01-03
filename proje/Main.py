# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Main.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(938, 656)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(0, 0, 941, 641))
        self.widget.setStyleSheet("background-color: rgb(188, 163, 127);")
        self.widget.setObjectName("widget")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(70, 30, 821, 571))
        self.widget_2.setStyleSheet("background-color: rgb(234, 215, 187);")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(self.widget_2)
        self.label.setGeometry(QtCore.QRect(290, 10, 261, 61))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(200, 90, 461, 71))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: rgb(17, 57, 70);\n"
"color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.widget_2)
        self.label_3.setGeometry(QtCore.QRect(290, 170, 241, 51))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: rgb(17, 57, 70);\n"
"color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(90, 260, 611, 181))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.widget_2)
        self.label_6.setGeometry(QtCore.QRect(10, 490, 511, 71))
        font = QtGui.QFont()
        font.setFamily("Monotype Corsiva")
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet("background-color: rgb(17, 57, 70);\n"
"color: rgb(255, 255, 255);")
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 938, 21))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menuSorgulama = QtWidgets.QMenu(self.menu)
        font = QtGui.QFont()
        font.setFamily("Segoe UI")
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.menuSorgulama.setFont(font)
        self.menuSorgulama.setObjectName("menuSorgulama")
        self.menuE_itmen_i_lemleri = QtWidgets.QMenu(self.menubar)
        self.menuE_itmen_i_lemleri.setObjectName("menuE_itmen_i_lemleri")
        self.menuSinif_i_lemleri = QtWidgets.QMenu(self.menubar)
        self.menuSinif_i_lemleri.setObjectName("menuSinif_i_lemleri")
        self.sinif_ad_ile_sorgulama = QtWidgets.QMenu(self.menuSinif_i_lemleri)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.sinif_ad_ile_sorgulama.setFont(font)
        self.sinif_ad_ile_sorgulama.setObjectName("sinif_ad_ile_sorgulama")
        self.menuDers_i_lemleri = QtWidgets.QMenu(self.menubar)
        self.menuDers_i_lemleri.setObjectName("menuDers_i_lemleri")
        self.action_ekle_si_deg = QtWidgets.QMenu(self.menuDers_i_lemleri)
        self.action_ekle_si_deg.setObjectName("action_ekle_si_deg")
        MainWindow.setMenuBar(self.menubar)
        self.action_ogrenci_islemleri = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_ogrenci_islemleri.setFont(font)
        self.action_ogrenci_islemleri.setObjectName("action_ogrenci_islemleri")
        self.action_ogrenci_sorgulamasi = QtWidgets.QAction(MainWindow)
        self.action_ogrenci_sorgulamasi.setObjectName("action_ogrenci_sorgulamasi")
        self.sinif_ogrencilerin_sorgulamasi = QtWidgets.QAction(MainWindow)
        self.sinif_ogrencilerin_sorgulamasi.setObjectName("sinif_ogrencilerin_sorgulamasi")
        self.action_egitmen_islemleri = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.action_egitmen_islemleri.setFont(font)
        self.action_egitmen_islemleri.setObjectName("action_egitmen_islemleri")
        self.action_sinif_islemleri = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_sinif_islemleri.setFont(font)
        self.action_sinif_islemleri.setObjectName("action_sinif_islemleri")
        self.actionSinif_ogrencilerin_sorgulamas = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionSinif_ogrencilerin_sorgulamas.setFont(font)
        self.actionSinif_ogrencilerin_sorgulamas.setObjectName("actionSinif_ogrencilerin_sorgulamas")
        self.actionDers_silme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionDers_silme.setFont(font)
        self.actionDers_silme.setObjectName("actionDers_silme")
        self.actionDers_duzenleme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionDers_duzenleme.setFont(font)
        self.actionDers_duzenleme.setObjectName("actionDers_duzenleme")
        self.actionSinifin_sorumlusu_degistir = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionSinifin_sorumlusu_degistir.setFont(font)
        self.actionSinifin_sorumlusu_degistir.setObjectName("actionSinifin_sorumlusu_degistir")
        self.actionDers_Ekleme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionDers_Ekleme.setFont(font)
        self.actionDers_Ekleme.setObjectName("actionDers_Ekleme")
        self.actionDers_Silme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionDers_Silme.setFont(font)
        self.actionDers_Silme.setObjectName("actionDers_Silme")
        self.actionDers_Duzenleme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionDers_Duzenleme.setFont(font)
        self.actionDers_Duzenleme.setObjectName("actionDers_Duzenleme")
        self.actionDersi_veren_ogretmeni_degistirme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionDersi_veren_ogretmeni_degistirme.setFont(font)
        self.actionDersi_veren_ogretmeni_degistirme.setObjectName("actionDersi_veren_ogretmeni_degistirme")
        self.actionSinifin_dersleri = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionSinifin_dersleri.setFont(font)
        self.actionSinifin_dersleri.setObjectName("actionSinifin_dersleri")
        self.action_ogretmen_verdigi_dersler = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_ogretmen_verdigi_dersler.setFont(font)
        self.action_ogretmen_verdigi_dersler.setObjectName("action_ogretmen_verdigi_dersler")
        self.actionDers_bilgilerini_arama = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionDers_bilgilerini_arama.setFont(font)
        self.actionDers_bilgilerini_arama.setObjectName("actionDers_bilgilerini_arama")
        self.actionOgrenci_notlarini_girme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionOgrenci_notlarini_girme.setFont(font)
        self.actionOgrenci_notlarini_girme.setObjectName("actionOgrenci_notlarini_girme")
        self.action_ogrenci_notlarini_degistirme = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_ogrenci_notlarini_degistirme.setFont(font)
        self.action_ogrenci_notlarini_degistirme.setObjectName("action_ogrenci_notlarini_degistirme")
        self.action_ogrenciler = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_ogrenciler.setFont(font)
        self.action_ogrenciler.setObjectName("action_ogrenciler")
        self.action_ogretmenler = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.action_ogretmenler.setFont(font)
        self.action_ogretmenler.setObjectName("action_ogretmenler")
        self.actionSiniflar = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.actionSiniflar.setFont(font)
        self.actionSiniflar.setObjectName("actionSiniflar")
        self.menuSorgulama.addAction(self.action_ogrenci_sorgulamasi)
        self.menu.addAction(self.action_ogrenciler)
        self.menu.addAction(self.action_ogrenci_islemleri)
        self.menu.addAction(self.menuSorgulama.menuAction())
        self.menu.addAction(self.actionOgrenci_notlarini_girme)
        self.menu.addAction(self.action_ogrenci_notlarini_degistirme)
        self.menuE_itmen_i_lemleri.addAction(self.action_ogretmenler)
        self.menuE_itmen_i_lemleri.addAction(self.action_egitmen_islemleri)
        self.menuE_itmen_i_lemleri.addAction(self.action_ogretmen_verdigi_dersler)
        self.sinif_ad_ile_sorgulama.addAction(self.actionSinif_ogrencilerin_sorgulamas)
        self.menuSinif_i_lemleri.addAction(self.actionSiniflar)
        self.menuSinif_i_lemleri.addAction(self.action_sinif_islemleri)
        self.menuSinif_i_lemleri.addAction(self.sinif_ad_ile_sorgulama.menuAction())
        self.menuSinif_i_lemleri.addAction(self.actionSinifin_sorumlusu_degistir)
        self.menuSinif_i_lemleri.addAction(self.actionSinifin_dersleri)
        self.action_ekle_si_deg.addAction(self.actionDers_Ekleme)
        self.action_ekle_si_deg.addAction(self.actionDers_Silme)
        self.action_ekle_si_deg.addAction(self.actionDers_Duzenleme)
        self.menuDers_i_lemleri.addAction(self.action_ekle_si_deg.menuAction())
        self.menuDers_i_lemleri.addAction(self.actionDersi_veren_ogretmeni_degistirme)
        self.menuDers_i_lemleri.addAction(self.actionDers_bilgilerini_arama)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuE_itmen_i_lemleri.menuAction())
        self.menubar.addAction(self.menuSinif_i_lemleri.menuAction())
        self.menubar.addAction(self.menuDers_i_lemleri.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Ana Sayfa"))
        self.label.setText(_translate("MainWindow", "Okul veri tabanı"))
        self.label_2.setText(_translate("MainWindow", "[Anas Eskander AL-Maqtari]"))
        self.label_3.setText(_translate("MainWindow", "[21670310176]"))
        self.label_5.setText(_translate("MainWindow", "                       BSM303\n"
"          Veritabanı Yönetim Sistemleri\n"
"                     Final Ödevi\n"
""))
        self.label_6.setText(_translate("MainWindow", "Dr. Öğr. Üyesi Bayram AKGÜL"))
        self.menu.setTitle(_translate("MainWindow", "Öğrenci işlemleri"))
        self.menuSorgulama.setTitle(_translate("MainWindow", "Öğrenci No ile Sorgulama"))
        self.menuE_itmen_i_lemleri.setTitle(_translate("MainWindow", "Öğretmen işlemleri"))
        self.menuSinif_i_lemleri.setTitle(_translate("MainWindow", "Sinif işlemleri"))
        self.sinif_ad_ile_sorgulama.setTitle(_translate("MainWindow", "Sınıf adı ile sorgulama"))
        self.menuDers_i_lemleri.setTitle(_translate("MainWindow", "Ders işlemleri"))
        self.action_ekle_si_deg.setTitle(_translate("MainWindow", "Ekleme - Silme - Düzenleme"))
        self.action_ogrenci_islemleri.setText(_translate("MainWindow", "Ekleme-Silme-Düzenleme"))
        self.action_ogrenci_sorgulamasi.setText(_translate("MainWindow", "Öğrenci sorgulaması"))
        self.sinif_ogrencilerin_sorgulamasi.setText(_translate("MainWindow", "Sınıf öğrencilerin sorgulaması"))
        self.action_egitmen_islemleri.setText(_translate("MainWindow", "Ekleme-Silme-Düzenleme"))
        self.action_sinif_islemleri.setText(_translate("MainWindow", "Ekleme-Silme-Düzenleme"))
        self.actionSinif_ogrencilerin_sorgulamas.setText(_translate("MainWindow", "Sınıf öğrencilerin sorgulaması"))
        self.actionDers_silme.setText(_translate("MainWindow", "Ders silme"))
        self.actionDers_duzenleme.setText(_translate("MainWindow", "Ders düzenleme"))
        self.actionSinifin_sorumlusu_degistir.setText(_translate("MainWindow", "Sınıfın sorumlusu değiştirme"))
        self.actionDers_Ekleme.setText(_translate("MainWindow", "Ders Ekleme"))
        self.actionDers_Silme.setText(_translate("MainWindow", "Ders Silme"))
        self.actionDers_Duzenleme.setText(_translate("MainWindow", "Ders Düzenleme"))
        self.actionDersi_veren_ogretmeni_degistirme.setText(_translate("MainWindow", "Dersi veren öğretmeni değiştirme"))
        self.actionSinifin_dersleri.setText(_translate("MainWindow", "Sınıfın dersleri"))
        self.action_ogretmen_verdigi_dersler.setText(_translate("MainWindow", "Öğretmen verdiği dersler"))
        self.actionDers_bilgilerini_arama.setText(_translate("MainWindow", "Ders bilgilerini arama"))
        self.actionOgrenci_notlarini_girme.setText(_translate("MainWindow", "Öğrenci notlarını girme"))
        self.action_ogrenci_notlarini_degistirme.setText(_translate("MainWindow", "Öğrenci notlarını değiştirme"))
        self.action_ogrenciler.setText(_translate("MainWindow", "Öğrenciler"))
        self.action_ogretmenler.setText(_translate("MainWindow", "Öğretmenler"))
        self.actionSiniflar.setText(_translate("MainWindow", "Sınıflar"))
