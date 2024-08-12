import random


MIN_LENGTH = 5
MAX_LENGTH = 10
QUESTION = 'What number is missing in the progression?'


def generate_progression():
    '''
    Returns a generated progression of a certain length.
    '''
    num_1 = random.randint(0, 100)
    num_2 = random.randint(1, 10)
    quantity = random.randint(MIN_LENGTH, MAX_LENGTH)
    prog_list = []
    for i in range(quantity):
        prog_list.append(num_1 + i * num_2)
    return prog_list


def game_choice():
    '''
    Returns the correct answer and the question of the task.
    '''
    prog_list = generate_progression()
    index = random.randint(0, len(prog_list) - 1)
    correct_answer = prog_list[index]
    prog_list[index] = '..'
    prog_str = " ".join(map(str, prog_list))
    return correct_answer, prog_str
