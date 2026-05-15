def Sum(n):
    if (n==1):
        return(1)
    return Sum (n-1) + n

A=int(input("Enter The Number:"))
print(Sum(A))