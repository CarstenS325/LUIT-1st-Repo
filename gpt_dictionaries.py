# Dictionary with sample words and their translations
sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}

# Start an infinite loop to keep asking for input
while True:
    # Prompt the user to enter a word or 'EXIT'
    word = input('Enter a word in English or EXIT: ')
    
    # Check if the entered word is a key in the dictionary
    if word in sample_dict:
        # Print the corresponding translation
        print(sample_dict[word])
    # Check if the entered word is 'EXIT'
    elif word == 'EXIT':
        # Print a goodbye message and exit the loop
        print('Bye!')
        break
    # Handle cases where the entered word is not in the dictionary and is not 'EXIT'
    else:
        # Print a message indicating no match was found
        print('No Match!')