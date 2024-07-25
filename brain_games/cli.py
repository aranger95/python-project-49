import prompt


def welcome_user():
    global nickname
    nickname = prompt.string('May I have your name? ')
    print(f'Hello, {nickname}')
    return nickname
