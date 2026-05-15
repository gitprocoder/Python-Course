def Table(A):
    B=0
    while (B<11):
        print(f"{A} X {B} = {A*B}")
        B+=1

A=int(input("Enter The Number:"))
Table(A)