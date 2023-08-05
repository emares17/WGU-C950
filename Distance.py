import csv
from HashTable import Hashmap
from Package import Package

distance_file = 'CSV/distance_file.csv'


def read_distance_matrix(distance_file):
    distances = []
    addresses = []
    with open(distance_file, newline='') as csvfile:
        reader = csv.reader(csvfile)
        column_headers = next(reader)[1:]

        for row in reader:
            address = row[0]
            addresses.append(address)
            
            distances.append([element for element in row[1:]])

    return distances, column_headers, addresses

distances, headers, addresses = read_distance_matrix(distance_file)

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

    distance = distances[current_address][next_address]

    if distance == '':
        return 0.0
    else:    
        return float(distance)

