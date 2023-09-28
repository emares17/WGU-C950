class Package:
    # Initializes the attributes for the Package object.
    def __init__(self, ID, address, del_city, del_state, del_zipcode, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.deadline = deadline
        self.del_city = del_city
        self.del_state = del_state
        self.del_zipcode = del_zipcode
        self.weight = weight
        self.status = status
        self.del_time = None
        self.depart_time = None

    # Returns a string with attributes from the Package object.
    def __str__(self):
        return f'Package ID: {self.ID}, Address: {self.address}, City: {self.del_city},' \
            f' State: {self.del_state}, Zip Code: {self.del_zipcode}' \
            f' Status: {self.status}, Delivery Time: {self.del_time}, Departure Time: {self.depart_time}'
    
