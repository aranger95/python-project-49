import prompt
from brain_games.cli import welcome_user


def engine(game, QUESTION):
    global nickname
    nickname = welcome_user()
    print(QUESTION)
    score = 0
    ROUNDS = 3

    while score < ROUNDS:
        question, correct_answer = game()
        print(f'Question: {question}')
        # print(correct_answer)
        answer = prompt.string('Your answer: ')
        if str(answer) != str(correct_answer):
            defeat()
            break
        elif str(answer) == str(correct_answer):
            print('Correct!')
            score += 1
        else:
            print(
                f'"{answer}" is wrong'
                ' answer ;(. '
                'Correct answer '
                f'was "{correct_answer}".'
            )
            defeat()
            break
    if score == 3:
        win()


def win():
    print(f'Congratulations, {nickname}!')


def defeat():
    print(f'Let\'s try again, {nickname}!')
