import prompt
from brain_games.cli import welcome_user


def engine(game):
    nickname = welcome_user()
    print(game.QUESTION)
    score = 0
    ROUNDS = 3

    while score < ROUNDS:
        correct_answer, question = game.game_choice()
        print(f'Question: {question}')
        # print(correct_answer)
        answer = prompt.string('Your answer: ')
        if str(answer) != str(correct_answer):
            print(f'Let\'s try again, {nickname}!')
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
            print(f'Let\'s try again, {nickname}!')
            break
    if score == 3:
        print(f'Congratulations, {nickname}!')