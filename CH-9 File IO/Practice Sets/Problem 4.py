word="Donkey"
with open("Problem 4.txt","r") as f:
    Content=f.read()
    NewContent=Content.replace(word,"######")


with open("Problem 4.txt","w") as f:
    f.write(NewContent)