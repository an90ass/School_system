class ClassLesson:
    def __init__(self,id,class_id,teacher_id,lesson_id):
            if id is None:
                  self.id = 0
            else:
                  self.id = id

            self.class_id = class_id
            self.teacher_id = teacher_id
            self.lesson_id = lesson_id

            


        