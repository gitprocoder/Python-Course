with open ("Problem 6.txt") as f:
    Content=f.read()
    if("Python" in Content):
        print("Python word is in Log File")

    else:
        print("Python Is Not Present")