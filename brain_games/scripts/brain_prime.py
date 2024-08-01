#!/usr/bin/env python3
from brain_games.games.game_prime import game_choice
from brain_games import core


QUESTION = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def main():
    print(QUESTION)
    core.engine(game_choice)


if __name__ == '__main__':
    main()
