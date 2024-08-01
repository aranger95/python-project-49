import random
import math


def game_choice():
    num_1 = random.randint(1, 100)
    num_2 = random.randint(1, 100)
    correct_answer = math.gcd(num_1, num_2)
    expression = f'{num_1} {num_2}'
    return correct_answer, expression
