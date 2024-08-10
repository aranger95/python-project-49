from random import randint


QUESTION = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def game_choice():
    '''
    Возвращает правильный ответ и вопрос задачи
    '''
    number = randint(1, 100)
    correct_answer = 'yes' if number % 2 == 0 else 'no'
    return correct_answer, number
