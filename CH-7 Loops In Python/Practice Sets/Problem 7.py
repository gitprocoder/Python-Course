# N=3 means 3 rows
"""
  *
 ***
*****

"""

n=int(input("Enter Number Of Rows:"))
for i in range(1,n+1):
    print(" " * (n-i),end="")
    print("*" * (2*i-1),end="")
    print("")