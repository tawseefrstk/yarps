import random

# username = input('What is your name? ')
# Get user's name

player_wins = 0
bot_wins = 0
ties = 0

while True:
    rounds = int(input('How many rounds do you want to play? (from 3 to 10) '))
    if rounds >=3 and rounds <= 10:
        # Verify the amount of rounds
        break;
    else:
        print('Try again.')
        # Prompt the user to try again.

# Game starts here.

print('''R = Rock
P = Paper
S = Scissors
Capitalisation doesn't matter.
''')
# Print rules.

potential_answers = ['r', 'p', 's']
# Potential answers.

victory_states = [['r', 's'], ['s', 'p'], ['p', 'r']]
# The states in which someone wins.

for i in range(rounds):
    bot_play = potential_answers[random.randint(0, 2)]
    # Get a random move for the bot.

    # print(bot_play)
    # Debugging, to see if victory states work.

    human_play = input('Rock, paper, or scissors? ')
    # Get input from the human.
    if human_play.lower() not in potential_answers:
        # Making sure input is valid
        print('That\'s not valid. Game invalidated.')
    elif [bot_play, human_play.lower()] in victory_states:
        # Checking to see if the bot beats the human
        print('The bot won the game.')
        bot_wins += 1
    elif [human_play.lower(), bot_play] in victory_states:
        # Checking to see if the human beat the bot
        print('You won.')
        player_wins += 1
    elif human_play.lower() == bot_play:
        print('It was a tie.')
        ties += 1
    else:
        print('Invalid state.')

print('You played ' + str(rounds) + ' rounds.')
print('You won ' + str(player_wins) + ' rounds.')
print('You lost ' + str(bot_wins) + ' rounds.')
print('You tied ' + str(ties) + ' rounds.')
