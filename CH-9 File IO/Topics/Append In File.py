A="Banana Is Good For Health And Body."

B=open("File2.txt","a") #It will Add The String At The End Of Text In File The Number Of Times It Run.
B.write(A)
B.close()

C=open("FileWrite.txt")
D=C.read()
print(D)
C.close()
