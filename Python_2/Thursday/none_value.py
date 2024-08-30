print_return = print('Hello world') # Print 'Hello world' and assign the result (which is None) to 'print_return'
print(print_return) # Print the value of 'print_return'; it will be 'None' because 'print' does not return a value
def get_average(input_numbers): # Define a function to calculate the average of a list of numbers
    sum = 0.0    # Initialize sum to 0.0
    for number in input_numbers:    # Iterate over each number in the list
        sum += number        # Add each number to the sum
    average = sum / len(input_numbers)    # Calculate the average by dividing the sum by the number of elements
    return average    # Return the calculated average
print('The average is:', get_average([5.0, 3.5, 7.8, 9.9, 10.0]))   # Call the function with a list of numbers and print the result
average = get_average([5.0, 3.5, 7.8, 9.9, 10.0])   # Store the result of the average calculation in a variable
if average > 5.0:   # Check if the average is greater than 5.0
    print('The average is too high')        # Print a message if the condition is true


def is_first_last_equal(number_list):   # Define a function to check if the first and last elements of a list are equal
    if (number_list[0] == number_list[-1]):     # Compare the first and last elements of the list
        return True         # Return True if they are equal
    else:        # Return False if they are not equal
        return False
print(is_first_last_equal([10,20,30,40,10])) # Call the function with two different lists and print the results
                                                # True because the first and last elements are both 10
print(is_first_last_equal([10,20,30,40,50]))  # False because the first and last elements are 10 and 50
def is_first_last_equal(number_list):   # Define an improved function to check if the first and last elements of a list are equal
    if len(number_list) == 0:       # Check if the list is empty
        return        # Return None if the list is empty
    if (number_list[0] == number_list[-1]):     # Compare the first and last elements of the list
        return True        # Return True if they are equal
    else:        # Return False if they are not equal
        return False            # Return False if they are not equal
# Call the improved function with three different lists and print the results
print(is_first_last_equal([10,20,30,40,10]))  # True because the first and last elements are both 10
print(is_first_last_equal([10,20,30,40,50]))  # False because the first and last elements are 10 and 50
print(is_first_last_equal([]))  # None because the list is empty
