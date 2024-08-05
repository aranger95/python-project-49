import random


QUESTION = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def is_even(number):
    return number % 2 == 0


def game_choice():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return correct_answer, number
