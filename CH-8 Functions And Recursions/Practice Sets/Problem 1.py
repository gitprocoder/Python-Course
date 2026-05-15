def Greatest (a,b,c):
    if (a>b and a>c):
        return("A is Greater")
        
    if (b>a and b>c):
        return("B is Greater")
        
    if (c>b and c>a):
        return("C is Greater")
    
a=int(input("Enter Number:"))
b=int(input("Enter Number:"))
c=int(input("Enter Number:"))

print(Greatest(a,b,c))