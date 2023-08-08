import random
def play():
    choices=('Rock', 'Paper', 'Scissors')
    user_choice = input(choices)
    computer_choice = random.choice(choices)
    is_win = (user_choice == 'Rock' and computer_choice == 'Scissors') or (user_choice == 'Paper' and computer_choice == 'Rock') or (user_choice == 'Scissors' and computer_choice == 'Paper')
    is_loss = (computer_choice == 'Paper' and user_choice == 'Rock') or (computer_choice == 'Rock' and user_choice == 'Scissors') or (computer_choice == 'Scissors' and user_choice == 'Rock')
    tie = (user_choice == 'Rock' and computer_choice == 'Rock') or (user_choice == 'Paper' and computer_choice == 'Paper') or (user_choice == 'Scissors' and computer_choice == 'Scissors') 
    print(f"You chose {user_choice}, Computer chose {computer_choice}")
    if is_win:
        print("You won!") 
    elif is_loss:
        print("You lost! Better luck next time!")
    elif tie:
        print("That's a tie!")    
def script():
    restart = input("Play again?")
    while True:
        if restart == "Yes" or restart == "yes":
            play()
            script()
            continue
        else:
            print("Thanks for playing!")        
play()
script()