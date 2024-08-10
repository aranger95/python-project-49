import random
import math


QUESTION = 'Find the greatest common divisor of given numbers.'


def game_choice():
    '''
    Возвращает правильный ответ и вопрос задачи
    '''
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    correct_answer = math.gcd(num_1, num_2)
    expression = f'{num_1} {num_2}'
    return correct_answer, expression
