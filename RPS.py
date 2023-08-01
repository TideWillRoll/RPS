import random
def play():
    options=['Rock', 'Paper', 'Scissors']
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'You tied!'
    if is_win(user, computer) == True:
        return 'Congrats! You Won!'
    else:
        return "You lost! Better luck next time!"
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
print(play())
print(script())