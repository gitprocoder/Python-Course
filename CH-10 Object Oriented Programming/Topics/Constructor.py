class Employee:
    Name="" 
    Language="Python"
    Salary=100000
    def __init__(self,Name,Language,Salary): #It Is Called Constructor OR Dunder IT Doesnt Require To Call TO Run It Will Run Automatically
        print("I m WORKER!") 
        self.Name=Name
        self.Salary=Salary
        self.Language=Language
    def info(Self):
        print(f"The Salary Is {Self.Salary} And Language Is {Self.Language} And Name Of Worker Is {Self.Name}")

Emp=Employee("Apple","Java",2090) 
Emp.info()