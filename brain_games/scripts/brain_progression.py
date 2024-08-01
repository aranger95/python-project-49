#!/usr/bin/env python3
from brain_games.games.game_progression import game_choice
from brain_games import core


QUESTION = 'What number is missing in the progression?'


def main():
    print(QUESTION)
    core.engine(game_choice)


if __name__ == '__main__':
    main()
