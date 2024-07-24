import random, prompt, games.game_exodus


def progression():
    print('What number is missing in the progression?')
    score = 0
    while score != 3:
        num_1 = random.randint(0, 100)
        num_2 = random.randint(1, 10)
        index = random.randint(0, 5)
        quantity = random.randint(5, 10)
        prog_list = []
        for i in range(quantity):
            prog_list.append(num_1 + i * num_2)
        correct_answer = str(prog_list[index])
        prog_list[index] = '..'
        print(f'Question: {" ".join(map(str, prog_list))}')
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            games.game_exodus.defeat()
            break
        elif answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            games.game_exodus.defeat()
            break
            
    if score == 3:
        games.game_exodus.winning()

