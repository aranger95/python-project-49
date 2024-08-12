from random import randint


QUESTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    '''
    Performs a number check for parity.
    '''
    return number % 2 == 0


def game_choice():
    '''
    Returns the correct answer and the question of the task.
    '''
    number = randint(1, 100)
    correct_answer = 'yes' if is_even(number) else 'no'
    return correct_answer, number
