# Changing variable inside code 
name_original = 'Jon Snow'
name_new = name_original
name_original = 'Daenerys Targaryen'
print(name_original, name_new)

# Failing list copying
list_original = [1, 2, 3]
list_new = list_original
list_original[0] = -5
print('Original: ',list_original, '\nNew: ',list_new)

# List copying with slicing 
list_original = [1, 2, 3]
list_new = list_original[:]
list_original[0] = -5
print('Original: ',list_original, '\nNew: ',list_new)

# Copying list until set number 
list_original = [1, 2, 3]
list_new = list_original[:2]
list_original[0] = -5
print('Original: ',list_original, '\nNew: ',list_new)

# Summary
# These will always print the same lists, modifying one - Modifys the other 
list_original = [1, 2, 3]
list_new = list_original

# This will copy the list without modifying the origianl inside the code (2 different list, 2 different variables)
list_original = [1, 2, 3]
list_new = list_original[:]
