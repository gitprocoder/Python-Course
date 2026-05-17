A=open("Problem 1.txt")
B=A.read()
if("Twinkle" in B):
    print("The Word Is Present.")

else:
    print("The Word Is Not Present.")

C=B.find("Twinkle")
print(f"The Word Is Located At {C+1}st Position In File.")

A.close()