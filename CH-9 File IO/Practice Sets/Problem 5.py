words=["Donkey","Bad","Ganda"]
with open("Problem 4.txt","r") as f:
    Content=f.read()
    
    for word in words:
        Contents=Content.replace(word,"#"*len(word))



with open("Problem 4.txt","w") as f:
    f.write(Contents)