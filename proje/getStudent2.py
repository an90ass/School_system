# getStudent2.py
from PyQt5 import QtWidgets
from getStudent import Ui_GetStudent
import dbmanager   # استيراد DbManager بدلاً من getStudentByName
from PyQt5.QtWidgets import QMessageBox  # استيراد QMessageBox

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_GetStudent()
        self.ui.setupUi(self)
        self.ui.table_getStudentByName.setColumnWidth(0,250)
        self.ui.table_getStudentByName.setColumnWidth(3,350)
        self.ui.table_getStudentByName.setRowHeight(0,50)
        
        self.ui.Ok.clicked.connect(self.get_student)
        
    def get_student(self):
        student_name = self.ui.student_name.toPlainText()  # الحصول على student_name من واجهة المستخدم
        if not student_name:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Lütfen arama yapmadan önce öğrencinin numarasını yada adını  giriniz.")
            msg.setWindowTitle("Uyarı")
            msg.exec_()
        else:
                db = dbmanager.DbManager()
                student = db.getStudentByName(student_name)
                if student is not None:
                    # print(db.getClassName(student[0].classid))
                    class_name = db.getClassName(student[0].classid)
                    self.load_Student(student[0].student_number,student[0].student_name,student[0].student_surname,student[0].student_birthday,student[0].student_gender,class_name)
                    info_text = f"Student Name: {student[0].student_name}\n"
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Bu öğrenci veri tabanında kayıtlı değildir")
                    msg.setWindowTitle("Dikkat")
                    msg.exec_()
                    self.ui.table_getStudentByName.clearContents()

    def load_Student(self,student_number,student_name,student_surname,student_birthday,student_gender,class_name):
        columon_names = [str(student_number),student_name,student_surname,str(student_birthday),student_gender,class_name]
        for col,value in enumerate(columon_names):
              item = QtWidgets.QTableWidgetItem(value)
              self.ui.table_getStudentByName.setItem(0, col, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())
