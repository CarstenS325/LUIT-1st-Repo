# List of integers (elements of the list = integers)
ran_list = [0, 1, 2, 3, 4, 5]

# List of variables (elements of the list = words/letters)
countries = ['UK', 'USA', 'France']

# Mixed Data types (Not recommended)
countries = [1, 'UK', 2, 'USA']

# Lists with lists as elements 
cells = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
print(cells[0])
print(cells[0][1])
print(cells[1][2])

# Print each rows
for x in cells: 
    print('Element:', x)

# Print each individual cell on each line 
for x in cells: 
    for y in x: 
        print('Element: ', y)

# Same code, but shows it is just like Excel or Google sheets
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table: 
    for cell in row: 
        print('Element: ', cell)

# Print as a table 
table = [['A1', 'A2', 'A3'], ['B1', 'B2', 'B3']]
for row in table: 
    for cell in row: 
        print(cell, '', end='')
    print()

# Take below values and creates lists inside a list until the number of lists reaches our set limit (j)

#1 2 3 4 5 
#1 2 3 4 5 
#1 2 3 4 5 
#1 2 3 4 5 

table = [[i for i in range(1, 6)] for j in range (4)]
print(table)