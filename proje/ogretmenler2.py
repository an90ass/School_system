# getStudent2.py
from PyQt5 import QtWidgets
from ogretmenler import Ui_ogretmenler
import dbmanager   # استيراد DbManager بدلاً من getStudentByName
from PyQt5.QtWidgets import QMessageBox  # استيراد QMessageBox
from PyQt5.QtCore import QTimer

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_ogretmenler()
        self.ui.setupUi(self)
        self.ui.table_getStudentByName.setColumnWidth(0,250)
        self.ui.table_getStudentByName.setColumnWidth(3,350)
        self.ui.table_getStudentByName.setRowHeight(0,50)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_student)
        self.timer.start(5000) 
        
        self.get_student()
        
    def get_student(self):
        
       
        db = dbmanager.DbManager()
        teachers = db.GetTeachers()

        if teachers is not None:
            self.ui.table_getStudentByName.setRowCount(len(teachers))
            
            for row, teacher_data in enumerate(teachers):
                teacher = teacher_data[0]
                class_name = db.Make_sure_that_the_teacher_is_responsible_for_another_class(teacher.id)
                if class_name:
                    class_name = class_name[0][0]
                else:
                    class_name = "Yok"
                                

                
                self.load_Student(row, teacher.teacher_number, teacher.teacher_name,
                                teacher.teacher_surname, teacher.teacher_birthday,
                                teacher.teacher_gender,class_name)

    def load_Student(self, row, student_number, student_name, student_surname,
                        student_birthday, student_gender,class_name):
            column_names = [str(student_number), student_name, student_surname,
                            str(student_birthday), student_gender,class_name]
            
            for col, value in enumerate(column_names):
                item = QtWidgets.QTableWidgetItem(value)
                self.ui.table_getStudentByName.setItem(row, col, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())
