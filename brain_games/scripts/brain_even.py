#!/usr/bin/env python3
from brain_games.games import even
from brain_games import core


def main():
    '''Launches the "Parity Check" game module.'''
    core.engine(even)


if __name__ == '__main__':
    main()
