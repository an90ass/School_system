from ogrenci_islemleri import Ui_MainWindow
from PyQt5 import QtWidgets,QtCore
import dbmanager 
from addStudent2 import myApp as AddStudentApp
import editStudent2
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog



class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.islem = 0

        self.ui.ekleme_btn.clicked.connect(self.add_action)
        self.ui.degistirme_btn.clicked.connect(self.edit_action)
        self.ui.silme_btn.clicked.connect(self.silme_action)


    def add_action(self):
        self.islem = 1
        self.add_page = AddStudentApp()
        self.add_page.show()

    def edit_action(self):
        self.islem = 2
        self.edit_page =editStudent2.myApp()       
        self.edit_page.show()
  
    def silme_action(self):
        student_number, ok_pressed = QInputDialog.getText(self, 'Öğrenci silme', 'Silmek istediğiniz öğrenci numarasını giriniz:')

        if ok_pressed and student_number:
            # استدعاء دالة deletStudent لحذف الطالب باستخدام الرقم المدخل
            db = dbmanager.DbManager()
            db.deletStudent(student_number)

            

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())
