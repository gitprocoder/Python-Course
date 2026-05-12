n=int(input("Enter The Number:"))

Product=1

for i in range(1,n+1):
    Product*=i

print(f"The Factorial Of Number {n} is {Product}")