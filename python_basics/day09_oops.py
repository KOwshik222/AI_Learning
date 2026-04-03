class Student:#create blue print
    def __init__(self,name,age,marks):#_is a function that runs by itself when you make a new object, to put data inside it.
        self.name = name
        self.age = age
        self.marks = marks
student1 = Student("a",12,[20,25,30])
student2 = Student("b",12,[20,25,30])
print(student1.age)

print("-------------------------------METHODS(ACTION)-------------------------------------------------------")

class Marks:
    def __init__(self,name,age,marks):
        self.name = name
        self.age = age
        self.marks = marks
    
    def average_marks(self):
        total_marks = sum(self.marks)
        count = len(self.marks)
        return total_marks/count
    def display(self):
        print(f"name:{self.name}")
        print(f"age:{self.age}")
        print(f"average:{self.average_marks()}")
student1 = Marks("a",12,[10,20,30])
student1.display()

print("------------------------------------PRACTICE-------------------------------------------")


class Student:
    def __init__(self,name,marks):
        self.name= name
        self.marks = marks

    def total_marks(self):
        total = sum(self.marks)
        return total
    def display(self):
        print(f"name:{self.name}")
        print(f"marks:{self.total_marks()}")
student = Student("a",[10,20,30])
student.display()

print("---------------------2ndquestion------------------------------")
class Rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        area = self.length * self.breadth
        return area
    def display(self):
        print(f"area is :{self.area()}")
rect = Rectangle(2,3)
rect.display()



