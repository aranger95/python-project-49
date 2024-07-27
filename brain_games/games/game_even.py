import random, prompt
from brain_games.cli import welcome_user


def even_game():
    nickname = welcome_user()
    print('Answer \"yes\" if the number is even, otherwise answer \"no\".')
    score = 0
    RIGHT_ANSWERS = ('yes', 'no')
    while score != 3:
        number = random.randint(1, 100)
        is_even = number % 2 == 0
        correct_answer = 'yes' if is_even else 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer not in RIGHT_ANSWERS:
            print(f'Let\'s try again, {nickname}!')
            break
        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f'Let\'s try again, {nickname}!')
            break
            
    if score == 3:
        print(f'Congratulations, {nickname}!')

