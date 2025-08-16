import random
def game():
    print("you are playing the game: ")

    score = random.randint(1, 100)

    with open("file_prblm1.txt", "r") as f:
        hi_score = f.read()
        if(hi_score!=""):
            hi_score = int(hi_score)
        else:
            hi_score = 0
    
    print(f"Your Score is {score}")
    
    if(score >= hi_score):
        with open("file_prblm1.txt", "w") as f:
            f.write(str(score))
    
    return score

game()
        


