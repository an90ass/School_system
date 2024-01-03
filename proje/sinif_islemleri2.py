from sinif_islemleri import Ui_sinif_islemleri
from PyQt5 import QtWidgets,QtCore
import dbmanager 
from addClass2 import myApp as AddClassMyapp
from editClass2 import myApp as editClassMyapp
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog,QMessageBox
class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_sinif_islemleri()
        self.ui.setupUi(self)
        self.ui.ekleme_btn_2.clicked.connect(self.add_action)
        self.ui.degistirme_btn.clicked.connect(self.edit_action)
        self.ui.silme_btn.clicked.connect(self.silme_action)


    def add_action(self):
        self.islem = 1
        self.add_page = AddClassMyapp()
        self.add_page.show()

    def edit_action(self):
        self.islem = 2
        self.edit_page = editClassMyapp()      
        self.edit_page.show()
  
    def silme_action(self):
        class_name, ok_pressed = QInputDialog.getText(self, 'Sinif silme', 'Silmek istediğiniz sinif ismi giriniz:')

        if ok_pressed and class_name:
            # Ask for user confirmation before deleting the class and associated students
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f"Sınıfı ve bu sınıfa bağlı tüm öğrencileri silmek istediğinizden emin misiniz?\nBu işlem geri alınamaz!")
            msg.setWindowTitle("Dikkat")
            msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
            result = msg.exec()

            if result == QMessageBox.Ok:
                # User confirmed the deletion
                db = dbmanager.DbManager()
                db.deletClass(class_name)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())