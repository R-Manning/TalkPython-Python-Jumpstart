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
        print('You guessed the number {0} correctly!'.format(guess))
        print('\nIt took you {0} turns.'.format(num_of_guesses))
    elif guess < rand_num:
        print('The number is greater than your guess of {0}.'.format(guess))
    else:
        print('The number is less than your guess of {0}.'.format(guess))
