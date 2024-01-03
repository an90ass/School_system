from verenDersOgretmentDegistirme import Ui_veren_ders_degistirme
from PyQt5 import QtWidgets,QtCore
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
        self.ui = Ui_veren_ders_degistirme()
        self.ui.setupUi(self)
        self.db = DbManager()
        self.lesson_id = None
        self.teacher_id = None
        self.new_teacher_id=None
        self.lesson_name = None
         
        self.disable_editable_elements()
        
        # fill comobox with class names from class table dahasonra secilen classin id sini alacagim
        class_names =self. db.fill_comobox_withClass_names()
        for i in class_names:
            self.ui.class_names.addItems(i)
        self.ui.class_names.setCurrentIndex(-1)
        
        # fill comobox with teacher names from teacher table dahasonra secilen teachein id sini alacagim
        class_names = self.db.fill_comoboxTeachersNames()
        for i in class_names:
            self.ui.teacher_names.addItems(i)             
        self.ui.teacher_names.setCurrentIndex(-1)

      


        self.ui.class_names.currentIndexChanged.connect(self.on_class_names_selected)# bir class secilirse
        self.disable_editable_elements()        
        self.ui.lesson_names.activated.connect(self.on_lesson_names_selected)# bir lesson secilirse
        self.ui.teacher_names.activated.connect(self.on_teacher_names_selected)  # bir teacher secilirse
        

        self.ui.degitir_btn.clicked.connect(self.degistirme_islemi)


        

    def on_class_names_selected(self):
        self.able_editable_elements()
        class_name = self.ui.class_names.currentText()
       
        class_id = self.db.getClassId(class_name) # class id getir
        information = self.db.getAllLessonInfoForTheClass(class_id)
        # print(information)
        lesson_ides2 = [row[0] for row in information] # sadece lessonId al
        lesson_names_list = []
        for i in range(1, len(lesson_ides2) + 1):
                id = lesson_ides2[i - 1]            
                secilen_class_ait_dersler = self.db.getLessonNamesByIdFromLesson(id)
                lesson_names_list.append(secilen_class_ait_dersler)               
        self.ui.lesson_names.clear()

        for name in lesson_names_list:
                self.ui.lesson_names.addItem(name)
        self.ui.lesson_names.setCurrentIndex(-1)

    def on_lesson_names_selected(self):
        self.lesson_name = self.ui.lesson_names.currentText()
        
        self.lesson_id = self.db.getLessonId(self.lesson_name)
        self.teacher_id = self.db.getTeacherIdFromclasslessonSecilen_ders_icin_hangi_ogretmen_verdigini_bilmek_icin(self.lesson_id)
        teacher_name =self. db.getTeacherNameByIdFromTeacher(self.teacher_id)
        message = f"<b><font size='5'> Bu ders'i <font color='green' size='10'>{teacher_name} </font>hoca veriyor</font></b>"    
        QMessageBox().information(self, "Bilgilendirme", message)
        # QMessageBox().information(self, "Bilgilendirme", "<b> <font color='red' size='5'> Değiştirmek istediğiniz öğretmeni seçmeyi unutmayın</font></b>")
       

    def on_teacher_names_selected(self):
         teacher_name =  self.ui.teacher_names.currentText()
         self.new_teacher_id = self.db.getTeacherId_toSaveIt_inClassTable_OR_ClassLessonTable(teacher_name)
         
       
         

    def degistirme_islemi(self):
            self.db.dersi_veren_teacher_degistirme(self.lesson_id,self.new_teacher_id)
            QMessageBox().information(self, "Basarili islem", f"{self.lesson_name} dersi veren öğretmen değiştirilidi")
            self.ui.teacher_names.setCurrentIndex(-1)
            self.ui.lesson_names.setCurrentIndex(-1)
            self.ui.lesson_names.clear()
            self.disable_editable_elements()





    



    def disable_editable_elements(self):
        self.ui.class_names.setEnabled(True)
        self.ui.teacher_names.setEnabled(False)
        self.ui.lesson_names.setEnabled(False)
    def able_editable_elements(self):
        self.ui.class_names.setEnabled(True)
        self.ui.teacher_names.setEnabled(True)
        self.ui.lesson_names.setEnabled(True)
    




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())
