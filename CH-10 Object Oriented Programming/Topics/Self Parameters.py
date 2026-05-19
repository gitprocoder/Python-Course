class Employee:
    Name="" 
    Language="Python"
    Salary=100000
    def info(Self): #We can put function in class.When we put self or any other var. and put that variable before variable it will not make any positional arguements.
        print(f"The Salary Is {Self.Salary} And Language Is {Self.Language}")

Emp=Employee()
Emp.Name="Apple"
Emp.Language="Java" 
Emp.info()
'''Employee.getinfo(Emp)''' #When We Dont Put self or Any variable in function it will convert like it.Here clearly the "Emp" becomes a positional Arguement.