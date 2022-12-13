import random
def play():
    print(">>>Welcome to Rock, Paper, Scissors<<<\n")
    print(">>>>>Down below is the game<<<<<\n")
    print("What is your choice?")
    user = input ("'R' for rock, 'P' for paper, 'S' for scissors\n")
    computer = random.choice(['R', 'P', 'S'])
    print(computer)

    if user == computer:
        return 'You have Tied with the Computer'

    if Winning(user, computer):
        return 'You won against the Computer'

    return 'You lost against the Computer'

def Winning(player, opponent):
    if (player == 'R' and opponent == 'S') or (player == 'p' and opponent == 'r') \
        or (player == 'S' and opponent == 'P'):
        return True

print(play())
print("Thank you for playing")




