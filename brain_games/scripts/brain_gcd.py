#!/usr/bin/env python3
from brain_games.games.game_gcd import gcd_game
from brain_games import core


QUESTION = 'Find the greatest common divisor of given numbers.'


def main():
    core.engine(gcd_game, QUESTION)


if __name__ == '__main__':
    main()
