import random
import math


QUESTION = 'Answer \"yes\" if given number is prime. Otherwise answer \"no\".'


def is_prime(number):
    '''
    Принимает число number, возвращает True, если число четное и
    False, если число нечетное
    '''
    if number <= 1:
        return False
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True


def game_choice():
    '''
    Возвращает правильный ответ и вопрос задачи
    '''
    number = random.randint(0, 100)
    return 'yes' if is_prime(number) else 'no', number
