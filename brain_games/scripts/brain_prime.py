#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.core import engine


def main():
    '''Launches the module of the game "Is a prime number?".'''
    engine(prime)


if __name__ == '__main__':
    main()
