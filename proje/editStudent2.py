from editStudent import Ui_StudenteditNumber
from PyQt5 import QtWidgets,QtCore
from dbmanager import DbManager
from Student import Student
from PyQt5.QtWidgets import QMessageBox

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_StudenteditNumber()
        self.ui.setupUi(self)
        self.ui.comboBox       
        db = DbManager() 
        # self.ui.comboBox.setCurrentIndex(-1)
        class_names = db.fill_comobox_withClass_names()
        for i in class_names:
            self.ui.comboBox.addItems(i)
        self.ui.comboBox.setCurrentIndex(0)
        self.disable_editable_elements()
        self.ui.bilgileri_goster_btn.clicked.connect(self.show_information_for_edit)
    def show_information_for_edit(self):
        # الحصول على الرقم المدخل من واجهة المستخدم
        name_or_number = self.ui.student_number_text.toPlainText()
        if not name_or_number: 
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen öğrenci numarası veya adı girin")
            msg.setWindowTitle("Uyarı")
            msg.setStyleSheet("color: red;")  # لتحديد لون النص
            msg.exec_()
        else:
            self.ui.mesaje.setText("")
            db = DbManager()
            student = db.getStudentByName(name_or_number)
            if student is not None:
                self.load_Student(student[0].student_number,student[0].student_name,student[0].student_surname,student[0].student_birthday,student[0].student_gender)
                info_text = f"Student Name: {student[0].student_name}\n"           
                # print(info_text)     
                # self.close()  
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Ögrenci bilgileri basarıyla getrilidi")
                msg.setWindowTitle("Uyarı")
                msg.setStyleSheet("color: green;")  # لتحديد لون النص
                msg.exec_()
                    
              # self.ui.mesaje.setText("")
                #self.ui.mesaje.setStyleSheet("color: green;")
                self.ui.edit_btn.clicked.connect(self.edit_information)
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Öğrenci veritabanında bulunmadı. Lütfen başka bir numara girin")
                msg.setWindowTitle("Uyarı")
                msg.setStyleSheet("color: red;")  # لتحديد لون النص
                msg.exec_()
                 
             
    def load_Student(self,student_number,student_name,student_surname,student_birthday,student_gender):

            self.ui.student_number_text.setPlainText(str(student_number))
            self.ui.student_name_text.setPlainText(student_name)
            self.ui.student_surname_text.setPlainText(student_surname)
            # formatted_birthday = student_birthday.strftime("yyyy-MM-dd hh:mm:ss")
            formatted_birthday = self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime(student_birthday))


            self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.fromString(formatted_birthday, "yyyy-MM-dd hh:mm:ss"))
             
            if student_gender == "E":
                self.ui.erkek.setChecked(True)
            else:
                self.ui.kadin.setChecked(True)
            self.able_editable_elements()
    def edit_information(self):
            student_number = self.ui.student_number_text.toPlainText()
            student_name = self.ui.student_name_text.toPlainText()
            student_surname = self.ui.student_surname_text.toPlainText()
            birth_date = self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
            gender = "E" if self.ui.erkek.isChecked() else "K"
            selected_class = self.ui.comboBox.currentText()
            # التحقق من أن المدخلات ليست فارغة
            if not student_number or not student_name or not student_surname or not birth_date or not gender:
                # self.ui.mesaje.setText("")
                # self.ui.mesaje.setStyleSheet("color: red;")
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText("Lütfen tüm bilgilere girin")
                msg.setWindowTitle("Uyarı")
                msg.setStyleSheet("color: red;")  # لتحديد لون النص
                msg.exec_()
                
            else:
                db = DbManager()
                student = Student(
                    None,  # اترك الـ id فارغًا لأنه سيتم توليده تلقائياً بواسطة قاعدة البيانات
                    student_number,
                    student_name,
                    student_surname,
                    birth_date,
                    gender,
                    selected_class
                )
                db.editStudent(student)
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Ögrenci basarıyla guncellendi")
                msg.setWindowTitle("Uyarı")
                msg.setStyleSheet("color: green;")   
                msg.exec_()
                
               # self.ui.mesaje.setText("")
               # self.ui.mesaje.setStyleSheet("color: green;")
                self.ui.student_number_text.clear()
                self.ui.student_name_text.clear()
                self.ui.student_surname_text.clear()
                self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
                self.ui.erkek.setChecked(False)
                self.ui.kadin.setChecked(False)
                self.disable_editable_elements()


    def disable_editable_elements(self):
        self.ui.edit_btn.hide()
        self.ui.bilgileri_goster_btn.show()

        self.ui.student_name_text.setDisabled(True)
        self.ui.student_surname_text.setDisabled(True)
        self.ui.dateTimeEdit.setDisabled(True)
        self.ui.erkek.setDisabled(True)
        self.ui.kadin.setDisabled(True)
        self.ui.comboBox.setDisabled(True)

    def able_editable_elements(self):
        self.ui.edit_btn.show()
        self.ui.bilgileri_goster_btn.hide()
        self.ui.student_name_text.setDisabled(False)
        self.ui.student_surname_text.setDisabled(False)
        self.ui.dateTimeEdit.setDisabled(False)
        self.ui.erkek.setDisabled(False)
        self.ui.kadin.setDisabled(False)
        self.ui.comboBox.setDisabled(False) 
    



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())
