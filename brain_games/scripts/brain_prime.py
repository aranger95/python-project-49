#!/usr/bin/env python3
from brain_games.games.game_prime import prime_game
from brain_games import core


QUESTION = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def main():
    core.engine(prime_game, QUESTION)


if __name__ == '__main__':
    main()
