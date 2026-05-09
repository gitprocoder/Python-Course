A=int(input("Enter Your Marks:"))

if(A<=100 and A>=90):
    Grade="Exc"
if(A<90 and A>=80):
    Grade="A"
if(A<80 and A>=70):
    Grade="B"
if(A<70 and A>=60):
    Grade="C"
if(A<60 and A>=50):
    Grade="D"
if(A<50):
    Grade="E"

print("Your grade is :",Grade)