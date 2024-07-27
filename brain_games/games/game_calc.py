import random, prompt
from brain_games.cli import welcome_user

def calc():
    nickname = welcome_user()
    print('What is the result of the expression?')
    score = 0
    while score != 3:
        num_1 = random.randint(1, 25)
        num_2 = random.randint(1, 25)
        operations = ['+', '-', '*']
        operation = random.choice(operations)

        if operation == '+':
            result = num_1 + num_2
        elif operation == '-':
            result = num_1 - num_2
        elif operation == '*':
            result = num_1 * num_2    

        print(f'Question: {num_1} {operation} {num_2}')
        answer = prompt.integer('Your answer: ')

        if answer == result:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{result}".')
            print(f'Let\'s try again, {nickname}!')
            break
            
    if score == 3:
        print(f'Congratulations, {nickname}!')
