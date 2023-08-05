import csv
import datetime
from Distance import calculate_distance
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

truck1 = Truck([1,2,3,4,5], 18, datetime.timedelta(hours=8), 0)

def route(truck):
    address = []

    for id in truck.packages:
        package = hash_map.get(id)

        if package in packages:
            address.append(package.address)
    
    milage = 0

    for distance in range(len(address) - 1):
        milage += calculate_distance(address[distance], address[distance + 1])

    return milage

print(route(truck1))
