from PyQt5 import QtWidgets,QtCore
import time
from addTeacher import Ui_AddTeacher
from Teacher import Teacher
from dbmanager import DbManager 
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QCheckBox

import egitmen_islemleri2 # استيراد DbManager بدلاً من getStudentByName

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_AddTeacher()
        self.ui.setupUi(self)   

        self.ui.add_btn.clicked.connect(self.add)
                
       
        
        
    def add(self):
            teacher_number = self.ui.teacher_number.toPlainText().upper()
            teacher_name = self.ui.teacher_name.toPlainText().upper()
            teacher_surname = self.ui.teacher_surname.toPlainText().upper()
            teacher_birthdate = self.ui.teacher_birthdate.dateTime().toString("yyyy-MM-dd hh:mm:ss")
            teacher_gender = "E" if self.ui.erkek.isChecked() else "K"
            # branch = self.ui.branch.toPlainText()
            if not teacher_name or not teacher_number or not teacher_surname or not teacher_birthdate or not teacher_gender :
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Lütfen tüm bilgilere girin")
                msg.setWindowTitle("Uyarı")
                msg.exec_()
            else:
                db = DbManager()
                teacher = Teacher(
                    None,
                    teacher_number, 
                    # branch,
                    teacher_name,
                    teacher_surname,
                    teacher_birthdate,
                    teacher_gender
                )
                db.addTeacher(teacher)
                self.ui.teacher_number.clear()
                self.ui.teacher_name.clear()
                self.ui.teacher_surname.clear()
                self.ui.erkek.setChecked(False)
                self.ui.kadin.setChecked(False)
                self.ui.teacher_birthdate.setDateTime(QtCore.QDateTime.currentDateTime())
                # self.ui.branch.clear()
                
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())       

  