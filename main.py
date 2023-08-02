import csv
from HashTable import Hashmap
from Package import Package

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


