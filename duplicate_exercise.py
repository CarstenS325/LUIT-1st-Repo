def unique(var_list=[]):  # define function 
    empty_list = []     # Initialize an empty list to hold unique elements
    for var in var_list:    # Iterate over each element in the input list
        if var not in empty_list:        # Check if the element is not already in the 'empty_list'
            empty_list.append(var)            # Append the element to 'empty_list' if it's not a duplicate
    return empty_list    # Return the list of unique elements
print(unique([1, 1, 4, 5, 1]))  # Test the function with a list of numbers
                                    # Output: [1, 4, 5]
print(unique(['Mark', 'Mark', 'John', 'Anne'])) # Test the function with a list of names
                                                    # Output: ['Mark', 'John', 'Anne']