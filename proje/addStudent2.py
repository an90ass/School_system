from PyQt5 import QtWidgets,QtCore
import time
from addStudent import Ui_addStudent
from Student import Student
import dbmanager  

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_addStudent()
        self.ui.setupUi(self)
        
        self.ui.comboBox
        
        db = dbmanager.DbManager() 
        class_names = db.fill_comobox_withClass_names()
        for i in class_names:
            self.ui.comboBox.addItems(i)
        self.ui.comboBox.setCurrentIndex(0)
        
        
        self.ui.add_btn.clicked.connect(self.add)
        


    def add(self):
    # الحصول على البيانات المُدخلة من واجهة المستخدم
        student_number = self.ui.student_number_text.toPlainText()
        student_name = self.ui.student_name_text.toPlainText()
        student_surname = self.ui.student_surname_text.toPlainText()
        birth_date = self.ui.dateTimeEdit.dateTime().toString("yyyy-MM-dd hh:mm:ss")
        gender = "E" if self.ui.erkek.isChecked() else "K"
        selected_class = self.ui.comboBox.currentText()
        # التحقق من أن المدخلات ليست فارغة
        if not student_number or not student_name or not student_surname or not birth_date or not gender:
            self.ui.mesaje.setText("Lütfen tüm bilgilere girin")
            self.ui.mesaje.setStyleSheet("color: red;")
        else:
            db = dbmanager.DbManager()
            student = Student(
                None,  # اترك الـ id فارغًا لأنه سيتم توليده تلقائياً بواسطة قاعدة البيانات
                student_number,
                student_name,
                student_surname,
                birth_date,
                gender,
                selected_class
            )
            db.addStudent(student)           
            self.ui.student_number_text.clear()
            self.ui.student_name_text.clear()
            self.ui.student_surname_text.clear()
            self.ui.dateTimeEdit.setDateTime(QtCore.QDateTime.currentDateTime())
            self.ui.erkek.setChecked(False)
            self.ui.kadin.setChecked(False)
            self.ui.comboBox.setCurrentIndex(0)
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())       