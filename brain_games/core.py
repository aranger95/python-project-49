import prompt
from brain_games.scripts import exodus


def engine(game):
    score = 0
    ROUNDS = 3

    while score < ROUNDS:
        correct_answer, question = game()
        print(f'Question: {question}')
        # print(correct_answer)
        answer = prompt.string('Your answer: ')
        if str(answer) != str(correct_answer):
            exodus.defeat()
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
            exodus.defeat()
            break
    if score == 3:
        exodus.win()
