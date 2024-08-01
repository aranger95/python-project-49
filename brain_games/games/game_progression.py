import random


MIN_LENGTH = 5
MAX_LENGTH = 10
MIN_STEP = 1
MAX_STEP = 4


def generate():
    num_1 = random.randint(0, 100)
    num_2 = random.randint(1, 10)
    index = random.randint(MIN_STEP, MAX_STEP)
    quantity = random.randint(MIN_LENGTH, MAX_LENGTH)
    prog_list = []
    for i in range(quantity):
        prog_list.append(num_1 + i * num_2)
    correct_answer = str(prog_list[index])
    return correct_answer, prog_list, index


def game_choice():
    correct_answer, prog_list, index = generate()
    prog_list[index] = '..'
    prog_str = " ".join(map(str, prog_list))
    print(correct_answer)
    return correct_answer, prog_str
