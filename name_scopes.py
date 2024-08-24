def show_truth():   # Define a function that prints a local variable
    mysterious_var = 'New Surprise!' # Local variable inside the function; it doesn't affect variables outside this function
    print(mysterious_var)    # Print the local variable
mysterious_var = 'Surprise'     # Global variable with the same name as the local variable in the function
print(mysterious_var)   # Print the global variable
show_truth() # Call the function; it prints the local variable inside the function
print(mysterious_var)  # Print the global variable again; it remains unchanged by the function



def show_truth(): # Define a function that modifies a global variable
    global mysterious_var    # Declare that we are using the global variable 'mysterious_var'
    mysterious_var = 'New Surprise!'        # Modify the global variable
    print(mysterious_var)     # Print the modified global variable
mysterious_var = 'Surprise' # Global variable with an initial value
print(mysterious_var)   # Print the global variable before calling the function
show_truth()    # Call the function; it modifies the global variable
print(mysterious_var)   # Print the global variable again; it has been updated by the function

