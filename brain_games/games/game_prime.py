import random, prompt, brain_games.games.game_exodus, math


def is_prime(number):
    i = 2
    while i <= math.sqrt(number):
        if number % i == 0:
            return False
        i += 1
    return True


def prime():
    print('Answer \"yes\" if the number is prime, otherwise answer \"no\"')
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
            brain_games.games.game_exodus.defeat()
            break
        elif answer == correct_answer:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{correct_answer}".')
            brain_games.games.game_exodus.defeat()
            break
            
    if score == 3:
        games.game_exodus.winning()
