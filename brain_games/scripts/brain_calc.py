#!/usr/bin/env python3
from brain_games.games.game_calc import game_choice
from brain_games import core


QUESTION = 'What is the result of the expression?'


def main():
    print(QUESTION)
    core.engine(game_choice)


if __name__ == '__main__':
    main()
