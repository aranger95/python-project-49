#!/usr/bin/env python3
from brain_games.games.game_progression import progression_game
from brain_games import core


QUESTION = 'What number is missing in the progression?'


def main():
    core.engine(progression_game, QUESTION)


if __name__ == '__main__':
    main()
