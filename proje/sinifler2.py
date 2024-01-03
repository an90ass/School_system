# getStudent2.py
from PyQt5 import QtWidgets
from sinifler import Ui_Sinifler
import dbmanager   # استيراد DbManager بدلاً من getStudentByName
from PyQt5.QtWidgets import QMessageBox  # استيراد QMessageBox
from PyQt5.QtCore import QTimer

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_Sinifler()
        self.ui.setupUi(self)
        self.ui.table_getStudentByName.setColumnWidth(0,250)
        self.ui.table_getStudentByName.setColumnWidth(1,250)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.get_class)
        self.timer.start(5000) 
        
        self.get_class()

        
    def get_class(self):
        
       
        db = dbmanager.DbManager()
        classes = db.GetClass()

        if classes is not None:
            self.ui.table_getStudentByName.setRowCount(len(classes))
            
            for row, class_instance in enumerate(classes):
                class_name = class_instance.class_name
                teacher_id = class_instance.teacher_id
                teacher_names = db.getTeacherNameByIdFromTeacher(teacher_id)
                                    

                
                self.load_Student(row, class_name, teacher_names)


    def load_Student(self, row, class_name, teacher_names):
            column_names = [str(class_name), teacher_names, ]
            
            for col, value in enumerate(column_names):
                item = QtWidgets.QTableWidgetItem(value)
                self.ui.table_getStudentByName.setItem(row, col, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())
