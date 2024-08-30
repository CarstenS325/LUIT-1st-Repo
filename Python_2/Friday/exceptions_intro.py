value = int(input('Enter an integer: ')) # Attempt to get input from the user and calculate the inverse
print('The inverse of', value, 'is', 1/value)  # Print the inverse of the provided number




try: # Handle potential exceptions
    value = int(input('Enter an integer: '))  # Try to get input and convert it to an integer
    print('The inverse of', value, 'is', 1/value)  # Print the inverse
except:
    print('You did not provide a number, so I will not calculate the inverse')     # Catch any exception and inform the user





try: # Handle specific exceptions
    value = int(input('Enter an integer: '))  # Try to get input and convert it to an integer
    print('The inverse of', value, 'is', 1/value)  # Print the inverse
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')    # Handle the case where the input is not a valid integer
except ZeroDivisionError:
    print('You provided 0, and division by 0 is not possible.')     # Handle the case where the user provides 0 (division by zero)






try:    # Handle specific exceptions and catch any other unforeseen exceptions
    value = int(input('Enter an integer: '))  # Try to get input and convert it to an integer
    print('The inverse of', value, 'is', 1/value)  # Print the inverse
except ValueError:
    print('You did not provide a number, so I will not calculate the inverse')    # Handle the case where the input is not a valid integer
except ZeroDivisionError:
    print('You provided 0, and division by 0 is not possible.')    # Handle the case where the user provides 0 (division by zero)
except:
    print('Hmm... that\'s not right')     # Catch any other unforeseen exceptions

