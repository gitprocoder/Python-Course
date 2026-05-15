def Pattern (n):
    if (n==0):
        return
    print("*"*n)
    Pattern(n-1)


A=int(input("Enter The Number:"))
Pattern(A)