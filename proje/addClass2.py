from PyQt5 import QtWidgets,QtCore
import time
from addClass import Ui_addClass
from Class import Class
import dbmanager  
from dbmanager import DbManager
from PyQt5.QtWidgets import QMessageBox
import  ogrenci_islemleri2 # استيراد DbManager بدلاً من getStudentByName

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_addClass()
        self.ui.setupUi(self)
        db = DbManager()
        class_names = db.fill_comoboxTeachersNames()
        for i in class_names:
            self.ui.teachers_name_combo.addItems(i)

        self.ui.teachers_name_combo.setCurrentIndex(-1)

        self.ui.pushButton.clicked.connect(self.addClass)
    

    def addClass(self):
        class_name = self.ui.name_class.toPlainText()
        teacher_name = self.ui.teachers_name_combo.currentText()
        if teacher_name:
            db = DbManager()
            teacher_id = db.getTeacherId_toSaveIt_inClassTable_OR_ClassLessonTable(teacher_name)
            teacher_already_exists = db.Make_sure_that_the_teacher_is_responsible_for_another_class(teacher_id)

            if teacher_already_exists:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f"{teacher_name}  hoca baska bir sınıfın sorumlusu lütfen baska bir hoca seciz ")
                msg.setWindowTitle("Hata")
                msg.exec_()
                # مسح المعلومات المدخلة
                self.ui.name_class.clear()
                self.ui.teachers_name_combo.setCurrentIndex(-1)
            else:
                if not class_name or not teacher_id:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Lütfen tüm bilgilere girin")
                    msg.setWindowTitle("Uyarı")
                    msg.exec_()
                else:
                    _class = Class(
                        None,#    
                        class_name,
                        teacher_id,
                    )
                    db.addClass(_class)
                    self.ui.name_class.clear()
                    self.ui.teachers_name_combo.setCurrentIndex(-1)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen eğitmen ismini seç")
            msg.setWindowTitle("Uyarı")
            msg.exec_()
            



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())