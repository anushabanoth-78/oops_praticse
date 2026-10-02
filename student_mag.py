class Student_Management_System:
    def __init__(self,name,roll_number,marks):
        self.name=name
        self.roll_number=roll_number
        self.marks=marks
    def display(self):
        print("name:",self.name)
        print("roll number:",self.roll_number)
        print("marks:",self.marks)
    def Add_marks(self,marks):
        self.marks +=marks
    
    def result(self):

       if self.marks>=40:
        print("pass")
       else:
        print("fail")
data1=Student_Management_System("Anusha",101,35)

data2=Student_Management_System("Rahul",102,75)

data1.result()
data2.result()
data1.Add_marks(10)
data2.Add_marks(5)
data1.result()
data2.result()



