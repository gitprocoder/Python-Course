A=open("Test.txt")

'''C=A.readlines() #It Will Print All The Lines In list At Same Time. 
print(C)'''

B1=A.readline() #It Will Print Line One By One If We Again Run It With Another Variable It Will Print Another Line. 
print(B1)
B2=A.readline()
print(B2)
B3=A.readline()
print(B3)

A.close()

