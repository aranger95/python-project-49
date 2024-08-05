import random


QUESTION = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False


def game_choice():
    number = random.randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    # print(correct_answer)
    return correct_answer, number