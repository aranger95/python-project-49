#!/usr/bin/env python3
from brain_games.games import gcd
from brain_games.core import engine


def main():
    '''Launches the "Greatest Common Divisor" game module.'''
    engine(gcd)


if __name__ == '__main__':
    main()
