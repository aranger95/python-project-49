from brain_games.cli import welcome_user


nickname = welcome_user()


def win():
    print(f'Congratulations, {nickname}!')


def defeat():
    print(f'Let\'s try again, {nickname}!')
