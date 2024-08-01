#!/usr/bin/env python3
from brain_games.games.game_gcd import game_choice
from brain_games import core


QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    print(QUESTION)
    core.engine(game_choice)


if __name__ == '__main__':
    main()
