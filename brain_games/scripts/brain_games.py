#!/usr/bin/env python3
from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import even
from brain_games.scripts.brain_calc import calc
from brain_games.scripts.brain_gcd import gcd
from brain_games.scripts.brain_progression import progression
from brain_games.scripts.brain_prime import prime


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    # even()
    # calc()
    # gcd()
    # progression()
    # prime()

if __name__ == '__main__':
    main()
