# Name: Fidel Mares
# Student ID: 001413646
# Class: WGU C950 Data Structures and Algorithms II

import csv
import datetime
from Distance import calculate_distance, distances
from HashTable import HashTable
from Package import Package
from Truck import truck1, truck2, truck3

package_file = 'CSV/package_file.csv'

packages = []
hash_table = HashTable()

with open(package_file, newline = '') as file:
    reader = csv.reader(file)
    for row in reader:
        id, address, city, state, zipcode, deadline, weight, status = row
        package = Package(ID = id, address = address, del_city = city, del_state = state, del_zipcode = zipcode, deadline = deadline, weight=weight, status = 'At Hub')

        packages.append(package)

        hash_table.insert(int(id), package)

trucks = [truck1, truck2, truck3]

def id_to_address(truck):
    addresses = []

    for id in truck.packages:
        package = hash_table.get(id)

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
    package = hash_table.get(id)

    if package is not None:
        package_status(package.ID, time)
        print(package)

def calculate_milage(trucks):
    count = 0
    for truck in trucks:
        count += truck.milage

    return f'{count:.2f}'

def nearest_neighbor(truck):
    truck_packages = id_to_address(truck)
    total_locations = len(truck_packages)
    visited = [False] * total_locations
    current_location = 0 
    truck.milage += calculate_distance(truck.current_loc, truck_packages[0])

    for _ in range(total_locations):
        visited[current_location] = True
        nearest_distance = float('inf')
        nearest_location = -1

        for next_location in range(total_locations):
            if not visited[next_location]:
                distance = calculate_distance(truck_packages[current_location], truck_packages[next_location])
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_location = next_location
        if nearest_location == -1:
            package = hash_table.get(truck.packages[current_location])
            package.depart_time = truck.departure_time
            package.del_time = truck.current_time
            break
        else:
            truck.current_time += datetime.timedelta(hours = nearest_distance / 18) 

        truck.milage += nearest_distance

        package = hash_table.get(truck.packages[current_location])
        package.depart_time = truck.departure_time
        package.del_time = truck.current_time

        truck.current_loc = nearest_location
        current_location = nearest_location

for truck in trucks:
    nearest_neighbor(truck)

class main:
    print('Welcome to WGUPS delivery!')
    print(f'The total milage driven today was {calculate_milage(trucks)} miles.')

    while True:
        print('Would you like to search a package or view all?')
        search = input("Enter 'All' to view all packages or enter a package ID: ")
        
        if search.lower() != 'all' and not search.isdigit():
            exit = input('Would you like to exit? Yes or No: ')
            if exit.lower() == 'yes':
                break
        else:
            time = input('Enter a time in HH:MM:SS format only: ')

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
                    exit = input('Would you like to exit? Yes or No: ')
                    if exit.lower() == 'yes':
                        break
            else:
                exit = input('Would you like to exit? Yes or No: ')

                if exit.lower() == 'yes':
                    break

