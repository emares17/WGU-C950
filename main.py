# Name: Fidel Mares
# Student ID: 001413646
# Class: WGU C950 Data Structures and Algorithms II

import csv
import datetime
from Distance import calculate_distance, distances
from HashTable import HashTable
from Package import Package
from Truck import truck1, truck2, truck3

# Initiates variable to the package file that will be used in the program.
package_file = 'CSV/package_file.csv'

# Packages list will be used to append each Package object of each package in the package file.
packages = []

# Sets variable to use HashTable methods.
hash_table = HashTable()

# Opens the package file using csv.reader, this iterates over the file and unpacks the data into variables to set as 
# package attributes. A Package object is then created for each individual package and appended to the packages list. Lastly, each
# package is inserted into the hash table using the package ID as the key.
with open(package_file, newline = '') as file:
    reader = csv.reader(file)
    for row in reader:
        id, address, city, state, zipcode, deadline, weight, status = row
        package = Package(ID = id, address = address, del_city = city, del_state = state, del_zipcode = zipcode, deadline = deadline, weight=weight, status = 'At Hub')

        packages.append(package)

        hash_table.insert(int(id), package)

# Creates a truck list from the truck objects.
trucks = [truck1, truck2, truck3]

# Used to convert package ID to exact addresses. Iterates over each package ID in the truck, finds a matching package ID in the packages list,
# and appends the exact address to the addresses list.
def id_to_address(truck):
    addresses = []

    for id in truck.packages:
        package = hash_table.get(id)

        if package in packages:
            addresses.append(package.address)

    return addresses

# Used to adjust package status accordingly in the UI. Takes a package ID and an exact time as parameters. Splits the entered time to
# make it readable for datetime. It then iterates to find a matching ID in the packages list, if found, it updates the the status to "At Hub", "En Route", or "Delivered". 
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

# Used to display all packages according to the given time in the user interface. The user will be prompted to enter a time when the select to view all packages.
# This function will then be called in which it iterates through each package of the packages list, updates the status using the package_status() function, 
# and then prints out every individual package.
def view_all(time):
    for package in packages:
        package_status(package.ID, time)
        print(package)
        
# Used in the user interface to display a single package search at a given time. If the package is found in the Hash Table, it updates the package status using the package_status()
# function and then prints the package with all of its attributes.
def view_single(id, time):
    package = hash_table.get(id)

    if package is not None:
        package_status(package.ID, time)
        print(package)

# Calculates the total milage driven by all truck by iterating over the total driven milage of each truck.
def calculate_milage(trucks):
    count = 0
    for truck in trucks:
        count += truck.milage

    return f'{count:.2f}'

# Main function of the program using the Nearest Neighbor algorithm.
def nearest_neighbor(truck):
    # Initiates a list the will hold all the exact addresses of each package, this will be achieved by calling the id_to_address() function 
    # and converting all package ID's to exact addresses.
    truck_packages = id_to_address(truck)
    # Sets the total_locations variable to the length of the truck_packages list.
    total_locations = len(truck_packages)
    # Used to keep track of all the visited locations.
    visited = [False] * total_locations
    # Sets the initial location to index 0.
    current_location = 0
    # Calculates the distance from the HUB to the first location. 
    truck.milage += calculate_distance(truck.current_loc, truck_packages[0])

    # Iterates over the total_locations variable to begin the main loop of the function.
    for _ in range(total_locations):
        # Marks the current visited location as True.
        visited[current_location] = True
        # Sets the variables to track the nearest distance and location.
        nearest_distance = float('inf')
        nearest_location = -1

        # Iterates over all the next_location to begin the nested loop to find the next best location to visit.
        for next_location in range(total_locations):
            # Checks if the next location is marked as False.
            if not visited[next_location]:
                # Uses the calculate_distance() function to calculate the distance between the current and next location.
                distance = calculate_distance(truck_packages[current_location], truck_packages[next_location])
                # Updates the nearest_location if the distance is shorter.
                if distance < nearest_distance:
                    nearest_distance = distance
                    nearest_location = next_location
        # If the nearest_location is equal to -1, we have reached the end and there is no more locations to visit.
        # At this point we update package variables for the last location, which at this point will be at the current_location.
        # We then break out of the loop.
        if nearest_location == -1:
            package = hash_table.get(truck.packages[current_location])
            package.depart_time = truck.departure_time
            package.del_time = truck.current_time
            break
        else:
            # If this part of the code executes, we have not yet visited all locations so we have to continue updating the time variable.
            truck.current_time += datetime.timedelta(hours = nearest_distance / 18) 

        # Updates the driven milage of the truck.
        truck.milage += nearest_distance

        # Updates package variables.
        package = hash_table.get(truck.packages[current_location])
        package.depart_time = truck.departure_time
        package.del_time = truck.current_time

        # Updates truck current_loc variable and sets the current variable to the nearest_location.
        truck.current_loc = nearest_location
        current_location = nearest_location

# Runs each truck through the nearest_neighbor() function.
for truck in trucks:
    nearest_neighbor(truck)

# User interface allows the user to look-up all packages or individual packages at any given time. The program then displays the package/s with all
# of its attributes. The user will be prompted to continue searching or exit the program.
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

