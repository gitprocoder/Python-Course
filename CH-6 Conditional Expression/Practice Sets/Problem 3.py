A="Make a lot of money"
B="buy now"
C="subscribe this"
D="click this"

Comment=input("Enter Comment :")

if(A in Comment or B in Comment or C in Comment or D in Comment ):
    print("This Comment is Spam")
else:
    print("This Comment is Not Spam")

