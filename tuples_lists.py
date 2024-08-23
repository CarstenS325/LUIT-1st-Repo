# Tuples inside of lists
city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)
capitals = [('London', 'UK', 8.98), ('Canberra', 'Australia', 0.4), ('Algiers', 'Algeria', 3.9)]
for capital in capitals:
    print('Name: ', capital[0], ', Country:', capital[1], ', Population:', capital[2])

# Adding to a list inside of a tuple
user_data = ('John', 'American', 1964, [77.0, 78.2, 77.5])
user_data[3].append(79.6)
print(user_data)

# Test - Why is this any different than the first example? 
city_1 = ('London', 'UK', 8.98)
city_2 = ('Canberra', 'Australia', 0.4)
city_3 = ('Algiers', 'Algeria', 3.9)
capitals = [(city_1), (city_2), (city_3)]
for capital in capitals:
    print('Name: ', capital[0], ', Country:', capital[1], ', Population:', capital[2])
