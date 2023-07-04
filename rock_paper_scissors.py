import random

def get_choices():
    player_choice = input("Choose one(rock, paper, or scissors): >> ").lower()
    computer_options = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(computer_options)

    choices = {
        'player': player_choice,
        'computer': computer_choice
    }

    return choices

def check_win(player, computer):
    print(f"You chose {player} and computer chose {computer}.")
    if player == computer:
        return "It's a tie."
    elif player == 'rock':
        if computer == 'paper':
            return 'Paper covers rock. Computer wins.'
        elif computer == 'scissors':
            return 'Rock crushes scissors. You win'
    elif player == 'paper':
        if computer == 'rock':
            return 'Paper covers rock. You win.'
        elif computer == 'scissors':
            return 'Scissors cuts paper. Computer wins.'
    elif player == 'scissors':
        if computer == 'paper':
            return 'Scissors cuts paper. You win.'
        elif computer == 'rock':
            return 'Rock crushes scissors. Computer wins.'


choices = get_choices()
result = check_win(choices['player'], choices['computer'])

print(result)