import random
import math


def is_prime(number):
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True


def prime_game():
    number = random.randint(0, 100)
    flag = is_prime(number)
    if flag is True:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return number, correct_answer
