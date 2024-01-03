class Class:
    def __init__(self,id,class_name,teacher_id):
            if id is None:
                  self.id = 0
            else:
                  self.id = id

            self.class_name = class_name#lesson_name
            self.teacher_id = teacher_id

    @staticmethod
    def get_Name_Class(obj):
      list = []

      for row in obj:
            list.append(Class(row[0], row[1], row[2]))

      return list
    
    @classmethod
    def from_tuple(cls, data_tuple):
        return cls(*data_tuple)

    @staticmethod
    def get_classes(data_tuples):
        return [Class.from_tuple(data) for data in data_tuples]








      


        