from PyQt5 import QtWidgets
from egitmen_dersleri import Ui_ogretmenDersleri
from Student import Student
import dbmanager
import ogrenci_islemleri2
import addTeacher2 
from PyQt5.QtWidgets import QMessageBox, QInputDialog
import editTeacher2
from itertools import zip_longest



import addTeacher2
class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_ogretmenDersleri()
        self.ui.setupUi(self)
        self.db = dbmanager.DbManager()
        self.ui.gosterbtn.clicked.connect(self.print)
        self.teacher_id = None
        self.ui.teacherDersTable.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.teacherDersTable.setColumnWidth(0,250)
        self.ui.teacherDersTable.setColumnWidth(1,238)
        class_names =self. db.fill_comobox_withClass_names()
       


    

           
        
    def print(self):
        teacher_number_text = self.ui.teacher_number_text.toPlainText()
        teacher = self.db.getTeacherByNumber(teacher_number_text)
        
        if teacher is not None:
            self.teacher_id=teacher[0].id
        classnames_and_lessons = self.db.getAllLessonInfoForTheClassByTeacherId(self.teacher_id)
        self.ui.gosterbtn.clicked.connect(self.print)
        lesson_ids = []
        class_ids = []
        for item in classnames_and_lessons:
            lesson_ids.append(item[0])
            class_ids.append(item[1])

        # print("Dersler idler :", lesson_ids)
        # print("siniflar idler ", class_ids)


        class_names_list = [] 
        lesson_names_list = [] 

        
        for i in range(1, len(class_ids) + 1):
                id = class_ids[i - 1]
                gelenclass_name = self.db.getClassName(id)
                class_names_list.append(gelenclass_name)

        for i in range(1, len(class_ids) + 1):
                id = lesson_ids[i - 1]
                gelen_lesson_name = self.db.getLessonNamesByIdFromLesson(id)
                lesson_names_list.append(gelen_lesson_name)
        # print(class_names_list)
        # print(lesson_names_list)

        if not lesson_names_list:
            message = f"<b><font size='7'> {self.ui.teacher_number_text} Bu numaraya sahip öğretmen herhangi bir ders vermiyor</font></b>"
            QMessageBox().warning(self, "Bilgilendirme", message)
            return
        else:

            self.ui.teacherDersTable.setRowCount(len(lesson_names_list))

            for row, (lesson_name, teacher_name) in enumerate(zip_longest(lesson_names_list, class_names_list, fillvalue='')):
                    item_lesson = QtWidgets.QTableWidgetItem(lesson_name)
                    item_teacher = QtWidgets.QTableWidgetItem(teacher_name)

                    self.ui.teacherDersTable.setItem(row, 0, item_lesson)
                    self.ui.teacherDersTable.setItem(row, 1, item_teacher)
                                

        







if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())       
        