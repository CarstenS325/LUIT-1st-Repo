# Write a program that implements a simple interactive dictionary.
# "Enter a word in English or EXIT: "
# When the user enters EXIT in capital letters, terminate the program with the following:
# "Bye!"
# Otherwise, try to find the German equivalent in the dictionary provided in the exercise.

sample_dict = {
    "mouth": "Mund",
    "finger": "Finger",
    "leg": "Bein",
    "hand": "Hand",
    "face": "Gesicht",
    "nose": "Nase"
}
while True:
    word = input('Enter a word in English or EXIT: ')  # Prompt the user to enter a word or 'EXIT'
    if word in sample_dict: # Check if the entered word is a key in the dictionary 'sample_dict'
        print('Translation: ', sample_dict[word])   # Print the value associated with the entered word
    elif word == 'EXIT': # Check if the entered word is 'EXIT'
        print('Bye!')    # Print a goodbye message
        break
    else: # Handle cases where the entered word is not in the dictionary and is not 'EXIT'
        print('No Match!')     # Print a message indicating no match was found