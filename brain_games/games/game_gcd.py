import random, prompt, games.game_exodus, math


def gcd():
    print('Find the greatest common divisor of given numbers.')
    score = 0
    while score != 3:
        num_1 = random.randint(1, 100)
        num_2 = random.randint(1, 100)
        result_gcd = math.gcd(num_1, num_2)
        print(f'Question: {num_1} {num_2}')
        answer = prompt.integer('Your answer: ')

        if answer == result_gcd:
            print('Correct!')
            score += 1
        else:
            print(f'"{answer}" is wrong answer ;(. Correct answer was "{result_gcd}".')
            games.game_exodus.defeat()
            break
            
    if score == 3:
        games.game_exodus.winning()
