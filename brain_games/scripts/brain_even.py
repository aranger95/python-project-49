#!/usr/bin/env python3
from brain_games.games.game_even import game_choice
from brain_games import core


QUESTION = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def main():
    print(QUESTION)
    core.engine(game_choice)


if __name__ == '__main__':
    main()
