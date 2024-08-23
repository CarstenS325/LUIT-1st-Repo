#Your task is to go through all the routes in a loop and check how many of them lead to Rome 
# (i.e. how many of them have city_to equal to 'Rome'). 
# Among the routes to Rome, you should also calculate the average flight time. 

# Print the following the output:
# {} connections lead to Rome with an average flight time of {} minutes
# Replace {} with the number of connections and the average flight time.

# format = (city_from, city_to, time)

connections = [
    ('Amsterdam', 'Dublin', 100),
    ('Amsterdam', 'Rome', 140),
    ('Rome', 'Warsaw', 130),
    ('Minsk', 'Prague', 95),
    ('Stockholm', 'Rome', 190),
    ('Copenhagen', 'Paris', 120),
    ('Madrid', 'Rome', 135),
    ('Lisbon', 'Rome', 170),
    ('Dublin', 'Rome', 170),
    ]

Rome = 0
flight_time = 0

for arrival in connections: 
    if arrival[1] == 'Rome':
        Rome += 1
        flight_time += arrival[2]
print(Rome, 'connections lead to Rome with an average flight time of', flight_time/Rome, 'minutes')