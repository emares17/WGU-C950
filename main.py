import csv
import datetime
from Distance import calculate_distance, distances
from HashTable import Hashmap
from Package import Package
from Truck import Truck

package_file = 'CSV/package_file.csv'

packages = []
hash_map = Hashmap()


with open(package_file, newline = '') as file:
    reader = csv.reader(file)
    for row in reader:
        id, address, city, state, zipcode, deadline, weight, status = row
        package = Package(ID = id, address = address, del_city = city, del_state = state, del_zip = zipcode, deadline = deadline, weight=weight, status = 'At Hub')

        packages.append(package)

        hash_map.insert(int(id), package)


truck1 = Truck([1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 18, datetime.timedelta(hours=8), 0, 'HUB')

def id_to_address(truck):
    addresses = []

    for id in truck.packages:
        package = hash_map.get(id)

        if package in packages:
            addresses.append(package.address)

    return addresses


def nearest_neighbor(truck):
    packages1 = id_to_address(truck)
    total_locations = len(packages1)
    visited = [False] * total_locations
    current_location = 0 
    truck.milage += calculate_distance(truck.current_loc, packages1[0])

    for _ in range(total_locations):
        visited[current_location] = True
        nearest_distance = float('inf')
        nearest_location = -1

        for next_location in range(total_locations):
            if not visited[next_location]:
                distance = calculate_distance(packages1[current_location], packages1[next_location])
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_location = next_location
        if nearest_location == -1:
            package = hash_map.get(truck.packages[current_location])
            package.del_time = truck.current_time
            # package.status = 'Delivered'
            break
        else:
            truck.current_time += datetime.timedelta(hours = nearest_distance / 18) 

        truck.milage += nearest_distance

        package = hash_map.get(truck.packages[current_location])
        package.depart_time = truck.departure_time
        package.del_time = truck.current_time
        # package.status = 'Delivered'

        truck.current_loc = nearest_location
        current_location = nearest_location

print(nearest_neighbor(truck1))

