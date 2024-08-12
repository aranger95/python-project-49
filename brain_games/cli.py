import prompt


def welcome_user():
    '''Returns the nickname variable.'''
    print('Welcome to the Brain Games!')
    nickname = prompt.string('May I have your name? ')
    print(f'Hello, {nickname}')
    return nickname
