from sinif_dersleri import Ui_SinifDersleri
from PyQt5 import QtWidgets,QtCore
import dbmanager 
from PyQt5.QtWidgets import QMessageBox
from addStudent2 import myApp as AddStudentApp
from editStudent2 import myApp as EditStudentApp
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog,QTableWidget,QTableWidgetItem,QAbstractItemView
from  dbmanager import DbManager  
from PyQt5.QtGui import QFont
from itertools import zip_longest




class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_SinifDersleri()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnWidth(0,250)
        self.ui.tableWidget.setColumnWidth(1,350)
        self.ui.tableWidget.setRowHeight(0,50)
        font = QFont("Arial", 15, QFont.Bold) # You can adjust the font family and size
        self.ui.tableWidget.setFont(font)
        self.ui.tableWidget.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.ui.tableWidget.setSelectionMode(QAbstractItemView.NoSelection)
        self.db =  DbManager()

        class_names =self. db.fill_comobox_withClass_names()
        for i in class_names:
            self.ui.class_names.addItems(i)
        self.ui.class_names.setCurrentIndex(-1)
        self.ui.class_names.currentIndexChanged.connect(self.on_class_names_selected)# bir class secilirse
   
    def on_class_names_selected(self):
        class_name = self.ui.class_names.currentText()
        class_id = self.db.getClassId(class_name) # class id getir
        print(class_id)
       
        information = self.db.getAllLessonInfoForTheClass(class_id)
        
        if information is None:
            message = f"<b><font size='7'> Bu sınıfın ait dersleri bulunmadı</font></b>"    
            QMessageBox().warning(self, "Bilgilendirme", message)
            return
        
        lesson_ids = []
        teacher_ids = []
        

        for lesson_id, teacher_id in information:
            lesson_ids.append(lesson_id)
            teacher_ids.append(teacher_id)

        
        teacher_names_list = [] 
        lesson_names_list = [] 

        
        for i in range(1, len(teacher_ids) + 1):
                id = teacher_ids[i - 1]
                gelen_teacher_name = self.db.getTeacherNameByIdFromTeacher(id)
                teacher_names_list.append(gelen_teacher_name)

        for i in range(1, len(teacher_ids) + 1):
                id = lesson_ids[i - 1]
                gelen_lesson_name = self.db.getLessonNamesByIdFromLesson(id)#getLessonNamesByIdFromclassLesson
                lesson_names_list.append(gelen_lesson_name)
        # print(lesson_names_list)
        # print(teacher_names_list)



        if not lesson_names_list:
            message = "<b><font size='7'> Bu sınıfın ait dersleri bulunmadı</font></b>"
            QMessageBox().warning(self, "Bilgilendirme", message)
            return
        else:

            self.ui.tableWidget.setRowCount(len(lesson_names_list))

            for row, (lesson_name, teacher_name) in enumerate(zip_longest(lesson_names_list, teacher_names_list, fillvalue='')):
                    item_lesson = QtWidgets.QTableWidgetItem(lesson_name)
                    item_teacher = QtWidgets.QTableWidgetItem(teacher_name)

                    self.ui.tableWidget.setItem(row, 0, item_lesson)
                    self.ui.tableWidget.setItem(row, 1, item_teacher)
                                


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())
