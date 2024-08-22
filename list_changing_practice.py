# Changing Order
cities = ['Sioux Falls', 'Las Vegas', 'Levenworth', 'Spokane']
print(cities)
cities[0], cities[1] = cities[1], cities[0]
print(cities)

# Alphabetize 
cities = ['Sioux Falls', 'Las Vegas', 'Levenworth', 'Spokane']
cities.sort()
print(cities)

# Sort numbers lower to greater 
ran_list = [1.1, 5.5, 0, 1, 2.2, 0.3, 4, 5]
ran_list.sort()
print(ran_list)

# Sort numbers greater to lower 
ran_list = [1.1, 5.5, 0, 1, 2.2, 0.3, 4, 5]
ran_list.sort(reverse=True)
print(ran_list)

# Sorted list temporarily inside the code
cities = ['Sioux Falls', 'Las Vegas', 'Levenworth', 'Spokane']
print(sorted(cities))
print(cities)