from tkinter import dialog
from ders_degistirme import Ui_DersDegistirme
from PyQt5 import QtWidgets,QtCore
from dbmanager import DbManager
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog
from Lesson import Lesson

from PyQt5.QtWidgets import QMessageBox
class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_DersDegistirme()
        self.ui.setupUi(self)
        self.ui.arama_btn.clicked.connect(self.ders_degistieme_islemi)
    


    def ders_degistieme_islemi(self):
                ders_adi = self.ui.ders_adi.toPlainText().strip()

                if not ders_adi or ders_adi.isspace():
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Lutfen ders adi gininiz.")
                    msg.setWindowTitle("Hata")
                    msg.exec()
                else:
                    db = DbManager()
                    lesson = Lesson(
                        None,  #  
                        ders_adi
                    )
                    result = db.chek_lesson_is_in_db(lesson)
                    if not result:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText(f'<font color="red" size="5"> "{ders_adi}" bu ders veritabanında bulunamadı .</font>')
                        msg.setWindowTitle('Hata')
                        msg.exec_()
                        self.ui.ders_adi.clear()
                        
                    else:
                        ders_adi, ok_pressed = QInputDialog.getText(self, 'Ders adi degistirme', 'Yeni ders adi giriniz:')

                        if ok_pressed and ders_adi:
                            if not ders_adi or ders_adi.isspace():
                                msg = QMessageBox()
                                msg.setIcon(QMessageBox.Warning)
                                msg.setText("Lutfen gecerli bir ders adi giriniz.")
                                msg.setWindowTitle("Hata")
                                msg.exec()
                            else:
                                db.editLesson(lesson, ders_adi.strip())
                                self.ui.ders_adi.clear()
                        else:
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Warning)
                            msg.setText("Lütfen gecerli bir ders adi giriniz.")
                            msg.setWindowTitle("Hata")
                            msg.exec()
                            

                        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())