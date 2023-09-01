import csv

# Initiatizes a variable to the distance file that will be used.
distance_file = 'CSV/distance_file.csv'

# Uses csv.reader to iterate through the distance file and extract a list of addresses, headers, and distances.
def read_distance_matrix(distance_file):
    distances = []
    addresses = []
    with open(distance_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        headers = next(reader)[1:]

        for row in reader:
            address = row[0]
            addresses.append(address)
            
            distances.append([0 if element == '' else float(element) for element in row[1:]])

    return distances, headers, addresses

# Assigns variables to the returned values from read_distance_matrix().
distances, headers, addresses = read_distance_matrix(distance_file)

# Takes in the arguments of current_package and next_package.
# Iterates through both the addresses and headers variables to find the index of each argument and breaks the loop when found.
def calculate_distance(current_package, next_package):
    current_address = None
    next_address = None

    for idx, val in enumerate(addresses):
        if val == current_package:
            current_address = idx
            break

    for idx, val in enumerate(headers):
        if val == next_package:
            next_address = idx 
            break
    
    # Sets a distance variable to return the exact distance from the distances variable at the intersection of [current_address][next_address]
    distance = distances[current_address][next_address]
   
    return distances[next_address][current_address] if distance == 0 else distance



