from tkinter import dialog
from Main import Ui_MainWindow
from PyQt5 import QtWidgets,QtCore
import dbmanager 
import addStudent2
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog
import ogrenci_islemleri2
import egitmen_islemleri2 
import getStudent2
import sinif_dersleri2
import getStudentsByClassName2
import ders_ekleme2
import  ders_degistirme2
import sinif_islemleri2,sinif_sorumlusu_degistirme2,ders_bilgilerini_arama2
import verenDersOgretmentDegistirme2
import egitmen_dersleri2
import ogrenci_puanlari2
import ogrenci_puanlari_edit2
import ogrenciler2
import ogretmenler2
import sinifler2
from Lesson import Lesson
from dbmanager import DbManager
from PyQt5.QtWidgets import QMessageBox
class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # ogrenci ekleme sileme duzenleme 
        action_ogrenci_islemleri = self.findChild(QtWidgets.QAction, "action_ogrenci_islemleri")
        if action_ogrenci_islemleri:
            action_ogrenci_islemleri.triggered.connect(self.ogrenci_islemleri)

         # ogrenci no ile sorgulama
        action_ogrenci_sorgulamasi = self.findChild(QtWidgets.QAction, "action_ogrenci_sorgulamasi")
        if action_ogrenci_sorgulamasi:
            action_ogrenci_sorgulamasi.triggered.connect(self.ogrenci_sorgulama)
        # Dersi veren ogretmeni degistirme
        actionDersi_veren_ogretmeni_degistirme = self.findChild(QtWidgets.QAction, "actionDersi_veren_ogretmeni_degistirme")
        if actionDersi_veren_ogretmeni_degistirme:
            actionDersi_veren_ogretmeni_degistirme.triggered.connect(self.Dersi_veren_ogretmeni_degistirme)

       # Egitmen islemeleri
        action_egitmen_islemleri = self.findChild(QtWidgets.QAction, "action_egitmen_islemleri")
        if action_egitmen_islemleri:
                    action_egitmen_islemleri.triggered.connect(self.egitmen_islemleri)

         # sinif islemeleri
        action_sinif_islemleri = self.findChild(QtWidgets.QAction, "action_sinif_islemleri")
        if action_sinif_islemleri:
                    action_sinif_islemleri.triggered.connect(self.sinif_islemleri)
        # sinifin sorumlusu degistirme  
        actionSinifin_sorumlusu_degistir = self.findChild(QtWidgets.QAction, "actionSinifin_sorumlusu_degistir")
        if action_ogrenci_islemleri:
            actionSinifin_sorumlusu_degistir.triggered.connect(self.actionSinifin_sorumlusu_degistir)

        #  sinif ogrencilerin sorgulama sinif adi ile ogrencileri getirme 
        action_sinif_ogrencilerin_sorgulamasi = self.findChild(QtWidgets.QAction, "actionSinif_ogrencilerin_sorgulamas")
        if action_sinif_ogrencilerin_sorgulamasi:
            action_sinif_ogrencilerin_sorgulamasi.triggered.connect(self.sinif_ogrencilerin_sorgulamasi)

         #   ogrenci ders notlarini girme
        actionOgrenci_notlarini_girme = self.findChild(QtWidgets.QAction, "actionOgrenci_notlarini_girme")
        if actionOgrenci_notlarini_girme:
            actionOgrenci_notlarini_girme.triggered.connect(self.Ogrenci_notlarini_girme)
         #  ogrenci ders notlarini değiştirme
        action_ogrenci_notlarini_degistirme = self.findChild(QtWidgets.QAction, "action_ogrenci_notlarini_degistirme")
        if action_ogrenci_notlarini_degistirme:
            action_ogrenci_notlarini_degistirme.triggered.connect(self.ogrenci_notlarini_degistirme)






        # Ders ekleme  
        actionDers_ekleme = self.findChild(QtWidgets.QAction, "actionDers_Ekleme")
        if actionDers_ekleme:
            actionDers_ekleme.triggered.connect(self.ders_ekleme)
        # Ders silme  
        actionDers_silme = self.findChild(QtWidgets.QAction, "actionDers_Silme")
        if actionDers_silme:
            actionDers_silme.triggered.connect(self.ders_silme)
        # Ders duzenleme  
        actionDers_duzenleme = self.findChild(QtWidgets.QAction, "actionDers_Duzenleme")
        if actionDers_duzenleme:
            actionDers_duzenleme.triggered.connect(self.ders_duzenleme)
        # sinifin dersleri gosterme
        actionSinifin_dersleri = self.findChild(QtWidgets.QAction, "actionSinifin_dersleri")
        if actionSinifin_dersleri:
            actionSinifin_dersleri.triggered.connect(self.Sinifin_dersleri)

        #  ogretmen verdigi dersler
        action_ogretmen_verdigi_dersler = self.findChild(QtWidgets.QAction, "action_ogretmen_verdigi_dersler")
        if action_ogretmen_verdigi_dersler:
            action_ogretmen_verdigi_dersler.triggered.connect(self.ogretmen_verdigi_dersler)

        #  ders bilgilerini arama 
        actionDers_bilgilerini_arama = self.findChild(QtWidgets.QAction, "actionDers_bilgilerini_arama")
        if actionDers_bilgilerini_arama:
            actionDers_bilgilerini_arama.triggered.connect(self.Ders_bilgilerini_arama)

            # ogrenciler
        action_ogrenciler = self.findChild(QtWidgets.QAction, "action_ogrenciler")
        if action_ogrenciler:
            action_ogrenciler.triggered.connect(self.ogrenciler)
               # Ogretmenler
        action_ogretmenler = self.findChild(QtWidgets.QAction, "action_ogretmenler")
        if action_ogretmenler:
            action_ogretmenler.triggered.connect(self.ogretmenler)
                    # sinifler
        actionSiniflar = self.findChild(QtWidgets.QAction, "actionSiniflar")
        if actionSiniflar:
            actionSiniflar.triggered.connect(self.siniflar)








    def ogrenci_islemleri(self):
        self.ogrenci_islemleri_sayfasi = ogrenci_islemleri2.myApp()
        self.ogrenci_islemleri_sayfasi.show()
    def ogrenci_sorgulama(self):
        self.ogrenci_sorgulama_sayfasi = getStudent2.myApp()
        self.ogrenci_sorgulama_sayfasi.show()
    def sinif_ogrencilerin_sorgulamasi(self):
        self.sinif_ogrencilerin_sorgulamasi_sayfasi = getStudentsByClassName2.myApp()
        self.sinif_ogrencilerin_sorgulamasi_sayfasi.show()
    def egitmen_islemleri(self):
        self.egitmen_islemleri_sayfasi= egitmen_islemleri2.myApp()
        self.egitmen_islemleri_sayfasi.show()
    def sinif_islemleri(self):
        self.egitmen_islemleri_sayfasi= sinif_islemleri2.myApp()
        self.egitmen_islemleri_sayfasi.show()

    def ders_ekleme(self):
        self.ders_ekleme_sayfasi= ders_ekleme2.myApp()
        self.ders_ekleme_sayfasi.show()

    def ders_silme(self):
        ders_adi, ok_pressed = QInputDialog.getText(self, 'Ders silme', 'Silmek istediğiniz dersin adi giriniz:')

        if ok_pressed:
            if ders_adi.strip():  # تحقق من وجود نص بعد إزالة الفراغات
                db = DbManager()
                lesson = Lesson(None, ders_adi)
                result = db.chek_lesson_is_in_db(lesson)
                
                if not result:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText(f'<font color="red"> Bu ders veritabanında bulunmadi : {lesson.lesson_name}.</font>')
                    msg.setWindowTitle('Hata')
                    msg.exec_()
                else:
                    db.deletLesson(ders_adi)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Lütfen silmek istediğiniz ders adi giriniz")
                msg.setWindowTitle("Uyarı")
                msg.exec_()

    def ders_duzenleme(self):
        self.ders_duzenleme_sayfasi=  ders_degistirme2.myApp()
        self.ders_duzenleme_sayfasi.show()
    def actionSinifin_sorumlusu_degistir(self):
          self.edit_class_sayfasi = sinif_sorumlusu_degistirme2.myApp()
          self.edit_class_sayfasi.show()
    def Dersi_veren_ogretmeni_degistirme(self):
         self.Dersi_veren_ogretmeni_degistirme_Sayfasi = verenDersOgretmentDegistirme2.myApp()
         self.Dersi_veren_ogretmeni_degistirme_Sayfasi.show()
    def Sinifin_dersleri(self):
         self.sinif_dersleri_Sayfasi = sinif_dersleri2.myApp()
         self.sinif_dersleri_Sayfasi.show()

    def ogretmen_verdigi_dersler(self):
        self.egitmen_dersleri_sayfasi = egitmen_dersleri2.myApp()
        self.egitmen_dersleri_sayfasi.show()
    def Ders_bilgilerini_arama(self):
        self.ders_bilgilerini_arama_sayfasi = ders_bilgilerini_arama2.myApp()
        self.ders_bilgilerini_arama_sayfasi.show()

    def Ogrenci_notlarini_girme(self):
        self.ogrenci_puanlari_sayfasi = ogrenci_puanlari2.MyMainWindow()
        self.ogrenci_puanlari_sayfasi.show()

    def ogrenci_notlarini_degistirme(self):
        self.ogrenci_puanlari_edit_sayfasi = ogrenci_puanlari_edit2.MyMainWindow()
        self.ogrenci_puanlari_edit_sayfasi.show()

    def ogrenciler(self):
        self.ogrecilersayfasi = ogrenciler2.myApp()
        self.ogrecilersayfasi.show()

    def ogretmenler(self):
        self.ogretmenler_sayfasi = ogretmenler2.myApp()
        self.ogretmenler_sayfasi.show()
        
    def siniflar(self):
        self.siniflar_sayfasi = sinifler2.myApp()
        self.siniflar_sayfasi.show()
         
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())