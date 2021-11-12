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

player1_wins = 0
player2_wins = 0
winning_score = 4

while player1_wins < winning_score and player2_wins < winning_score:
    print(f"player 1 : {player1_wins} and player 2 : {player2_wins}")
    Player_1 = input("player_1 , Make your move : ").lower()
    print(f"player_2 , Make your move : {computerMove}")
    Player_2 = computerMove
