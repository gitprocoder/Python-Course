words=["Donkey","Ganda","Baga"]
with open("Problem 5.txt","r") as f:
    Content=f.read()
    
    for word in words:
        Content=Content.replace(word,"#"*len(word))



with open("Problem 5.txt","w") as f:
    f.write(Content)