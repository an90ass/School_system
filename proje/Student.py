class Student:
    def __init__(self,id,student_number,student_name,student_surname,student_birthday,student_gender,classid):
            if id is None:
                  self.id = 0
            else:
                  self.id = id

            self.student_number = student_number

            if len(student_name)>45:
                  raise Exception("Name icin maksimum 45 karakter girmelisiniz")
            self.student_name = student_name

            self.student_surname = student_surname
            self.student_birthday = student_birthday
            self.student_gender = student_gender
            self.classid = classid
        
    @staticmethod
    def CreatStudent(obj):#dbManager gelen obj
          list = []

          if isinstance(obj,tuple):
                list.append(Student(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5], obj[6]))
          else:
                for i in obj: #birden fazla student gelse
                    list.append(Student(i[0], i[1], i[2], i[3], i[4], i[5], i[6]))
          return list
                      
          

        