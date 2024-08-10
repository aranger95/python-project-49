#!/usr/bin/env python3
from brain_games.games import even
from brain_games import core


def main():
    '''Запускает модуль игры \"Проверка на четность\" '''
    core.engine(even)


if __name__ == '__main__':
    main()
