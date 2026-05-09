English=int(input("Enter English Marks:"))
Maths=int(input("Enter Maths Marks:"))
Science=int(input("Enter Science Marks:"))

Total_Percentage=(100)*(English+Maths+Science)/300
if (Total_Percentage>=40):
    print("You Are Passed!")

else:
    print("You Are Failed!")