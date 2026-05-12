A=int(input("Enter The Number:"))

for i in range (2,A):
    if(A%2)==0:
        print("Number Is Composite (Not Prime)")
        break

else:
    print("Number Is Prime")