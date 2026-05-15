import random

Comp= random.choice([1,2,3])
You= input("Enter Your Choice:")

Dic={
    "Rock"    :   1,
    "Paper"   :   2,
    "Scissor" :   3
}
CompDic={
    1    :   "Rock",
    2   :   "Paper",
    3 : "Scissor"  
}
Y=Dic[You]
X=CompDic[Comp]
Z=CompDic[Y]
print(f"You Choose:{Z}\nComputer Choose:{X}")

if(Comp==1 and Y==1):
    print("Draw!")

elif(Comp==1 and Y==2):
    print("You Won!")
elif(Comp==1 and Y==3):
    print("Comp Won!")
elif(Comp==2 and Y==1):
    print("Comp Won!")
elif(Comp==2 and Y==2):
    print("Draw!")
elif(Comp==2 and Y==3):
    print("You Won!")
elif(Comp==3 and Y==1):
    print("You Won!")
elif(Comp==3 and Y==2):
    print("Comp Won!")
elif(Comp==3 and Y==3):
    print("Draw!")

else:
    print("Something Went Wrong!")