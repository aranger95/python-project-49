import prompt, random
import cli


print('Answer \"yes\" if the number is even, otherwise answer \"n\"')

def game_even():
    score = 0
    RIGHT_ANSWERS = ('yes', 'no')
    while score != 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        answer = prompt.string('Your answer: ')
        if answer not in RIGHT_ANSWERS:
            defeat()
            break
        if number % 2 == 0:
            if answer == 'yes':
                print('Correct!')
                score += 1    
            else:
                print('\"no\" is wrong answer ;(. Correct answer was \"yes\"')
                defeat()
                break
        elif answer == 'no':
            print('Correct!')
            score += 1    
        else:
            print('\"yes\" is wrong answer ;(. Correct answer was \"no\"')
            defeat()
            break
    if score == 3:
        winning()

def winning():
    print(f'Congratulations, {cli.name}!')

def defeat():
    print(f'Let\'s try again, {cli.name}!')
