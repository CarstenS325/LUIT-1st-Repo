answer_a = int(input('How many days ago have you purchased the item? '))
if answer_a <= 10:
    answer_b = input('Have you used the item? y/n ')
    if answer_b == 'y':
        answer_c = input('Has the item broken down on its own? y/n ')
        if answer_c == 'y':
                    print('You can get a refund.')
        else:
                    print('You cannot get a refund')
    else:
            print('You can get a refund.')
else:
    answer_d = input('Has the item broken down on its own? y/n ') 
    if answer_d == 'y':
        print('You can get a refund.')
    else:
        print('You cannot get a refund')