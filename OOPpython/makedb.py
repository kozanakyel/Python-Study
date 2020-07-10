import person
bob = person.Person('bob sth')

from person import Person
bob = Person('bob sth')

from person import Person, Manager
 # Load our classes
bob = Person('Bob Smith')
 # Re-create objects to be stored
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')
for object in (bob,sue,tom):
    db[object.name] = object
db.close()