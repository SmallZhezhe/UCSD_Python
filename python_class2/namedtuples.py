"""
namedtuple examples for REPL
"""

from collections import namedtuple
Name = namedtuple('Name', ['first', 'last'])

def split_name(name):
    first, last = name.split(" ", 1)
    return Name(first, last)


"""
names = split_name("Diane Chen")
names
names.first
names.last
first_name, last_name = names
print(first_name, last_name)
"""

LatLong = namedtuple('LatLong', 'lat long')
location = LatLong(lat=32.733999, long=-117.147777)
location.lat
my_lat, my_long = location
my_lat
my_long


from collections import namedtuple

EmployeeRecord = namedtuple('EmployeeRecord',
    'name, age, title, department, paygrade')
emp_data = ["Ralph Jones", 50, "Supervisor", "IT", "S-12"]
emp1 = EmployeeRecord(emp_data)

emp1 = EmployeeRecord(*emp_data)
emp1
emp2 = EmployeeRecord._make(emp_data)
emp2

emp1 = EmployeeRecord("Sally Smith", 33, "Programmer", "IT", "P-11")
emp1


# EmployeeRecord(name='Ralph Jones', age=50, title='Supervisor', department='IT', paygrade='S-12')
