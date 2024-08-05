import random


MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 4
QUESTION = 'What number is missing in the progression?'


def generate_progression():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(1, 10)
    quantity = random.randint(MIN_LENGTH, MAX_LENGTH)
    prog_list = []
    for i in range(quantity):
        prog_list.append(num_1 + i * num_2)
    return prog_list


def game_choice():
    index = random.randint(MIN_STEP, MAX_STEP)
    prog_list = generate_progression()
    correct_answer = str(prog_list[index])
    prog_list[index] = '..'
    prog_str = " ".join(map(str, prog_list))
    # print(correct_answer)
    return correct_answer, prog_str
