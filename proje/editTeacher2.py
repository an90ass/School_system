from PyQt5 import QtWidgets,QtCore
import time
from editTeacher import Ui_EditTeacher
from Teacher import Teacher
from dbmanager import DbManager 
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QCheckBox

import egitmen_islemleri2 # استيراد DbManager بدلاً من getStudentByName

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_EditTeacher()
        self.ui.setupUi(self)
        self.disable_editable_elements()
        self.teacher_id = None
        self.ui.bilgileri_goster_btn.clicked.connect(self.edit)


    def edit(self):
            teacherNumber = self.ui.teacher_number.toPlainText()
            if not teacherNumber: 
                # self.add_page.ui.mesaje.setText("Lütfen öğrenci numarasıveya adı girin")
                # self.add_page.ui.mesaje.setStyleSheet("color: red;")
              
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("Lütfen egitmen numarasi giriniz")
                msg.setWindowTitle("Uyarı")
                msg.exec_()
            else:
                # self.add_page.ui.mesaje.setText("")
                db = DbManager()
                teacher = db.getTeacherByNumber(teacherNumber)##getTeacherByName di
                if teacher is not None:                          #branch.
                    self.load_Teacher(teacher[0].teacher_number,teacher[0].teacher_name,teacher[0].teacher_surname,teacher[0].teacher_birthday,teacher[0].teacher_gender)
                    self.teacher_id=teacher[0].id
                    
##################################################             buraya kadara tmm        ##################################################### buraya kadar tmm
                    self.ui.kaydet_for_edit_btn.clicked.connect(self.edit_information)
    def load_Teacher(self,teacherNumber,teacher_name,teacher_surname,teacher_birthdate,teacher_gender):
            self.ui.teacher_number.setPlainText(str(teacherNumber))
            self.ui.teacher_name.setPlainText(str(teacher_name))
            self.ui.teacher_surname.setPlainText(teacher_surname)
            # self.ui.branch.setPlainText(branch)
            # formatted_birthday = student_birthday.strftime("yyyy-MM-dd hh:mm:ss")
            formatted_birthday = self.ui.teacher_birthdate.setDateTime(QtCore.QDateTime(teacher_birthdate))


            self.ui.teacher_birthdate.setDateTime(QtCore.QDateTime.fromString(formatted_birthday, "yyyy-MM-dd hh:mm:ss"))
             
            if teacher_gender == "E":
                self.ui.erkek.setChecked(True)
            else:
                self.ui.kadin.setChecked(True)
            self.able_editable_elements()
   

    def edit_information(self):
            self.teacher_id
            teacher_number = self.ui.teacher_number.toPlainText()
            teacher_name = self.ui.teacher_name.toPlainText()
            teacher_surname = self.ui.teacher_surname.toPlainText()
            # branch = self.ui.branch.toPlainText()
            teacher_birthdate = self.ui.teacher_birthdate.dateTime().toString("yyyy-MM-dd hh:mm:ss")
            teacher_gender = "E" if self.ui.erkek.isChecked() else "K"
            # 
            if not teacher_name or not teacher_surname  or not teacher_birthdate or not teacher_gender:
                # self.ui.mesaje.setText("Lütfen tüm bilgilere girin")
                # self.ui.mesaje.setStyleSheet("color: red;")
                print("Lütfen tüm bilgilere girin")
            else:
                db =DbManager()
                teacher = Teacher(
                    self.teacher_id,  
                    teacher_number,
                    # branch,
                    teacher_name,
                    teacher_surname,
                    teacher_birthdate,
                    teacher_gender
                )
                # إضافة البيانات إلى قاعدة البيانات باستخدام الكائن DbManager
                db.editTeacher(teacher)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Egitmen basarıyla guncelledi")
                msg.setWindowTitle("Uyarı")
                msg.exec_()
                # print("Egitmen basariyla guncelledi")
                # مسح المدخلات من واجهة المستخدم بعد الإضافة
                self.ui.teacher_number.clear()
                self.ui.teacher_name.clear()
                self.ui.teacher_surname.clear()
                # self.ui.branch.clear()
                self.ui.teacher_birthdate.setDateTime(QtCore.QDateTime.currentDateTime())
                self.ui.erkek.setChecked(False)
                self.ui.kadin.setChecked(False)
                self.disable_editable_elements()
    def disable_editable_elements(self):   
            self.ui.teacher_number.setDisabled(False)
            self.ui.teacher_name.setDisabled(True)
            self.ui.teacher_surname.setDisabled(True)
            self.ui.teacher_birthdate.setDisabled(True)
            self.ui.erkek.setDisabled(True)
            self.ui.kadin.setDisabled(True)
            # self.ui.branch.setDisabled(True)
            self.ui.bilgileri_goster_btn.setDisabled(False)  
            self.ui.kaydet_for_edit_btn.setDisabled(True)

    def able_editable_elements(self):   
            self.ui.teacher_number.setDisabled(False)    
            self.ui.teacher_name.setDisabled(False)
            self.ui.teacher_surname.setDisabled(False)
            self.ui.teacher_birthdate.setDisabled(False)
            self.ui.erkek.setDisabled(False)
            self.ui.kadin.setDisabled(False)
            # self.ui.branch.setDisabled(False)
            self.ui.bilgileri_goster_btn.setDisabled(True) 
            self.ui.kaydet_for_edit_btn.setDisabled(False)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())   