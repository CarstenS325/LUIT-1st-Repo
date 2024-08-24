def print_letter_count(text, letter): # Define function 
    counter = 0 # Initialize a counter to keep track of the occurrences of the specified letter
    for char in text:   # Iterate over each character in the given text
        if char == letter:  # Check if the current character matches the specified letter
            counter += 1    # Increment the counter by 1 for each match found
    print('Number of', letter, 'is', counter)   # Print the current count of the specified letter

def print_letter_count(text, letter='a'): # Define function * defines defines 'a' as the search parameter
    counter = 0 # Initialize a counter to keep track of the occurrences of the specified letter
    for char in text:   # Iterate over each character in the given text
        if char == letter:  # Check if the current character matches the specified letter
            counter += 1    # Increment the counter by 1 for each match found
    print('Number of', letter, 'is', counter)   # Print the current count of the specified letter

def print_letter_count(text='This is the default string to search', letter='a'): # Define function * defines 'a' as the search parameter, and the set string to search
    counter = 0 # Initialize a counter to keep track of the occurrences of the specified letter
    for char in text:   # Iterate over each character in the given text
        if char == letter:  # Check if the current character matches the specified letter
            counter += 1    # Increment the counter by 1 for each match found
    print('Number of', letter, 'is', counter)   # Print the current count of the specified letter

print_letter_count()
