
# The most general class


class person():
    def __init__(self,birthDate = "Unknown",adress = "Unknown"):
        self.birthDate = birthDate
        # birthday is defined as a list or touple. [x,y,z] = [day,month,year]
        self.adress = adress
# Inherit class
class student(person) :
    def __init__(self,name = "Unknown",id = "Unknown",GPA = "Unknown", birthDate = "Unknown",adress = "Unknown"):
        super().__init__(birthDate,adress) 
        self.name = name 
        self.id = id
        self.GPA = GPA
    def show_student_info (self):
        print("""
        
        Name : {}

        ID : {}

        GPA : {}

        BirthDate = {}

        Adress = {}
        
        """.format(self.name,self.id,self.GPA,self.birthDate,self.adress))



person1 = person([1,2,3],"asd")
print(person1.adress)
print(person1.birthDate)
fatih = student("Fatih",150416028,2.70,[8,5,1998],"kucukyali")
fatih.show_student_info()
print("asdasdsd")

all_students = []

class course():
    def __init__ (self,name = "Unknown",students = "Unknown",capacity = "Unknown",numberOfStudent = "Unknown"):
        self.name = name
        self.students = students
        self.capacity = capacity
        self.numberOfStudents = numberOfStudent
    
    def get_numberOfStudents(self):
        print("This course has {} students".format(self.numberOfStudents))

    def get_nameOfCourse(self):
        print("The name of course is {}".format(self.name))
    
    def get_students(self):
        print("Student List;")
        for i in self.students:
            a = 0
            print("Student {} : {}".format(a,i))
            a = a + 1
    
    def add_student(self,new_student):
        self.students.append(new_student)
        # How to be sure new_student is a 'student' object ?
    
    def delete_student(self):
        # deleting specific student should be her/his id, rigth?
        pass

        




