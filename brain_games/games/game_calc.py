import random


OPERATIONS = ['+', '-', '*']


def calculate(operation: str, num_1: int, num_2: int):
    if operation == '+':
        return num_1 + num_2
    elif operation == '-':
        return num_1 - num_2
    elif operation == '*':
        return num_1 * num_2


def game_choice():
    num_1 = random.randint(1, 25)
    num_2 = random.randint(1, 25)
    operator = random.choice(OPERATIONS)
    calculate(operator, num_1, num_2)
    expression = f'{num_1} {operator} {num_2}'
    correct_answer = calculate(operator, num_1, num_2)
    return expression, correct_answer
