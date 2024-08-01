import random
import math


def is_prime(number):
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True


def game_choice():
    number = random.randint(0, 100)
    correct_answer = 'yes' if is_prime(number) else 'no'
    return correct_answer, number
