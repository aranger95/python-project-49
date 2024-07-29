#!/usr/bin/env python3
from brain_games.games.game_calc import calc_game
from brain_games import core


QUESTION = 'What is the result of the expression?'


def main():
    core.engine(calc_game, QUESTION)


if __name__ == '__main__':
    main()
