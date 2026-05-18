with open("Problem 7.txt") as f:
    Lines=f.readlines()

lineno=1
for line in Lines:
    if("Python" in line):
        print(f"Python is in {lineno} line ")
        break
    lineno+=1
else:
    print("Python Is Not Present In Any Line")


    