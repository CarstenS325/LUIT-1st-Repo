secret_number = 14 
print('''
===============================
=====  SECRET NUMBER GAME =====
===============================
''')
user_input = int(input('Try to guess the secret number from 0 - 20:' ))
while user_input != secret_number:
    print('Wrong!')
    user_input = int(input('Try to guess the secret number form 0 - 20: '))
print('Perfect! You have guessed the secret number!')