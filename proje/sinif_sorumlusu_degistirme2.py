from PyQt5 import QtWidgets,QtCore
from sinif_sorumlusu_degistirme import Ui_edit_class
from Class import Class
from  dbmanager import DbManager  
import ogrenci_islemleri2 
import addTeacher2 # استيراد DbManager بدلاً من getStudentByName
from PyQt5.QtWidgets import QMessageBox,QInputDialog

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_edit_class()
        self.ui.setupUi(self)
        db = DbManager()
        class_names = db.fill_comoboxTeachersNames()
        for i in class_names:
            self.ui.teachers_name_combo.addItems(i)
              
        self.ui.teachers_name_combo.setCurrentIndex(-1)
        
        class_names = db.fill_comobox_withClass_names()
        for i in class_names:
            self.ui.class_combo.addItems(i)

        self.ui.class_combo.setCurrentIndex(-1)
        self.ui.label_3.setText("")

        self.disable_editable_elements()
        self.ui.bilgileri_goster_2.clicked.connect(self.bilgileri_goster_2)
        self.ui.pushButton.clicked.connect(self.edit_information)

        
    def bilgileri_goster_2(self):
            class_name = self.ui.class_combo.currentText()
            teacher_name = self.ui.teachers_name_combo.currentText()
            if not class_name: 
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("lütfen sınıfın adı giriniz")
                    msg.setWindowTitle("Başarılı")
                    msg.exec()
            else:
                db = DbManager()
                teacher_id = db.getTeacherIdFromClass(class_name)# sininf sorumlusus hocanin id si class tablosundan detir
                teacher_name = db.getTeacherNameByIdFromTeacher(teacher_id) # daha sonra bu id ile (teacher id) teacher name teacher tablosundan getir
                self.ui.label_3.setText("Bu sınıfın sorumlusu öğretmen "+teacher_name+"\n"+"Değiştirmek istediğiniz hocanın ismi seçiniz")
                self.able_editable_elements()
                new_teachername = self.ui.teachers_name_combo.currentText()
                # new_teacher_id = db.getTeacherId_toSaveIt_inClassTable_whenYouAddNewClass(new_teachername)
                
    def edit_information(self):
                class_name = self.ui.class_combo.currentText()
                new_teachername = self.ui.teachers_name_combo.currentText()

                if not class_name or not new_teachername:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Lutfen Hoca ismi seciniz.")
                    msg.setWindowTitle("Hata")
                    msg.exec()
                else:
                    db = DbManager()
                    new_teacher_id = db.getTeacherId_toSaveIt_inClassTable_OR_ClassLessonTable(new_teachername)
                    
                    if new_teacher_id is not None:
                        # Check if the new teacher is already responsible for another class
                        responsible_classes = db.Make_sure_that_the_teacher_is_responsible_for_another_class(new_teacher_id)
                        responsible_classes = [responsible_class[0] for responsible_class in responsible_classes]
                        
                        if not responsible_classes:
                            _class = Class(
                                None,
                                class_name,
                                new_teacher_id
                            )
                            db.editClass_sorumlusu(_class)
                            # Optionally, you can show a message to confirm the edit
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText("Sınıfın sorumlusu başarıyla güncellendi.")
                            msg.setWindowTitle("Başarılı")
                            msg.exec()
                            self.ui.class_combo.clear()
                            self.ui.teachers_name_combo.clear()
                            self.ui.label_3.setText("")
                            self.disable_editable_elements()
                            self.fill_combo()
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText(f"Bu öğretmen zaten {', '.join(responsible_classes)} sınıfının sorumlusu. Lütfen başka bir öğretmen seçin.")
                            msg.setWindowTitle("Hata")
                            msg.exec()
                                
    def fill_combo(self):
                    db = DbManager()
                    teachers_names = db.fill_comoboxTeachersNames()
                    for i in teachers_names:
                            self.ui.teachers_name_combo.addItems(i)
                            
                    self.ui.teachers_name_combo.setCurrentIndex(-1)

                    class_names = db.fill_comobox_withClass_names()
                    for i in class_names:
                        self.ui.class_combo.addItems(i)

                    self.ui.class_combo.setCurrentIndex(-1)
         
            

    def disable_editable_elements(self) :
         self.ui.class_combo.setDisabled(False)
         self.ui.teachers_name_combo.setDisabled(True)
    def able_editable_elements(self) :
         self.ui.class_combo.setDisabled(True)
         self.ui.teachers_name_combo.setDisabled(False)
                           
             
         

    






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())       