def get_average(input_numbers): #define function "get_average"
    sum = 0.0   # Initialize a variable to keep track of the sum of the numbers
    for number in input_numbers:    # Iterate over each number in the input list
        sum += number   # Add the current number to the sum
    average = sum / len(input_numbers)  # Calculate the average by dividing the sum by the number of elements
    print(average)  # Print the calculated average
get_average([5.0, 3.5, 7.8, 9.9, 10.0]) # Call the function with a list of numbers and print their average
