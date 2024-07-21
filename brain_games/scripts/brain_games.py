#!/usr/bin/env python3
from cli import welcome_user
from scripts.brain_even import game
from scripts.brain_calc import calc


def main():
    print('Welcome to the Brain Games!')
    welcome_user()
    # game()
    calc()


if __name__ == '__main__':
    main()
