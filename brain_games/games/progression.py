import random


MIN_LENGTH = 5
MAX_LENGTH = 10
QUESTION = 'What number is missing in the progression?'


def generate_progression():
    '''
    Возвращает сгенерированную прогрессию prog_list с длиной quantity
    '''
    num_1 = random.randint(0, 100)
    num_2 = random.randint(1, 10)
    quantity = random.randint(MIN_LENGTH, MAX_LENGTH)
    prog_list = []
    for i in range(quantity):
        prog_list.append(num_1 + i * num_2)
    return prog_list, quantity


def game_choice():
    '''
    Возвращает правильный ответ и вопрос задачи
    '''
    prog_list, quantity = generate_progression()
    index = random.randint(0, quantity - 1)
    correct_answer = prog_list[index]
    prog_list[index] = '..'
    prog_str = " ".join(map(str, prog_list))
    # print(correct_answer)
    return correct_answer, prog_str
