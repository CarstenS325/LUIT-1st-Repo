# Printing each letter on individual line
for char in 'Happy Birthday':
    print(char)

# Check if variable is in predetermined list
guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name in guests: 
    print('Welcome to the party!')
else: 
    print('Sorry, you are not on the list')

#  Check if variable is not in predetermined list
guests = ['Kate', 'Adam', 'Kerry', 'Joe', 'Anne', 'Marie']
name = input('What is your name? ')
if name not in guests: 
    print('Sorry, you are not on the list')
else: 
    print('Welcome to the party!')