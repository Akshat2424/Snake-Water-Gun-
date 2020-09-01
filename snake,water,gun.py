import random
n=11
for i in range(n):
    list=["snake","water","gun"]
    turn=int(input("enter your choice 1 for snake 2 for water 3 for gun"))

    choice=random.choice(list)
    if(turn==1 and choice==list[1]):
        print("you win")
    elif (turn == 2 and choice == list[2]):
        print("you win")
    elif (turn == 3 and choice == list[0]):
        print("you win")
    elif (turn == 1 and choice == list[2]):
        print("you lose")
    elif (turn == 2 and choice == list[0]):
        print("you lose")
    elif (turn == 3 and choice == list[1]):
        print("you lose")
    elif (turn == 1 and choice == list[0]):
        print("tie")
    elif (turn == 2 and choice == list[1]):
        print("tie")
    elif (turn == 3 and choice == list[2]):
        print("tie")









