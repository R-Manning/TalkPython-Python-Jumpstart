import random
import time

from players import Wizard, Creature, Dragon, SmallAnimal


def main():
    print_header()
    game_loop()


def print_header():
    print('----------------------')
    print('     Wizard Game      ')
    print('----------------------')
    print()


def game_loop():

    creatures = [
        SmallAnimal('Toad', 1),
        Creature('Tiger', 12),
        SmallAnimal('Bat', 3),
        Dragon('Dragon', 50, 75, True),
        Wizard('Evil Wizard', 1000)
    ]

    hero = Wizard('Gandolf', 75)
    cmd = ''

    while True:

        active_creature = random.choice(creatures)
        print('A {} of level {} has appeared from a dark and foggy forest...'
              .format(active_creature.name, active_creature.level))
        print()

        cmd = input('Do you [A]ttack, [R]unaway, or [L]ook-around? ').lower()
        if cmd == 'a':
            if hero.attack(active_creature):
                creatures.remove(active_creature)
            else:
                print('The wizard runs and hides taking time to recover...')
                time.sleep(5)
                print('The wizard returns revitalized!')
        elif cmd == 'r':
            print('The wizard has become unsure of his power and flees!')
        elif cmd == 'l':
            print('The wizard {} takes in the surroundings and sees:'.format(hero.name))
            for c in creatures:
                print('* A {} of level {}'.format(c.name, c.level))
        else:
            print('Exiting game...')  # could ask if they're sure they want to exit or something
            break


        if not creatures:
            print("You've defeated all the creatures!")
            break

        print()


if __name__ == '__main__':
    main()
