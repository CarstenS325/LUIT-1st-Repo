# Creating a list 1-100
numbers = []
for i in range(1, 101):
    numbers.append(i)
print(numbers)

# Shorter way to create list
numbers = [i for i in range(1, 101)]
print(numbers)

# Skip numbers that are divisible by a number
numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)