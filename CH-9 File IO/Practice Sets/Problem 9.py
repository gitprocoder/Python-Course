with open("Problem 9.txt") as f:
    Content1=f.read()

with open("Problem 9.2.txt") as f:
    Content2=f.read()

if(Content1==Content2):
    print("Both Files Have Same Content")

else:
    print("Both Files Have Diffrent Content")