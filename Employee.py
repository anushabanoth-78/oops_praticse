class Employee_Management_System:
    def __init__(self,Employee_name,Employee_ID,Salary):
        self.Employee_name=Employee_name
        self.Employee_ID=Employee_ID
        self.Salary=Salary
    def display(self):
         print(self.Employee_name)
         print(self.Employee_ID)
         print(self.Salary)
    def increase_salary():
        
        self.Salary +=1000
    def   check_salary(self):
        if self.Salary>=5000:
            print("Eligible for the promotion")
        else:
            print("Not Eligible for the promotion")
employee1=Employee_Management_System("Anusha",101,40000)         
employee1.check_salary()