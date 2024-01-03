from tkinter import messagebox
from ders_ekleme import Ui_DersEkleme
from PyQt5 import QtWidgets,QtCore
import dbmanager
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog
from classlesson import ClassLesson
from PyQt5.QtWidgets import QMessageBox
from Lesson import Lesson  # Assuming Lesson is a class defined in Lesson.py
from sinif_sorumlusu_degistirme import Ui_edit_class
from Class import Class
from  dbmanager import DbManager  
import ogrenci_islemleri2 
class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_DersEkleme()
        self.ui.setupUi(self)
        db = DbManager()
        # fill comobox with teacher names from teacher table dahasonra secilen teachein id sini alacagim
        teacherNames = db.fill_comoboxTeachersNames()
        for i in teacherNames:
            self.ui.teacher_names.addItems(i)             
        self.ui.teacher_names.setCurrentIndex(-1)

      # fill comobox with class names from class table dahasonra secilen classin id sini alacagim
        class_names = db.fill_comobox_withClass_names()
        for i in class_names:
            self.ui.class_names.addItems(i)
        self.ui.class_names.setCurrentIndex(-1)

        self.ui.ekleme_btn.clicked.connect(self.add_ders)

    def add_ders(self):
        ders_adi = self.ui.ders_adi.toPlainText()
        class_name = self.ui.class_names.currentText()
        teacher_name = self.ui.teacher_names.currentText()

        if not ders_adi  or not class_name or not teacher_name:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen ders adi ve diger bilgileri giriniz")
            msg.setWindowTitle("Uyarı")
            msg.exec_()
        else:
            db = dbmanager.DbManager()
            teacher_id = db.getTeacherId_toSaveIt_inClassTable_OR_ClassLessonTable(teacher_name)# teacher id getir
            class_id = db.getClassId(class_name) # class id getir
            lesson = Lesson(None, ders_adi)
            db.addLesson(lesson) # once ders ekle
            lesson_id = db.getLessonId(ders_adi) # daha sonra id si al
            classlesson = ClassLesson(
                 None,
                 class_id,
                 teacher_id,
                 lesson_id
            )
            db.addClassLesson(classlesson)
            # msg = QMessageBox()
            # msg.setIcon(QMessageBox.Information)
            # msg.setText(f'<font color="green"> Ders başarıyla veritabanına eklendi.</font>')
            # msg.setWindowTitle('Ekleme işlemi başarılı')
            # msg.exec_()
            
            

            
            
                
            # self.ui.ders_adi.clear()
    def delete_ders(self):
        ders_adi, ok_pressed = QInputDialog.getText(self, 'Öğrenci silme', 'Silmek istediğiniz öğrenci numarasını giriniz:')              
        if ok_pressed and ders_adi:
                    db = dbmanager.DbManager()
                    db.deletLesson(ders_adi)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())
