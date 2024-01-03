from PyQt5 import QtWidgets
from egitmen_islemleri import Ui_egitmen_islemleri
from Student import Student
import dbmanager
import ogrenci_islemleri2
import addTeacher2 
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import editTeacher2

import addTeacher2
class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_egitmen_islemleri()
        self.ui.setupUi(self)
        

        self.ui.add_teacher_btn.clicked.connect(self.add_action)
        self.ui.edit_teacher_btn.clicked.connect(self.edit_action)
        self.ui.delete_teacher_btn.clicked.connect(self.silme_action)


    def add_action(self):
        self.add_page = addTeacher2.myApp()
        self.add_page.show()

    def edit_action(self):
        self.edit_page = editTeacher2.myApp()       
        self.edit_page.show()
        
        
    def silme_action(self):
        
        teacher_number, ok_pressed = QInputDialog.getText(self, 'Eğitmen silme', 'Silmek istediğiniz egitmen numarasi giriniz:')

        if ok_pressed and teacher_number:
            db = dbmanager.DbManager()
            db.deleteTeacher(teacher_number)
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())       