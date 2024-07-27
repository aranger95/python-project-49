import random, prompt, math
from brain_games.cli import welcome_user


def is_prime(number):
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True


def prime_game():
    nickname = welcome_user()
    print('Answer \"yes\" if given number is prime. Otherwise answer \"no\".')
    score = 0
    while score != 3:
        number = random.randint(0, 100)
        print(f'Question: {number}')
        flag = is_prime(number)
        if flag is True:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        print(correct_answer)
        answer = prompt.string('Your answer: ')
        if answer != correct_answer:
            print(f'Let\'s try again, {nickname}!')
            break
        elif answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            print(f'Let\'s try again, {nickname}!')
            break
            
    if score == 3:
            print(f'Congratulations, {nickname}!')
