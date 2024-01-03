from PyQt5 import QtWidgets
from ders_bilgilerini_arama import Ui_ders_egitmen_arama
from Student import Student
import dbmanager
import ogrenci_islemleri2
import addTeacher2 
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import editTeacher2
from itertools import zip_longest



import addTeacher2
class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_ders_egitmen_arama()
        self.ui.setupUi(self)
        self.ui.ders_arama_table.setColumnWidth(0,230)
        self.ui.ders_arama_table.setColumnWidth(1,250)
        self.ui.ders_arama_table.setColumnWidth(2,500)

        self.db = dbmanager.DbManager()

        lesson_names =self. db.fill_comoboxLessonNames()
        for i in lesson_names:
            self.ui.lesson_names_combo.addItems(i)
        self.ui.lesson_names_combo.setCurrentIndex(-1)
        self.ui.lesson_names_combo.currentIndexChanged.connect(self.on_lesson_names_combo_selected)# bir ders secilirse
    def on_lesson_names_combo_selected(self):
        db = dbmanager.DbManager()
        lesson_name = self.ui.lesson_names_combo.currentText()
        lesson_id = db.getLessonId(lesson_name)
        T_id = db.getTeacherIdFromclasslessonSecilen_ders_icin_hangi_ogretmen_verdigini_bilmek_icin(lesson_id)
        teacher_name = db.getTeacherNameByIdFromTeacher(T_id)
        # bu derse ogretmen hangi sinifin sormlusu
        sorumlu_oldugu_sinif_adi = db.Make_sure_that_the_teacher_is_responsible_for_another_class(T_id)
        if sorumlu_oldugu_sinif_adi:
            sorumlu_oldugu_sinif_adi = sorumlu_oldugu_sinif_adi[0][0]
        else:
            sorumlu_oldugu_sinif_adi = "Yok"
        # secilen ders hangi classa ait
        class_id = db.getClassIdFromclassLessonByLessonId(lesson_id)
        bu_dersin_classi = db.getClassName(class_id)

        columon_names = [bu_dersin_classi,teacher_name,sorumlu_oldugu_sinif_adi]
        for col,value in enumerate(columon_names):
              item = QtWidgets.QTableWidgetItem(value)
              self.ui.ders_arama_table.setItem(0, col, item)





if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())     