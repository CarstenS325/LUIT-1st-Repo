# Print 6th character in a variable 
band = 'Green Day'
print(band[6])

# Print up to the 6th character in a variable 
band = 'Green Day'
print(band[:6])

# Capitalize all letters
text = 'capitalised phrase'
text_cap = text.upper()
print(text_cap)

# Capitalizes the first letter in a phrase
text = 'capitalised phrase'
text_proper = text.capitalize()
print(text_proper)

# Capitalizes first letter in all words 
text = 'capitalised phrase'
text_cap = text.title()
print(text_cap)

# Check is input is entered correctly (as a number in this example)
user_number = input('Please provide a number: ')
if user_number.isnumeric():
    print('Thank you, that\'s a correct number')
else:
    print('Sorry,', user_number, 'is not a number.')
