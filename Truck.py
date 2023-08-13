class Truck:
    def __init__(self, packages, speed, departure_time, milage, current_loc):
        self.packages = packages
        self.speed = speed
        self.departure_time = departure_time
        self.milage = milage
        self.current_time = departure_time
        self.current_loc = current_loc

    def __str__(self):
        return f'Current Packages: {self.packages}, Traveling Speed: {self.speed}, Departure Time: {self.departure_time}, Current Traveled Milage: {self.milage}'

