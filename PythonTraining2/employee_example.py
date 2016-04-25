from collections import namedtuple
from operator import itemgetter, attrgetter
from pprint import pprint
from heapq import nsmallest, nlargest
import sqlite3

Employee = namedtuple('Employee', 'id name title dept')

a = Employee('012303', 'Raymond Hettinger', 'Python Guy', 'Training')

staff = [
    Employee('012303', 'Raymond Hettinger', 'Python Guy', 'Training'),
    Employee('432941', 'Jaime Lannister', 'King Slayer', 'Security'),
    Employee('345345', 'Jack Bauer', 'Ex-Spy', 'Classified'),
    Employee('104357', 'Peter Pan', 'Boy', 'Fantasy'),
    Employee('555555', 'Daniel Miz', 'PyATS', 'Training'),
]

def get_name(emp):
    return emp.name

print map(get_name, staff)
print map(lambda emp: emp.name, staff)
print map(attrgetter('name'), staff)
print map(itemgetter(1), staff)

def get_dept_id(emp):
    return emp.dept, emp.id

print map(get_dept_id, staff)
print map(lambda emp: (emp.dept, emp.id), staff)
print map(attrgetter('dept','id'),staff)
print map(itemgetter(3,0),staff)

print zip(map(attrgetter('dept'), staff), map(attrgetter('id'), staff))

pprint(staff)
pprint(sorted(staff))
pprint(sorted(staff, key=attrgetter('name')))
pprint(sorted(staff, key=attrgetter('dept', 'name')))

data = [10, -5, 18, -8, 25, -90, 32, 5, -41, 7]

# Relationships between: min --> nsmallest --> sorted <-- nlargest <-- max
print sorted(data)
print sorted(data)[0], min(data)
print sorted(data)[-1], max(data)
print sorted(data)[:3], nsmallest(3, data)
print sorted(data)[-3:][::-1], nlargest(3, data)

# Data analysis with the tools combined together
print sorted(data, key=abs)
print nsmallest(3, data, key=lambda x: abs(x-9))   # cluster analysis:  3 data points closest to 9

# Databases
conn = sqlite3.connect(':memory:')
conn.execute('CREATE TABLE Employee (id TEXT, name TEXT, title TEXT, dept TEXT)')
conn.execute('CREATE INDEX DeptIndex ON Employee (dept)')
conn.executemany('INSERT INTO Employee VALUES (?,?,?,?)', staff)
conn.commit()

c = conn.cursor()
for row in c.execute('SELECT * FROM Employee WHERE dept = "Training"'):
    print row
print c.execute('SELECT COUNT(*) FROM Employee WHERE dept = "Training"').fetchone()

