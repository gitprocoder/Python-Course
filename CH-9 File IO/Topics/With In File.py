A=open("Test.txt")
print(A.read())
A.close()

#The Same Task Can Be Done By This.
with open("Test.txt") as F:
    print(F.read())

#Here We Dont Need To Close The Function It Will Automatically Close It.