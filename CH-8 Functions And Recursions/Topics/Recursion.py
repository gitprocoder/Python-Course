#Sometime The Function Call Itself To Do Some Tasks It Is Called Recursion . It Is Usefull In Factorial and Other Tasks.
"""
factorial of 1=1
factorial of 2=1x2
factorial of 3=1x2x3
factorial of 4=1x2x3x4
factorial of 5=1x2x3x4x5
"""
def Factorial(n):
    if(n==0 or n==1):
        return(1)
    
    return(n*Factorial(n-1))
    
n=int(input("Enter Number:"))
print(f"Factorial Is: {Factorial(n)} ")
