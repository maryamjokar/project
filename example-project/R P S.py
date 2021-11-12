import random

print("Rock...".lower())
print("Paper...".lower())
print("Scissors...".lower())
print("------------------")

randomNumber = random.randint(0, 2)
computerMove = "rock"

if randomNumber == 0:
    computerMove = "rock"
elif randomNumber == 1:
    computerMove = "paper"
elif randomNumber == 2:
    computerMove = "scissors"

