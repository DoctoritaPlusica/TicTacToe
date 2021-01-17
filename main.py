#Rock paper scissors game

import random

# Rules : rock>scissors , scissors>paper , paper>rock

def is_win(player,opponent):
    #return true if player wins
    if (player=='r' and opponent=='s') or(player=='s' and opponent=='p' ) or (player=='p' and opponent=='r'):
        return True

#How do you play
def play ():
    user = input("Chose betweem  'r' for rock , 'p' for paper and 's' for scissors : ")
    computer = random.choice(['r','p','s'])
    if computer=='r':
        print("Computer chose rock")
    if computer=='p':
        print("Computer chose paper")
    if computer == 's':
        print("Computer chose scissors")

    if user ==computer:
        return 'tie'
    if is_win(user,computer):
        return "You won"
    return"You lost"
print(play())

