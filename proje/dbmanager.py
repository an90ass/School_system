import mysql.connector
from datetime import date
from connection import connection
from Student import Student
from Teacher import Teacher
from Class import Class
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtGui import QColor
from Lesson import Lesson
from classlesson import ClassLesson
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QInputDialog
from PyQt5.QtWidgets import QCheckBox

class DbManager:
    def __init__(self):
        self.connection = connection
        self.cursor = self.connection.cursor()
    @staticmethod
    def getStudentByName(name_or_number):
        # sql = "SELECT * FROM student WHERE Name = %s OR StudentNumber = %s"
        # value = (name_or_number,name_or_number)    
        # cursor = DbManager().cursor
        # cursor.execute(sql, value)       
        # try:
        #     obj = cursor.fetchone()  
        #     if obj:
        #         return Student.CreatStudent(obj)
        #     else:
        #         return None
        # except mysql.connector.Error as err:
        #      print("Error", err)
        try:
            cursor = connection.cursor()
            cursor.callproc("getStudentByName", [name_or_number,])
            result = list(cursor.stored_results())[0].fetchone()
            if result is not None:
                print(result)
                return Student.CreatStudent(result)
            else:
                print("No result found.")
                return None
        except mysql.connector.Error as err:
            print("Error executing stored procedure:", err)
        finally:
            cursor.close()

             
    def getStudentByClassName(self, class_name):
            try:
                # First, get the class_id and teacher_id from the 'class' table
                sql1 = "SELECT id, TeacherId FROM class WHERE Name = %s"
                value1 = (class_name,)
                self.cursor.execute(sql1, value1)
                class_data = self.cursor.fetchone()

                if class_data:
                    class_id = class_data[0]
                    teacher_id = class_data[1]

                    # Now, retrieve students by class_id
                    sql2 = "SELECT * FROM student WHERE ClassId = %s"
                    value2 = (class_id,)
                    self.cursor.execute(sql2, value2)
                    students = self.cursor.fetchall()

                    # Now, retrieve teacher name by teacher_id
                    sql3 = "SELECT Name FROM Teacher WHERE Id = %s"
                    value3 = (teacher_id,)
                    self.cursor.execute(sql3, value3)
                    teacher_name = self.cursor.fetchone()[0]

                    return Student.CreatStudent(students), teacher_name
                else:
                    return None, None

            except mysql.connector.Error as err:
                print("Error:", err)

    def fill_comobox_withClass_names(self):
       
            # Execute an SQL query to get class names from the 'class' table
            # sql = "SELECT Name FROM class"
            # self.cursor.execute(sql)

            # class_names = self.cursor.fetchall()
          
            # return class_names
            try:
                    self.cursor.callproc("GetClassNames")

                    result = []
                    for result_cursor in self.cursor.stored_results():
                            result.extend(result_cursor.fetchall())
                            self.connection.commit()
                    return result
            except mysql.connector.Error as err:
                 print("Error", err)
        

    # def  getClassId(self,name) : # tekrarlanan method
    #     sql = "select Id from Class Where Name =%s"
    #     value = (sql,value)
    #     self.cursor.execute(sql, value)
    def getClassName(self,classid):#by id
         
        # sql = "SELECT Name FROM class WHERE Id = %s"
        # value = (classid,)
        # self.cursor.execute(sql, value)
        # class_name = self.cursor.fetchone()
        # if class_name is not None:
        #     return class_name[0]
        # else:
        #     return None 
            cursor = None
         
            try:           
                    cursor = connection.cursor()

                    self.cursor.callproc("GetClassNameById",(classid,))

                    result = []
                    for result_cursor in self.cursor.stored_results():
                            result.extend(result_cursor.fetchall())
                            self.connection.commit()
                    # print(result[0][0])
                    return result[0][0]
                     
            
            except mysql.connector.Error as err:
                 print("Error", err)
            finally:
                     if cursor is not None:
                        cursor.close()
        
             
    def addStudent(self,student:Student):
        class_id = self.getClassId(student.classid)

        check_sql = "SELECT 1 FROM Student WHERE StudentNumber = %s"
        check_values = (student.student_number,)
        self.cursor.execute(check_sql, check_values)
        result = self.cursor.fetchone()

        if result:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f'<font color="red"> Öğrenci veritabanında zaten mevcut: {student.student_number} .</font>')
            msg.setWindowTitle('Hata')
            msg.exec_()
        else:
            procedure_name = "addStudent"
            params = (
                student.student_number,
                student.student_name,
                student.student_surname,
                student.student_birthday,
                student.student_gender,
                class_id  # Make sure to set the class_id appropriately
            )

            try:
                self.cursor.callproc(procedure_name, params)
                self.connection.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f'<font color="green"> Öğrenci başarıyla veritabanına eklendi: {student.student_number} .</font>')
                msg.setWindowTitle('Ekleme işlemi başarıdı')
                msg.exec_()
            except mysql.connector.Error as err:
                print("Eklemede hata olustu", err)
    def getClassId(self, class_name):
        sql = "SELECT Id FROM Class WHERE Name = %s"
        value = (class_name,)
        self.cursor.execute(sql, value)
        class_id = self.cursor.fetchone()
        
        if class_id is not None:
            return class_id[0]
        else:
            return None
        # self.cursor.execute("CALL GetClassIdByName(%s)", (class_name,))
        # result = self.cursor.fetchone()
        # print(result)
        # if result is not None:
        #     return result[0]
        # else:
        #     return None


    def editStudent(self, student: Student):
            class_id = self.getClassId(student.classid)

            procedure_name = "editStudent"
            params = (
                student.student_name,
                student.student_surname,
                student.student_birthday,
                student.student_gender,
                class_id,  # Make sure to set the class_id appropriately
                student.student_number
            )

            try:
                    self.cursor.callproc(procedure_name, params)
                    self.connection.commit()
            except mysql.connector.Error as err:
                    print("Duzenlemede hata olustu", err)


    def deletStudent(self,student_number):
                # إعداد الاستعلام SQL للتحقق من وجود الرقم
        check_sql = "SELECT 1 FROM Student WHERE StudentNumber = %s"
        check_values = (student_number,)

        # قم بتنفيذ الاستعلام للتحقق من وجود الرقم في قاعدة البيانات
        self.cursor.execute(check_sql, check_values)
        result = self.cursor.fetchone()

        # if result:
        #     # إذا وجد الرقم، قم بعملية الحذف
        #     # إعداد الاستعلام SQL لحذف الطالب بناءً على رقم الطالب
        #     sql = "DELETE FROM Student WHERE StudentNumber = %s"
        #     values = (student_number,)

        #     try:
        #         self.cursor.execute(sql, values)
        #         self.connection.commit()

        #         # إظهار رسالة تأكيد باستخدام QMessageBox
        #         msg = QMessageBox()
        #         msg.setIcon(QMessageBox.Information)
        #         msg.setText(f'<font color="green"> Öğrenci başarıyla veritabanından silindi: {student_number} .</font>')
        #         msg.setWindowTitle('Silme işlemi başarıdı')
        #         msg.exec_()
                
        #     except mysql.connector.Error as err:
        #         print("Silme işleminde bir hata oluştu:", err)
        # else:
        #     # إذا لم يتم العثور على الرقم، قم بعرض رسالة بأن الرقم غير موجود
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
        #     msg.setText(f'<font color="red"> Öğrenci veritabanında bulunamadı: {student_number} .</font>')
        #     msg.setWindowTitle('Hata')
        #     msg.exec_()
        if result:
   

            try:
                params = (student_number,)
                self.cursor.callproc("deletStudent", params)
                self.connection.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f'<font color="green"> Öğrenci başarıyla veritabanından silindi: {student_number} .</font>')
                msg.setWindowTitle('Silme işlemi başarıdı')
                msg.exec_()
            except mysql.connector.Error as err:
                print("hata", err)
        else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f'<font color="red"> Öğrenci veritabanında bulunamadı: {student_number} .</font>')
                msg.setWindowTitle('Hata')
                msg.exec_()
    #Teacher
    def addTeacher(self,teacher:Teacher):
    
        # check_sql = "SELECT T_number FROM teacher WHERE T_number = %s "
        # check_values = (teacher.teacher_number,)  # Note the comma to create a tuple with a single element
        # self.cursor.execute(check_sql, check_values)
        # result = self.cursor.fetchone()
        check_sql = "CALL CheckTeacherExists(%s, @result)"
        check_values = (teacher.teacher_number,)

        self.cursor.execute(check_sql, check_values)
            
            # Fetch the result
        self.cursor.execute("SELECT @result")
        result_exists = self.cursor.fetchone()[0]

            # Check the result
        if result_exists:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f'<font color="red"> Eğitmen veritabanında zaten mevcut: {teacher.teacher_number} .</font>')
            msg.setWindowTitle('Hata')
            msg.exec_()
        else:
           
            procedure_name = "addTeacher"
            params = (
                teacher.teacher_number,
                teacher.teacher_name,
                teacher.teacher_surname,
                teacher.teacher_birthday,
                teacher.teacher_gender
            )

            try:
                self.cursor.callproc(procedure_name, params)
                self.connection.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f'<font color="green"> Eğitmen başarıyla veritabanına eklendi: {teacher.teacher_name} .</font>')
                msg.setWindowTitle('Ekleme işlemi başarıdı')
                msg.exec_()
            except mysql.connector.Error as err:
                print("Eklemede hata olustu", err)
    def editTeacher(self, teacher: Teacher):
                    procedure_name = "editTeacher"
                    params = (
                        teacher.teacher_number,
                        teacher.teacher_name,
                        teacher.teacher_surname,
                        teacher.teacher_birthday,
                        teacher.teacher_gender,
                        teacher.id
                    )
                    try:
                        self.cursor.callproc(procedure_name, params)
                        self.connection.commit()
                    except mysql.connector.Error as err:
                        print("ogretmen degistirmedede hata oldu:", err)                
                        print("Ogretmen veri tabaninda bulunmadi.")

    def deleteTeacher(self,teacher_number):
        # check_sql = "SELECT 1 FROM teacher WHERE T_number = %s"
        # check_values = (teacher_number,)

        # self.cursor.execute(check_sql, check_values)
        # result = self.cursor.fetchone()

        check_sql = "CALL CheckTeacherExists(%s, @result)"
        check_values = (teacher_number,)

        self.cursor.execute(check_sql, check_values)
            
            # Fetch the result
        self.cursor.execute("SELECT @result")
        result_exists = self.cursor.fetchone()[0]

        # if result:
        #     sql = "DELETE FROM teacher WHERE T_number = %s"
        #     values = (teacher_number,)

        #     try:
        #         self.cursor.execute(sql, values)
        #         self.connection.commit()

        #         msg = QMessageBox()
        #         msg.setIcon(QMessageBox.Information)
        #         msg.setText(f'<font color="green"> Eğitmen başarıyla veritabanından silindi: {teacher_number} .</font>')
        #         msg.setWindowTitle('Silme işlemi başarıdı')
        #         msg.exec_()
                
        #     except mysql.connector.Error as err:
        #         print("Silme işleminde bir hata oluştu:", err)
        # else:
        #     msg = QMessageBox()
        #     msg.setIcon(QMessageBox.Warning)
        #     msg.setText(f'<font color="red"> Eğitmen veritabanında bulunamadı: {teacher_number} .</font>')
        #     msg.setWindowTitle('Hata')
        #     msg.exec_()


        if result_exists:
   

            try:
                params = (teacher_number,)
                self.cursor.callproc("deleteTeacher", params)
                self.connection.commit()
            

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f'<font color="green"> Eğitmen başarıyla veritabanından silindi: {teacher_number} .</font>')
                msg.setWindowTitle('Silme işlemi başarıdı')
                msg.exec_()
            except mysql.connector.Error as err:
                print(" Hata teacher silmede:", err)
        else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f'<font color="red"> Eğitmen veritabanında bulunamadı: {teacher_number} .</font>')
                msg.setWindowTitle('Hata')
                msg.exec_()
    @staticmethod
    def getTeacherByNumber(teacher_number):
        sql = "SELECT * FROM teacher WHERE T_number = %s "
        value = (teacher_number,)

        try:
            cursor = DbManager().cursor
            cursor.execute(sql, value)
            obj = cursor.fetchone()
            print(obj)

            if obj is not None:
                return Teacher.CreatTeacher(obj)
            else:
                return None
        except mysql.connector.Error as err:
            print("Error", err)
    #     cursor = connection.cursor()
    #     # sql = "SELECT * FROM teacher WHERE T_number = %s "
    #     # value = (teacher_number,)
    #     sql = "CALL GetTeacherByNumber(%s)"
    #     value = (teacher_number,)

    #     try:
    #         cursor.execute(sql, value)

    # # Fetch the result set
    #         result = cursor.fetchall()
    #         print("********************************8")
    #         print(result[0])

    #         if result is not None:
    #             return Teacher.CreatTeacher(result[0])
    #         else:
    #             return None
    #     except mysql.connector.Error as err:
    #         print("Error", err)

    def deleteClass(self,id):
            # sql = "DELETE FROM class WHERE Id = %s"
            # values = (id,)

            # try:
            #         self.cursor.execute(sql, values)
            #         self.connection.commit()

            #         # إظهار رسالة تأكيد باستخدام QMessageBox
            #         print("Basariyla silendi")
                    
            # except mysql.connector.Error as err:
            #         print("Silme işleminde bir hata oluştu:", err) 
            params = (id,)

            try:
                self.cursor.callproc("deleteClass", params)
                self.connection.commit()
                print("Basariyla silendi")

            except mysql.connector.Error as err:
                    print("Silme işleminde bir hata oluştu:", err) 
    
    def fill_comoboxTeachersNames(self):
        try:
            # Execute an SQL query to get class names from the 'class' table
            sql = "SELECT Name FROM Teacher"
            self.cursor.execute(sql)
            class_names = self.cursor.fetchall()          
            return class_names
        except mysql.connector.Error as err:
            print("Error", err)
    def getTeacherId_toSaveIt_inClassTable_OR_ClassLessonTable(self, teacher_name):
            try:
                sql = 'SELECT Id from teacher WHERE NAME =%s'
                value = (teacher_name,)
                self.cursor.execute(sql, value)
                teacher_id = self.cursor.fetchone()
                self.connection.commit()
                if teacher_id is not None:
                    return teacher_id[0]
                else:
                    return None
            except mysql.connector.Error as err:
                print("Hocanin Id si veritabanindan getirme isleminde bir hata oluştu:", err) # tablo da ayni isimli iki ogretmen varsa
                
 
    def addClass(self,_class:Class):
            check_sql = "SELECT 1 FROM class WHERE Name = %s "
            check_values = (_class.class_name,)

            self.cursor.execute(check_sql, check_values)
            result = self.cursor.fetchone()
            if  result:
                        # If the class exists, display a warning message
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Warning)
                        msg.setText(f'<font color="red"> {_class.class_name} sınıfı veritabanında zaten mevcuttur.</font>')
                        msg.setWindowTitle('Hata')
                        msg.exec_()
            else:
                        procedure_name = "addClass"
                        params = (
                            _class.class_name,
                            _class.teacher_id
                        )

                        try:
                            self.cursor.callproc(procedure_name, params)
                            self.connection.commit()
                            # Display a success message
                            msg = QMessageBox()
                            msg.setIcon(QMessageBox.Information)
                            msg.setText(f'<font color="green"> Sınıf başarıyla veritabanına eklendi: {_class.class_name}.</font>')
                            msg.setWindowTitle('Ekleme işlemi başarıdı')
                            msg.exec_()
                        except mysql.connector.Error as err:
                            print("Eklemede hata oluştu:", err)


    def getTeacherIdFromClass(self,class_name):
     
        # try:
        #     # Execute an SQL query to get class names from the 'class' table
        #     sql = 'Select TeacherId From class WHERE Name =%s'               
        #     value = (class_name,)
        #     self.cursor.execute(sql,value)
        #     teacher_id = self.cursor.fetchone() 
        #     print("333333333") 
        #     print(teacher_id)      
        #     print("333333333333")  
        #     return teacher_id[0]
        # except mysql.connector.Error as err:
        #     print("Error", err)
        try:
            self.cursor.callproc("GetTeacherIdByClassName", [class_name])
            result = []
            for result_cursor in self.cursor.stored_results():
                result.extend(result_cursor.fetchall())
            return result[0][0]

        except mysql.connector.Error as err:
            print("Error:", err)
            return None

    # def getTeacherNameBYId(self,teacher_id):   
    #         #try:  
    #            # sql = "SELECT Name FROM Teacher WHERE Id = %s"
    #            #value = (teacher_id,)
    #            # self.cursor.execute(sql, value)
    #            # teacher_name = self.cursor.fetchone() 
    #            # return teacher_name   
    #         try:  
    #             sql = "SELECT Name FROM Teacher WHERE Id = %s"
    #             value = (teacher_id,)
    #             self.cursor.execute(sql, value)
    #             result = self.cursor.fetchone() 
    #             teacher_name = result[0] if result else None  # Use None if no result is found

    #             return teacher_name
    #         except mysql.connector.Error as err:
    #                 print("Error", err)




                    
    def Make_sure_that_the_teacher_is_responsible_for_another_class(self,teacher_id):
        
        #   try:  
        #         sql = "SELECT Name FROM class WHERE TeacherId = %s"
        #         value = (teacher_id,)
        #         self.cursor.execute(sql, value)
        #         classname = self.cursor.fetchall()
        #         print("++++++++++++++++++++")
        #         print(classname)
        #         print("++++++++++++++++")
        #         return classname
        #   except mysql.connector.Error as err:
        #             print("Error", err)
        try:
            self.cursor.callproc("GetClassNameByTeacherId", [teacher_id])
            result = []
            for result_cursor in self.cursor.stored_results():
                result.extend(result_cursor.fetchall())
          
            return result

        except mysql.connector.Error as err:
            print("Error:", err)
            return None
         






    def editClass_sorumlusu(self,_class:Class):
            procedure_name = "editClass_sorumlusu"
            params = (_class.teacher_id, _class.class_name)

            try:
                self.cursor.callproc(procedure_name, params)
                self.connection.commit()
            except mysql.connector.Error as err:
                print("Duzenlemede hata olustu", err)
    def editClass(self,old_class_name,new_class_name):
        check_sql = "SELECT 1 FROM class WHERE Name = %s"
        check_values = (new_class_name,)

        # Assuming self.cursor and self.connection are initialized somewhere
        self.cursor.execute(check_sql, check_values)
        result = self.cursor.fetchone()

        if result:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f'<font color="red"> Girdiğiniz sınıf adı zaten mevcut. Lütfen farklı bir sınıf adı girin: {new_class_name}.</font>')
            msg.setWindowTitle('Hata')
            msg.exec_()
        else:
            procedure_name = "editClass"
            params = (new_class_name, old_class_name)

            try:
                self.cursor.callproc(procedure_name, params)
                self.connection.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText("Sınıfın adı başarıyla güncellendi.")
                msg.setWindowTitle("Başarılı")
                msg.exec()
            except mysql.connector.Error as err:
                print("   hata ", err)
    def deletClass(self,class_name):
        check_sql = "SELECT 1 FROM class WHERE Name = %s"
        check_values = (class_name,)

        self.cursor.execute(check_sql, check_values)
        result = self.cursor.fetchone()

        if result:
            procedure_name = "deletClass"
            params = (class_name,)

            try:
                self.cursor.callproc(procedure_name, params)
                self.connection.commit()

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f'<font color="green"> Sinif başarıyla veritabanından silindi: {class_name} .</font>')
                msg.setWindowTitle('Silme işlemi başarıdı')
                msg.exec_()
                
            except mysql.connector.Error as err:
                print("Silme işleminde bir hata oluştu:", err)
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Warning)
            msg.setText(f'<font color="red"> Sinif veritabanında bulunamadı: {class_name} .</font>')
            msg.setWindowTitle('Hata')
            msg.exec_()
    
    def addLesson(self, lesson):
        cursor = connection.cursor()

        try:
                cursor.callproc('addLesson', (lesson.lesson_name,))

                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText(f'<font color="green"> Ders başarıyla veritabanına eklendi.</font>')
                msg.setWindowTitle('Ekleme işlemi başarılı')
                msg.exec_()

        except mysql.connector.Error as err:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Warning)
                msg.setText(f'<font color="red"> Ders onceden vardi: {lesson.lesson_name} .</font>')
                msg.setWindowTitle('Ekleme işlemi başarsiz')
                msg.exec_()


    def deletLesson(self,ders_adi):

                try:
                    cursor = connection.cursor()

                    # حذف الفصل باستخدام اسم الفصل
                    cursor.execute("CALL deletLesson(%s, @success_var)", (ders_adi,))

                    # جلب قيمة المتغير من الناتج
                    cursor.execute("SELECT @success_var")
                    success_value = cursor.fetchone()[0]

                    connection.commit()

                    if success_value > 0:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText(f'<font color="green"> Ders başarıyla veritabanından silindi: {ders_adi} .</font>')
                        msg.setWindowTitle('Silme işlemi başarıdı')
                        msg.exec_()
                    else:
                        print(f'Ders bulunamadı: {ders_adi}')

                except mysql.connector.Error as err:
                    print("Silme işleminde bir hata oluştu:", err)

                finally:
                    if cursor:
                        cursor.close()
                        
       
    
    def editLesson(self,lesson:Lesson,new_lesson_name):
                # check_sql = "SELECT 1 FROM lesson WHERE Name = %s"# yeni sinif adi daha onceden mevcut mu ?
                # check_values = (new_lesson_name,)

                # # Assuming self.cursor and self.connection are initialized somewhere
                # self.cursor.execute(check_sql, check_values)
                # result = self.cursor.fetchone()
                # if  result:
                #         msg = QMessageBox()
                #         msg.setIcon(QMessageBox.Warning)
                #         msg.setText(f'<font color="red"> Eklemeye çalıştığınız yeni dersin adı zaten veritabanında mevcut, Başka bir dersin adını girin: {lesson.lesson_name}.</font>')
                #         msg.setWindowTitle('Hata')
                #         msg.exec_()               
                # else:
            cursor = connection.cursor()

            try:
                success_value = cursor.callproc('editLesson', [lesson.lesson_name, new_lesson_name, None])

                connection.commit()

                output_parameter_value = success_value[2]

                if output_parameter_value == 1:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Information)
                    msg.setText('<font color="green">Ders adı başarıyla değiştirilmiştir.</font>')
                    msg.setWindowTitle('Başarı')
                    msg.exec_()
                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText('<font color="red">Değiştirmek istediğiniz ders veritabanında mevcut değildir.</font>')
                    msg.setWindowTitle('Hata')
                    msg.exec_()

            except Exception as e:
                print(f"An error occurred: {str(e)}")

            finally:
                 cursor.close()



            
                            

    def chek_lesson_is_in_db(self,lesson:Lesson):
        check_sql = "SELECT 1 FROM lesson WHERE Name = %s"
        check_values = (lesson.lesson_name,)

        # Assuming self.cursor and self.connection are initialized somewhere
        self.cursor.execute(check_sql, check_values)
        result = self.cursor.fetchone()
        return result
    
    # def  getLessonId(self,lesson_name) : tekrarlanan metot
    #     sql = "SELECT Id from lesson Where Name =%s"
    #     value = (lesson_name,)
    #     self.cursor.execute(sql, value)
    #     lesson_id = self.cursor.fetchone()
    #     if lesson_id is not None:
    #         return lesson_id[0]
    #     else:
    #         return None
    def addClassLesson(self,classlesson:ClassLesson):
            procedure_name = "addClassLesson"
            params = (classlesson.class_id, classlesson.lesson_id, classlesson.teacher_id)

            try:
                self.cursor.callproc(procedure_name, params)
                self.connection.commit()
                
            except mysql.connector.Error as err:
                print("Eklemede hata olustu", err)
    def fill_comoboxLessonNames(self):
        # try:
        #     # Execute an SQL query to get class names from the 'class' table
        #     sql = "SELECT Name FROM lesson ORDER BY Name"#ORDER BY Name
        #     self.cursor.execute(sql)
        #     lesson_names = self.cursor.fetchall()          
        #     return lesson_names
            try:
                self.cursor.callproc("getAllLessonNames")

                result = []
                for result_cursor in self.cursor.stored_results():
                    result.extend(result_cursor.fetchall())
                    self.connection.commit()
                return result
            except mysql.connector.Error as err:
                print("Error", err)

    def getLessonId(self, lesson_name):
        # sql = "SELECT Id FROM lesson WHERE Name = %s"
        # value = (lesson_name,)
        # self.cursor.execute(sql, value)
        # lesson_id = self.cursor.fetchone()
        # print(")))))))))))))))")
        # print(lesson_id)
        # print("(((((((((((())))))))))))")
        # if lesson_id is not None:
        #     return lesson_id[0]
        # else:
        #     return 
        try:
                self.cursor.callproc("GetLessonIdByName", [lesson_name])
                result = []
                for result_cursor in self.cursor.stored_results():
                    result.extend(result_cursor.fetchall())
                # print(result[0])
                return result[0][0]

        except mysql.connector.Error as err:
                print("Error:", err)
                return None
    
        




    def getTeacherIdFromclasslessonSecilen_ders_icin_hangi_ogretmen_verdigini_bilmek_icin(self,lesson_id):#انا دخلت اسم الدرس واخذت الايدي حق واريد اعرف من يجيب هذا الدرس
        #  sql = "SELECT TeacherId FROM classlesson WHERE LessonId = %s"
        #  values = (lesson_id,)
        #  self.cursor.execute(sql, values)
        #  result = self.cursor.fetchone()
        #  print(")))))))))))))))")
        #  print(result)
        #  print("(((((((((((())))))))))))")
        #  teacher_id = result[0] if result else None  # Use None if no result is found

        #  return teacher_id
        try:
                self.cursor.callproc("GetTeacherIdByLessonId", [lesson_id])
                result = []
                for result_cursor in self.cursor.stored_results():
                    result.extend(result_cursor.fetchall())
                # print(result[0])
                return result[0][0]

        except mysql.connector.Error as err:
                print("Error:", err)
                return None
    
    def getAllLessonInfoForTheClass(self, class_id):
        # sql = "SELECT LessonId, TeacherId FROM classlesson WHERE ClassId = %s"
        # values = (class_id,)
        # self.cursor.execute(sql, values)
        # result = self.cursor.fetchall()
        # # print(result)
        # return result
            try:
                    self.cursor.callproc("getAllLessonInfoForTheClass",(class_id,))

                    result = []
                    for result_cursor in self.cursor.stored_results():
                            result.extend(result_cursor.fetchall())
                            self.connection.commit()
                    return result
            except mysql.connector.Error as err:
                 print("Error", err)

        
    def getAllLessonInfoForTheClassByTeacherId(self, TeacherId):
        # sql = "SELECT LessonId, ClassId FROM classlesson WHERE TeacherId = %s"
        # values = (TeacherId,)
        # self.cursor.execute(sql, values)
        # result = self.cursor.fetchall()
        # return result


        # procedure_name = "getAllLessonInfoForTheClassByTeacherId"
        # params = (TeacherId,)
        # self.cursor.callproc(procedure_name, params)
        # result = self.cursor.fetchall()
        # return result




        procedure_name = "getAllLessonInfoForTheClassByTeacherId"
        params = (TeacherId,)

        try:
            self.cursor.callproc(procedure_name, params)

            # Fetch the result using stored_results
            results = self.cursor.stored_results()
            result = None
            for result_cursor in results:
                result = result_cursor.fetchall()

            print("Parameters:", params)
            print("Result:", result)
            return result

        except mysql.connector.Error as err:
            print("Saklı yordam yürütülürken bir hata oluştu:", err)
            return None


        

    
    
    
    
    def dersi_veren_teacher_degistirme(self,lesson_id,teacher_id):
        procedure_name = "dersi_veren_teacher_degistirme"
        params = (teacher_id, lesson_id)

        try:
            self.cursor.callproc(procedure_name, params)
            self.connection.commit()
        except mysql.connector.Error as err:
                print("  hata ", err)

    # def getTeacherNamesById_s (self,ids):
    #     try:
    #         # Create a placeholder string for the number of IDs
    #         placeholders = ','.join(['%s'] * len(ids))

    #         # Use the IN operator in the SQL query
    #         sql = f"SELECT Name FROM Teacher WHERE Id IN ({placeholders})"
    #         values = tuple(ids)
            
    #         self.cursor.execute(sql, values)
    #         teacher_names_result = self.cursor.fetchall()

    #         # Extract names from the result and store only the last value in the list
    #         teacher_names = [result[0] for result in teacher_names_result[-1:]]

    #         # print(teacher_names)
            
    #         return teacher_names
    #     except mysql.connector.Error as err:
    #         print("Error", err)
    def getTeacherNameByIdFromTeacher(self,tid):
         # Use the IN operator in the SQL query
            # sql = "SELECT Name FROM Teacher WHERE Id = %s"
            # values = (tid,)
            
            # self.cursor.execute(sql, values)
            # teacher_names_result = self.cursor.fetchall()
            # return teacher_names_result[0][0]
                
        procedure_name = "GetTeacherNameById"
        self.cursor.callproc(procedure_name, [tid])

        # Fetch the result set
        result = []
        for result_cursor in self.cursor.stored_results():
            result.extend(result_cursor.fetchall())
        
        # print(result)
        return result[0][0]
    



    def getLessonNamesByIdFromLesson(self, lid):
        try:
            sql = "SELECT Name FROM lesson WHERE Id = %s"
            values = (lid,)
            
            self.cursor.execute(sql, values)
            lesson_names_result = self.cursor.fetchall()
            return lesson_names_result[0][0] 
        except mysql.connector.Error as err:
            print("Error", err)
        # secilen ders hangi classa ait
    def getClassIdFromclassLessonByLessonId(self,lesson_id):
         

         sql = "SELECT ClassId FROM classlesson WHERE LessonId = %s"
         values = (lesson_id,)
         self.cursor.execute(sql, values)
         result = self.cursor.fetchone()

         teacher_id = result[0] if result else None  # Use None if no result is found
         print(teacher_id)

         return teacher_id
        # try:
        #             procedure_name = "GetClassIdByLesson_Id"
        #             params = (lesson_id,)
        #             self.cursor.callproc(procedure_name, params)
        #             result = self.cursor.fetchone()


        #             # Fetch the result using stored_results
                    
        #             print(result)

        #             return result

        # except mysql.connector.Error as err:
        #             print("Saklı yordam yürütülürken :", err)
        #             return None
        







    # def getClasaas(self):
    #      sql = "SELECT ClassId FROM classlesson WHERE LessonId = %s"
    def getClassIdFromStudentByStudentNumber(self,student_number):
         sql = "SELECT ClassId FROM student WHERE StudentNumber = %s"
         values = (student_number,)
         self.cursor.execute(sql, values)
         result = self.cursor.fetchone()
         class_id = result[0] if result else None  # Use None if no result is found
         return class_id
    



    def getStudentIdformStudentByStudentNumber(self,student_number):
        sql = "SELECT Id FROM student WHERE StudentNumber = %s"
        value = (student_number,)
        self.cursor.execute(sql, value)
        class_id = self.cursor.fetchone()
        print(class_id)
        
        if class_id is not None:
            return class_id[0]
        else:
            return None
        # try:
        #     self.cursor.callproc("getStudentIdformStudentByStudentNumber", (student_number,))
        #     result = []
        #     for result_cursor in self.cursor.stored_results():
        #         result.extend(result_cursor.fetchall())
        #     print(result[0])
        #     return result[0]

        # except mysql.connector.Error as err:
        #     print("Error:", err)
        #     return None
            

         
        
    def addSudentPuan(self, Student_id, ders_id, _not):
            msg = QMessageBox()

            check_sql = "SELECT * FROM student_lesson WHERE studentId = %s AND lessonId = %s"
            check_values = (Student_id, ders_id)
            self.cursor.execute(check_sql, check_values)
            existing_entry = self.cursor.fetchone()

            if existing_entry:
                msg.setIcon(QMessageBox.Warning)
                msg.setText('<font color="red">Bu dersin puanı zaten eklenmiş.</font>')
                msg.exec_()
            else:
                procedure_name = "addSudentPuan"
                params = (Student_id, ders_id, _not)

                try:
                    self.cursor.callproc(procedure_name, params)
                    self.connection.commit()

                    msg.setIcon(QMessageBox.Information)
                    msg.setText('<font color="green">Not başarıyla eklendi.</font>')
                    msg.exec_()

                except mysql.connector.Error as err:
                    print("Eklemede hata oluştu", err)

                    
    def getStudentPuanlar(self,student_id):
        # sql = "SELECT * FROM student_lesson WHERE studentId =  %s"
        # value = (student_id,)    
        # cursor = DbManager().cursor
        # cursor.execute(sql, value)       
        # try:
        #     obj = cursor.fetchall()  
        #     if obj:
        #         return obj
        #     else:
        #         return None
        # except mysql.connector.Error as err:
        #      print("Error", err)
        try:
            self.cursor.callproc("getStudentPuanlar", (student_id,))
            result = []
            for result_cursor in self.cursor.stored_results():
                result.extend(result_cursor.fetchall())
            return result

        except mysql.connector.Error as err:
            print("Error:", err)
            return None

         
    def editStudentPuanlar(self,Student_id, ders_id, _not):
            procedure_name = "editStudentPuanlar"
            params = (_not, Student_id, ders_id)
            try:
                self.cursor.callproc(procedure_name, params)
                self.connection.commit()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Information)
                msg.setText('<font color="green">Öğrenci Notu başarıyla değiştirildi.</font>')
                msg.exec_()
            except mysql.connector.Error as err:
                print("Duzenlemede hata olustu", err)

    def GetStudents(self):
        sql = "SELECT * FROM student" #GetStudentsData
        try:
            cursor = DbManager().cursor
            cursor.execute(sql)
            students_data = cursor.fetchall()

            if students_data:
                # Assuming Student.CreateStudent is a method to create a Student object
                return [Student.CreatStudent(student) for student in students_data]
            else:
                return None
        except mysql.connector.Error as err:
            print("Error:", err)
            return None
            # cursor = None
            # try:
            #     cursor = connection.cursor()

            #     # Call the stored procedure
            #     self.cursor.execute("CALL GetStudents()")
            #     students_data = self.cursor.fetchall()

            #     if students_data:
            #         # Assuming Student.CreateStudent is a method to create a Student object
            #         return [Student.CreatStudent(student) for student in students_data]
            #     else:
            #         return None

            # except mysql.connector.Error as err:
            #     print("Error:", err)
            #     return None

            # finally:
            #          if cursor is not None:
            #             cursor.close()
        
    # def __exit__(self, exc_type, exc_value, traceback):
    #     self.cursor.close()
    #     self.connection.close()
    def GetTeachers(self):
        sql = "SELECT * FROM teacher" #GetTeachersData
        try:
            cursor = DbManager().cursor
            cursor.execute(sql)
            teacher_data = cursor.fetchall()

            if teacher_data:
                # Assuming Student.CreateStudent is a method to create a Student object
                return [Teacher.CreatTeacher(teacher) for teacher in teacher_data]
            else:
                return None
        except mysql.connector.Error as err:
            print("Error:", err)
            return None
    def GetClass(self):
        sql = "SELECT * FROM class" #GetClassData
        try:
            cursor = DbManager().cursor
            cursor.execute(sql)
            class_data = cursor.fetchall()
            # print(class_data)

            if class_data:
                return Class.get_classes(class_data)
            else:
                return None

            
        except mysql.connector.Error as err:
            print("Error:", err)
            return None

            
        


                
                

                


    
    
    


                






db = DbManager()
# student = db.getStudentByName(100)
# print(student[0].student_birthday)
# student = db.getStudentByClassName(1)
# # print(student[0].student_name)
# for student_record in student:
#     print(student_record.student_name)

# _class = db.fill_comobox_to_getStudents()
# for i in _class:
#      print(i[0])
# db.deleteClass(4)
# _class=addClass(Mat,2)
    