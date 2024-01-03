class Teacher:
    def __init__(self,id,teacher_number,teacher_name,teacher_surname,teacher_birthday,teacher_gender):#branc teacherin gidigi ders
            if id is None:
                  self.id = 0
            else:
                  self.id = id
            self.teacher_number = teacher_number
            # self.branch = branch
            self.teacher_name = teacher_name
            self.teacher_surname = teacher_surname
            self.teacher_birthday = teacher_birthday
            self.teacher_gender = teacher_gender
    @staticmethod
    def CreatTeacher(obj):#dbManager gelen obj
          list = []

          if isinstance(obj,tuple):
                list.append(Teacher(obj[0], obj[1], obj[2], obj[3], obj[4], obj[5]))
          else:
                for i in obj: #birden fazla student gelse
                    list.append(Teacher(i[0], i[1], i[2], i[3], i[4], i[5]))
          return list

        