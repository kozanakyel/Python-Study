class adder:
    def __init__(self,value=0):
        self.data = value
    def __add__(self,other):
        self.data += other

class addrepr(adder):
    def __repr__(self):
        return 'addrepr(%s)' % self.data
    
class addboth(adder):
    def __str__(self):
        return '[Value: %s]' % self.data
    def __repr__(self):
        return 'addboth(%s)' % self.data

class Commuter:
    def __init__(self,val):
        self.val = val
    def __add__(self,other):
        print('add',self.val,other)
        return self.val+other
    def __radd__(self,other):
        print('radd', salfe.val,other)
        return other+self.val
    def __iadd__(self, other):
        self.val += other
        return self
    def __str__(self):
        return '<Commuter: %s>' % self.val
    
x = Commuter(88)
y = Commuter(99)
print(x)

class Prod():
    def __init__(self,value):
        self.value = value
    def __call__(self,other):
        return self.value * other

x = Prod(2)
print(x(3))

class C:
    data = 'spam'
    def __gt__(self,other):       #greather than
        return self.data > other
    def __lt__(self,other):
        return self.data < other

class Life:
    def __init__(self,name='unknown'):
        print('hello', name)
        self.name = name
    def __del__(self):
        print('goodbye', self.name)
        
  

        
        