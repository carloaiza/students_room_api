from model.student import Student

class StudentService():

    def __init__(self):
        self.students=[]

    def getAllStudents(self):
        self.students.append(Student("1222223",
            "Carlos Loaiza",20000,"M",True,"3016052808"))

        self.students.append(Student("34434343",
                                     "Pedro Pérez",
                                     230000, "M", True, "44343434343"))
        return self.students