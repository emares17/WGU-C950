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
truck2 = Truck([3,6,12,17,18,19,21,22,23,24,26,27,35,36,38,39], 18, datetime.timedelta(hours=10, minutes=20), 0, 'HUB')
truck3 = Truck([2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 18, datetime.timedelta(hours=9, minutes=5), 0, 'HUB')

trucks = [truck1, truck2, truck3]

def id_to_address(truck):
    addresses = []

    for id in truck.packages:
        package = hash_map.get(id)

        if package in packages:
            addresses.append(package.address)

    return addresses

def package_status(id, time):
    (hour, minutes, seconds) = time.split(':')
    converted_time = datetime.timedelta(hours = int(hour), minutes = int(minutes), seconds = int(seconds))

    for package in packages:
        if package.ID == id:
            if package.del_time < converted_time:
                package.status = 'Delivered'
            elif converted_time > package.depart_time and converted_time < package.del_time:
                package.status = 'En Route'
            else:
                package.status = 'At Hub'

            return f'Package {id} current status is {package.status}'
        
def view_all(time):
    for package in packages:
        package_status(package.ID, time)
        print(package)
        
def view_single(id, time):
    package = hash_map.get(id)

    if package is not None:
        package_status(package.ID, time)
        print(package)

def calculate_milage(trucks):
    count = 0
    for truck in trucks:
        count += truck.milage

    return f'{count:.2f}'

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
            package.depart_time = truck.departure_time
            package.del_time = truck.current_time
            break
        else:
            truck.current_time += datetime.timedelta(hours = nearest_distance / 18) 

        truck.milage += nearest_distance

        package = hash_map.get(truck.packages[current_location])
        package.depart_time = truck.departure_time
        package.del_time = truck.current_time

        truck.current_loc = nearest_location
        current_location = nearest_location

for truck in trucks:
    nearest_neighbor(truck)

# for package in packages:
#     if int(package.ID) in truck1.packages or int(package.ID) in truck2.packages or int(package.ID) in truck3.packages:
#         print(package.ID, package.status, package.depart_time, package.del_time)

class main:
    print('Welcome to WGUPS delivery!')
    print(f'The total milage driven today was {calculate_milage(trucks)} miles.')

    while True:
        print('Would you like to search a package or view all?')
        search = input("Enter 'All' to view all packages or enter a package ID: ")
        
        if search.lower() != 'all' and search != search.isdigit():
            exit = input('Would you like to exit? Yes or No: ')
            if exit.lower() == 'yes':
                break
        else:
            time = input('Enter a time in HH:MM:SS format only: ')
            print(search, time)

            if search.isdigit():
                id = int(search)
                view_single(id, time)

            elif search.lower() == 'all':
                view_all(time)
                single_search = input('Would you like to search a single package?: Yes or No: ')
                if single_search.lower() == 'yes':
                    package_id = input('Please enter a package number: ')
                    time = input('Enter a time in HH:MM:SS format only: ')
                    id = int(package_id)
                    view_single(id, time)
                else:
                    break
            else:
                exit = input('Would you like to exit? Yes or No: ')

                if exit.lower() == 'yes':
                    break

