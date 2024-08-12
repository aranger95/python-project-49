import random
import math


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    '''
    Accepts a number, returns True if the number is even and
    False if the number is odd.
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
    Returns the correct answer and the question of the task.
    '''
    number = random.randint(0, 100)
    return 'yes' if is_prime(number) else 'no', number
