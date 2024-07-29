import random


def conditions(operation, num_1, num_2):
    global correct_answer
    if operation == '+':
        correct_answer = num_1 + num_2
        return correct_answer
    elif operation == '-':
        correct_answer = num_1 - num_2
        return correct_answer
    elif operation == '*':
        correct_answer = num_1 * num_2
        return correct_answer


def calc_game():
    num_1 = random.randint(1, 25)
    num_2 = random.randint(1, 25)
    operations = ['+', '-', '*']
    operation = random.choice(operations)
    conditions(operation, num_1, num_2)
    expression = f'{num_1} {operation} {num_2}'
    return expression, correct_answer
