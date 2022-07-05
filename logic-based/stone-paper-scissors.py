import random

def sps():

    print("You won't get to chose because the other can see. We will chose for you.")
    user_one = random.randint(1, 3)
    user_two = random.randint(1, 3)

    storage = {1: "Stone", 2: "Paper", 3:"Scissors"}

    print("User 1 got: ", storage[user_one])
    print("User 2 got: ", storage[user_two])


sps()
     