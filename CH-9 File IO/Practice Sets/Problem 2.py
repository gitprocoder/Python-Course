import random

def game():
    print("You Are Playing The Game...")
    Score=random.randint(1,100)
    #Fetch The High Score
    with open("Problem 2.txt") as f:
        Hiscore=f.read()
        if(Hiscore!=""):
            Hiscore=int(Hiscore)

        else:
            Hiscore=0

    print(f"Your Score Is {Score}")

    if(Score>Hiscore):
        with open("Problem 2.txt","w") as f:
            f.write(str(Score))

    return Score



game()