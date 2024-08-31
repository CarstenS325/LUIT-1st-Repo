grades = {}  # Create an empty dictionary to store student names and their grades
grades['John'] = 'A-'  # Add an entry for 'John' with grade 'A-'
grades['Anne'] = 'B'   # Add an entry for 'Anne' with grade 'B'
print(grades)  # Print the dictionary to see the current state
grades['Anne'] = 'A'  # Update the grade for 'Anne' to 'A'
print(grades)  # Print the dictionary to see the updated state
grades.update({'John': 'A'})  # Update the grade for 'John' to 'A' using the update() method
print(grades)  # Print the dictionary to see the updated state
print(len(grades))  # Print the number of entries in the dictionary  (LEN = Length)
if 'John' in grades: # Check if 'John' is in the dictionary and print his grade if found
    print('John got:', grades['John']) # Print the grade for 'John'
del grades ['John'] # Remove the entry for 'John' from the dictionary
print(grades)  # Print the dictionary to see the state after removing 'John'

grades = {}  # Create an empty dictionary to store student names and their grades
grades['John'] = 'A-'  # Add an entry for 'John' with grade 'A-'
grades['Anne'] = 'B' # Add an entry for 'Anne' with grade 'B'

for el in grades: # Iterate over the dictionary and print each key
    print(el) # Print the key (student name) of the current dictionary entry

for el in grades.keys(): # Iterate over each key in the 'grades' dictionary
    print(el)     # Print the current key (which represents a student's name, for example)

for el in grades.values():  # Iterate over each value in the 'grades' dictionary
    print(el)      # Print the current value (which represents a grade, for example)

for person, grade in grades.items(): # Iterate over each key-value pair in the 'grades' dictionary
    print(person, 'got', grade)    # Print the person and their corresponding grade