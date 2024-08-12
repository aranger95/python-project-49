import random


OPERATIONS = ['+', '-', '*']
QUESTION = 'What is the result of the expression?'


def calculate(operation: str, num_1: int, num_2: int):
    '''
    Accepts the numbers num_1 and num_2 and a mathematical operator,
    returns the result of addition, subtraction or multiplication.
    '''
    if operation == '+':
        return num_1 + num_2
    elif operation == '-':
        return num_1 - num_2
    elif operation == '*':
        return num_1 * num_2


def game_choice():
    '''
    Returns the correct answer and the question of the task.
    '''
    num_1 = random.randint(1, 25)
    num_2 = random.randint(1, 25)
    operator = random.choice(OPERATIONS)
    expression = f'{num_1} {operator} {num_2}'
    correct_answer = calculate(operator, num_1, num_2)
    return correct_answer, expression
