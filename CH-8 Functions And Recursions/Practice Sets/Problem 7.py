def Remove (l,word):
    n=[]
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n
        

l=["Apple","Maple", "Able"]

print(Remove(l,"le"))