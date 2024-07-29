import random


RIGHT_ANSWERS = ('yes', 'no')


def even_game():
    number = random.randint(1, 100)
    is_even = number % 2 == 0
    correct_answer = 'yes' if is_even else 'no'
    return number, correct_answer
