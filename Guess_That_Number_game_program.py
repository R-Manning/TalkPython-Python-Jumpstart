from random import randint

print('--------------------------------')
print('     Guess That Number Game     ')
print('--------------------------------')

rand_num = randint(0, 100)
guess = -1
num_of_guesses = 0

while rand_num != guess:
    num_of_guesses += 1
    guess = int(input('Guess a number between 0 and 100: '))

    if guess == rand_num:
        print('You guessed the number {} correctly!'.format(guess))
        print('\nIt took you {} turns.'.format(num_of_guesses))
    elif guess < rand_num:
        print('The number is GREATER than your guess of {}.'.format(guess))
    else:
        print('The number is LESS than your guess of {}.'.format(guess))
#TODO: save "high-score", lowest number of guesses to get the correct answer
#program should also load the "high-score" and compare it to the user's score at the end of the game
#TODO: add user-names, save by user-names, add database of usernames, highscores overall/by user
#other add-ons that you can think of
