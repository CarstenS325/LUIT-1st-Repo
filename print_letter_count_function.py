def print_letter_count(text, letter): # Define function 
    counter = 0 # Initialize a counter to keep track of the occurrences of the specified letter
    for char in text:   # Iterate over each character in the given text
        if char == letter:  # Check if the current character matches the specified letter
            counter += 1    # Increment the counter by 1 for each match found
    print('Number of', letter, 'is', counter)   # Print the current count of the specified letter
print_letter_count('Get wrecked Donnie', 'e')   # Call the function with a text and a letter to count its occurrences
print_letter_count('e', 'Welcome') # Shows that it's searching "e" for "welcome"
print_letter_count(letter='e', text='Welcome') # shows the print will always search the letter in the text regarless of orientaiton 