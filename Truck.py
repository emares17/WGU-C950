import datetime

class Truck:
    # Initializes the attributes for the Truck object.
    def __init__(self, packages, speed, departure_time, milage, current_loc):
        self.packages = packages
        self.speed = speed
        self.departure_time = departure_time
        self.milage = milage
        self.current_time = departure_time
        self.current_loc = current_loc

    # Returns a string with attributes from the Truck object.
    def __str__(self):
        return f'Current Packages: {self.packages}, Traveling Speed: {self.speed}, Departure Time: {self.departure_time}, Current Traveled Milage: {self.milage}'

# Creates the Truck objects that will be used in the program, all packages are manually loaded.
truck1 = Truck([1, 13, 14, 15, 16, 20, 29, 30, 31, 34, 37, 40], 18, datetime.timedelta(hours=8), 0, 'HUB')
truck2 = Truck([3,6,12,17,18,19,21,22,23,24,26,27,35,36,38,39], 18, datetime.timedelta(hours=10, minutes=20), 0, 'HUB')
truck3 = Truck([2, 4, 5, 6, 7, 8, 9, 10, 11, 25, 28, 32, 33], 18, datetime.timedelta(hours=9, minutes=5), 0, 'HUB')
