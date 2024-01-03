from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget, QPushButton, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIntValidator, QFont
from dbmanager import DbManager

class MyMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.db = DbManager()
        self.student_id = None
        self.ders_id = None

        background_color = '#BCA37F'
        search_background_color = '#EAD7BB'
        bn_bak = '#113946'
        button_font = QFont("Arial", 16)
        search_font = QFont("Arial", 16, QFont.Bold)  # Use bold for the search text
        search_input_font = QFont("Arial", 14)  # Smaller font for the input text

        self.setStyleSheet(f'background-color: {background_color};')

        self.setWindowTitle("Öğrenci puanları girme sayfası")
        self.setGeometry(100, 100, 800, 600)

        self.student_number_input = QLineEdit(self)
        self.student_number_input.setPlaceholderText("Öğrenci numarası")
        self.student_number_input.setFont(search_input_font)  

        # Search Button
        search_button = QPushButton('Ara', self)
        search_button.setFont(button_font)
        search_button.setStyleSheet(f'color: white; background-color: {bn_bak};')
        search_button.clicked.connect(self.search_student)

        # Table Widget
        self.table_widget = QTableWidget(self)
        self.table_widget.setHorizontalHeaderLabels(['Ders', 'puan', ''])
        header = self.table_widget.horizontalHeader()
        header.setFont(QFont("Arial", 16))


        # Layout
        layout = QVBoxLayout()
        layout.addWidget(self.student_number_input)
        layout.addWidget(search_button)
        layout.addWidget(self.table_widget)

        # Central Widget
        central_widget = QWidget(self)
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def search_student(self):
        entered_student_number = self.student_number_input.text()
        if not entered_student_number:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText("Öğrenci numarasını girmelisiniz.")
            msg.setWindowTitle("Uyarı")
            msg.setStyleSheet("color: red;")
            msg.exec_()
        else:
            self.student_id = self.db.getStudentIdformStudentByStudentNumber(entered_student_number)
            class_id = self.db.getClassIdFromStudentByStudentNumber(entered_student_number)
            class_name = self.db.getClassName(class_id)
            if class_name is not None:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f"{entered_student_number} numaralı öğrenci {class_name} sınıfında okuyor  ")
                msg.setWindowTitle("Uyarı")
                msg.setStyleSheet("color: green;")
                msg.exec_()
                self.table_widget.clearContents()
                self.table_widget.setRowCount(0)
                class_lessonid_and_teachersId_information = self.db.getAllLessonInfoForTheClass(class_id)
                lesson_ides2 = [row[0] for row in class_lessonid_and_teachersId_information]
                lesson_names_list = [self.db.getLessonNamesByIdFromLesson(id) for id in lesson_ides2]

                num_rows = max(len(lesson_names) for lesson_names in lesson_names_list) if lesson_names_list else 0
                num_cols = 3  

                self.table_widget.setRowCount(num_rows)
                self.table_widget.setColumnCount(num_cols)

                for row, lesson_names in enumerate(lesson_names_list):
                    item = QTableWidgetItem(lesson_names)
                    item.setFlags(item.flags() ^ Qt.ItemIsEditable)  # Make the item non-editable
                    item.setFont(QFont("Arial", 16))  
                    self.table_widget.setItem(row, 0, item)

                    grade_input = QLineEdit(self)
                    grade_input.setValidator(QIntValidator(0, 100))  
                    grade_input.setFont(QFont("Arial", 16))  
                    self.table_widget.setCellWidget(row, 1, grade_input)

                    button = QPushButton('Gir', self)
                    button.setFont(QFont("Arial", 16))
                    button.setStyleSheet('background-color: #113946; color: white;')
                    button.clicked.connect(lambda _, r=row: self.enter_grade(r))
                    self.table_widget.setCellWidget(row, 2, button)

                # تعديل عرض الأعمدة
                for col in range(num_cols):
                    self.table_widget.setColumnWidth(col, 250)# 

            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f"{entered_student_number} numaralı öğrenci sınıfı bulunmuyor  ")
                msg.setWindowTitle("Uyarı")
                msg.setStyleSheet("color: red;")
                msg.exec_()

    def enter_grade(self, row):
        ders_adi = self.table_widget.item(row, 0).text()
        grade_input = self.table_widget.cellWidget(row, 1)
        entered_grade = grade_input.text()

        try:
            puan = int(entered_grade)
            if 0 <= puan <= 100:
                self.ders_id = self.db.getLessonId(ders_adi)
                self.db.addSudentPuan(self.student_id, self.ders_id, puan)
                grade_input.clear()
            else:
                raise ValueError("Notlar 100-0 ile arasinda olmasi gerekir.")
        except ValueError as e:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(str(e))
            msg.setWindowTitle("Error")
            msg.setStyleSheet("color: red;")
            msg.exec_()

if __name__ == '__main__':
    app = QApplication([])
    main_window = MyMainWindow()
    main_window.show()
    app.exec_()
