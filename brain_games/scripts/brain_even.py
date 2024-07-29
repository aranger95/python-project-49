#!/usr/bin/env python3
from brain_games.games.game_even import even_game
from brain_games import core


QUESTION = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def main():
    core.engine(even_game, QUESTION)


if __name__ == '__main__':
    main()
