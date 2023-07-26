import random
def play():
    options=['Rock', 'Paper', 'Scissors']
    user = input("What's your choice? 'r' for rock, 'p' for paper, 's' for scissors\n")
    computer = random.choice(['r', 'p', 's'])
    if user == computer:
        return 'It\'s a tie!'
    if is_win(user, computer):
        return 'You won'
    else:
        return("You lost! Better luck next time!")
def is_win(player, opponent):
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or (player == 'p' and opponent == 'r'):
        return True
def script():
    restart = input("Would you like play again?")
    if restart == "yes" or restart == "y":
        play()
    if restart == "no" or restart == "n":
        print("Thanks for playing!")
print(play())
script()