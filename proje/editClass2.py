from PyQt5 import QtWidgets,QtCore
from editClass import Ui_edit_class
from  dbmanager import DbManager  
from PyQt5.QtWidgets import QMessageBox,QInputDialog

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_edit_class()
        self.ui.setupUi(self)
        db = DbManager()
       
              
        
        class_names = db.fill_comobox_withClass_names()
        for i in class_names:
            self.ui.class_combo.addItems(i)

        self.ui.class_combo.setCurrentIndex(-1)

        self.ui.pushButton.clicked.connect(self.edit_information)

 
    def edit_information(self):
                class_name = self.ui.class_combo.currentText()
                new_class_name = self.ui.new_class_name.toPlainText()

                if not class_name  or not new_class_name:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Lutfen bilgileri giriniz .")
                    msg.setWindowTitle("Hata")
                    msg.exec()
                else:
                    db = DbManager()
                    
                    db.editClass(class_name,new_class_name)
                            # Optionally, you can show a message to confirm the edit
                    
                    self.ui.class_combo.clear()
                    self.ui.new_class_name.clear()
   



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())       