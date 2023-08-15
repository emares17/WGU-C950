class Package:
    def __init__(self, ID, address, del_city, del_state, del_zip, deadline, weight, status):
        self.ID = ID
        self.address = address
        self.deadline = deadline
        self.del_city = del_city
        self.del_state = del_state
        self.del_zip = del_zip
        self.weight = weight
        self.status = status
        self.del_time = None
        self.depart_time = None

    def __str__(self):
        return f'Package ID: {self.ID}, Address: {self.address}, City: {self.del_city}' \
            f' State: {self.del_state}, Zip Code: {self.del_zip}' \
            f' Deadline: {self.deadline}, Weight: {self.weight}, Status: {self.status}, Delivery Time: {self.del_time}, Departure Time: {self.depart_time}'
    
