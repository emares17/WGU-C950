class Truck:
    def __init__(self, packages, speed, departure_time, milage ):
        self.packages = packages
        self.speed = speed
        self.departure_time = departure_time
        self.milage = milage
        self.current_time = departure_time

    def __str__(self):
        return f'Current Packages: {self.packages}, Traveling Speed: {self.speed}, Departure Time: {self.departure_time}, Current Traveled Milage: {self.milage}'

