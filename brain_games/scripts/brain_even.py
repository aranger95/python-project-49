import random, cli, prompt


def game():
    print('Answer \"yes\" if the number is even, otherwise answer \"n\"')
    score = 0
    RIGHT_ANSWERS = ('yes', 'no')
    while score != 3:
        number = random.randint(1, 100)
        is_even = number % 2 == 0
        correct_answer = 'yes' if is_even else 'no'
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer not in RIGHT_ANSWERS:
            defeat()
            break
        if answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            defeat()
            break
            
    if score == 3:
        winning()

def winning():
    print(f'Congratulations, {cli.nickname}!')

def defeat():
    print(f'Let\'s try again, {cli.nickname}!')