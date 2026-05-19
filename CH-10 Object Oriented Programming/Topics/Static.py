class Employee:
    Name="" 
    Language="Python"
    Salary=100000
    def info(Self): #We can put function in class.When we put self or any other var. and put that variable before variable it will not make any positional arguements.
        print(f"The Salary Is {Self.Salary} And Language Is {Self.Language}")

    @staticmethod #We Write It To Mark That Greet Function Doesnt Take Any "Self" Method it is ALso Called Decorator
    def Greet():
        print("Good Morning")

Emp=Employee()
Emp.Name="Apple"
Emp.Language="Java"
Emp.Greet() 
Emp.info()