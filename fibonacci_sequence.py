# Print the first 10 numbers in the Fibonacci sequence
a, b = 0, 1
for _ in range(10):
    print(a, end=' ')
    a, b = b, a + b
print()