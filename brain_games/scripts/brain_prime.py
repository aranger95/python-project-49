#!/usr/bin/env python3
from brain_games.games import prime
from brain_games.core import engine


def main():
    '''Запускает модуль игры \"Простое ли число?\" '''
    engine(prime)


if __name__ == '__main__':
    main()
