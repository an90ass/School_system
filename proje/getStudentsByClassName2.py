from getStudentsByClass import Ui_GetStudents
from PyQt5 import QtWidgets
from dbmanager import DbManager

class myApp(QtWidgets.QMainWindow):

    def __init__(self):
        super(myApp, self).__init__()
        self.ui = Ui_GetStudents()
        self.ui.setupUi(self)
        self.ui.get_students_comboBox.activated.connect(self.get_students)
        db = DbManager()
        class_names = db.fill_comobox_withClass_names()
        for i in class_names:
            self.ui.get_students_comboBox.addItems(i)

        self.ui.get_students_table.setColumnWidth(0,100)
        self.ui.get_students_table.setColumnWidth(1,150)
        self.ui.get_students_table.setColumnWidth(2,150)
        self.ui.get_students_table.setColumnWidth(3,250)
        self.ui.get_students_table.setColumnWidth(4,70)


        self.ui.get_students_comboBox.setCurrentIndex(-1)


    def get_students(self):
        class_name = self.ui.get_students_comboBox.currentText()
        if class_name is not None:
            db = DbManager()
            students, teacher_name = db.getStudentByClassName(class_name)
            if students is not None:
                info_text = ""
                for student in students:
                    info_text += f"Student Name: {student.student_surname}\n"
                self.load_Student(students,teacher_name)
        else:
            self.ui.get_students_table.clearContents()

    def load_Student(self, students_information,teacher_name):
        # Clear any existing data in the table
        self.ui.rehberlik_hoca_lbl.setText(" "+teacher_name)
        self.ui.get_students_table.clearContents()

        # Set the number of rows in the table based on the number of students
        self.ui.get_students_table.setRowCount(len(students_information))

        for row, student in enumerate(students_information):
            # Add student information to each row
            columon_names = [str(student.student_number), student.student_name, student.student_surname, str(student.student_birthday), student.student_gender]
            for col, value in enumerate(columon_names):
                item = QtWidgets.QTableWidgetItem(value)
                self.ui.get_students_table.setItem(row, col, item)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = myApp()
    window.show()
    sys.exit(app.exec_())
