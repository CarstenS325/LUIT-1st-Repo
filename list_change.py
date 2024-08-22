# Wrong way to do it
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping: ', first, second)
first = second
second = first
print('After swapping: ', first, second)

# One way to do it
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping: ', first, second)
temporary = first
first = second
second = temporary
print('After swapping: ', first, second)

# Shorter way to do it
first = input('Enter first number: ')
second = input('Enter second number: ')
print('Before swapping: ', first, second)
first, second = second, first
print('After swapping: ', first, second)