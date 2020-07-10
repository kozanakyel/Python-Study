
class Spam:
    numInstances = 0
    def __init__(self):
        Spam.numInstances += 1
        
    @staticmethod
    def printNumInstances():
        print("Number of instances created: ", Spam.numInstances)

a = Spam()
b = Spam()
c = Spam()
Spam.printNumInstances()
a.printNumInstances()

class tracer:
    def __init__(self,func):
        self.calls = 0
        self.func = func
    def __call__(self,*args):
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))
        self.func(*args)
        
@tracer
def spam(a,b,c):
    print(a,b,c)
    
spam(1,2,3)
spam('a','b','c')
spam(4,5,6)

class C:
    shared = []
    def __init__(self):
        self.preobj = []
        
x = C()
y = C()
print(y.shared,y.preobj)
x.shared.append('spam')
x.preobj.append('kozan')
print(x.shared,x.preobj)

print(y.shared,y.preobj)
