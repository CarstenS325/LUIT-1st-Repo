python_creation = 1994
user_input = int(input('When was Python 1.0 released?: '))
while user_input != python_creation:
    if user_input < python_creation:
        print('It was later than that!')
    else:
        print('It was earlier than that!')
    user_input = int(input('When was Python 1.0 released?: '))
print('Correct!')
