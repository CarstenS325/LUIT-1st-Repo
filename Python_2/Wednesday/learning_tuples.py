# Acts just like lists, however are immutable in the code. 
# In order to change any data in a tuple, you must manually change the code 
empty_tuple = ()
one_el_tuple_a = (1,)
one_el_tuple_b = 1,
three_el_tuple = 1, 2, 3,
print(three_el_tuple)
print(len(three_el_tuple))

# print "" if argument is true
user_data = ('John', 'American', 1964)
if 'American' in user_data: 
    print('This person comes from the US.')

# Print each element in the tuple 
user_data = ('John', 'American', 1964)
for element in user_data: 
    print(element)

# Adding to a tuple 
user_data = ('John', 'American', 1964) + ('teacher', 'male')
print(user_data)

numbers = (0, 1) * 10
print(numbers)

# Tuples are used mostly when you want data of different types grouped together