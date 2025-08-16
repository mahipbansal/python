"""
snake = 1
water = -1
gun = 0

"""
import random
computer = random.choice([-1, 1, 0])
user = input("user choice : ")

game= {"s" : 1, "w" : -1, "g" : 0}
reverse_game= {1: "Snake", -1 : "water", 0: "gun"}
choice_user = game[user]
print(f"You chose : {reverse_game[choice_user]}\nComputer chose : {reverse_game[computer]} ")
if(computer == choice_user):
    print("draw")
else:
    if(computer == 1 and choice_user == 0):
        print("Congrats!, You win")
    elif(computer == 1 and choice_user == -1):
        print("Sorry, You lose")
    elif(computer == -1 and choice_user == 1):
        print("Congrats!, You win")
    elif(computer == -1 and choice_user == 0):
        print("Sorry, You lose")
    elif(computer == 0 and choice_user == -1):
        print("Congrats!, You win")
    elif(computer == 0 and choice_user == 1):
        print("Sorry, You lose")
    else:
        print("wrong input")

print("thanks for playing hope you like it")