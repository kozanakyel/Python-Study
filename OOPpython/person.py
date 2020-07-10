from classtools import AttrDisplay

class Person(AttrDisplay):   
    def __init__(self,name,job = None,pay = 0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)
    
class Manager(Person):
    def __init__(self,name,pay):
        Person.__init__(self,name,'mgr',pay)
    def giveRaise(self,percent,bonus=.10):
        Person.giveRaise(self, percent + bonus)
    

class Department:
    def __init__(self,*args):
        self.members = list(args)
    def addMember(self,person):
        self.members.append(person)
    def giveRaises(self,percent):
        for person in self.members:
            person.giveRaise(percent)
    def showAll(self):
        for person in self.members:
            print(person)
        
if __name__ == '__main__':        
    bob=Person('bob sth')
    sue = Person('sue hohn', job='dev',pay=100000)
    print(bob.name,bob.pay)
    print(sue.name,sue.pay)
    print('{0} {1}'.format(bob.name,bob.pay))
    print(bob.name.split()[-1])
    #sue.pay *= 1.10
    print(sue.pay)
    print(bob.lastName(), sue.lastName())
    print(sue)
    sue.giveRaise(.10)
    print(sue.pay)
    print(sue)
    print(bob)
    tom = Manager('tom jones',50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)
    
    print('--All three--')
    for object in (bob,sue,tom):
        object.giveRaise(.10)
        print(object)
        
    development = Department(bob,sue)
    development.addMember(tom)
    development.giveRaises(.10)
    development.showAll()
