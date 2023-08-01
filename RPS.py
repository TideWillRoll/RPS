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
def script():
    restart = input("Play again?")
    if restart == "yes" or restart == "y" or restart == True:
        print(play())
        print(script())
    if restart == "no" or restart == "n" or restart == False:
        print("Thanks for playing!")
print(play())
print(script())