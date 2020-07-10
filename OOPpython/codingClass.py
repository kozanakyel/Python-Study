class Super:
    def method(self):
        print('in Super.method')
    def delegate(self):
        self.action()
        
class Inheritor(Super):
    pass

class Replacer(Super):
    def method(self):
        print('in replacermethod')
        
class Extender(Super):
    def method(self):
        print('starting extender')
        Super.method(self)
        print('ending extender')
        
class Provider(Super):
    def action(self):
        print('in provider.action')
        
if __name__ == '__main__':
    for klass in (Inheritor, Replacer, Extender):
        print('\n' + klass.__name__ + '...')
        klass().method()
    print('\nProvider...')
    x = Provider()
    x.delegate()
    
from abc import ABCMeta, abstractmethod

class Super1(metaclass=ABCMeta):
    def delegate(self):
        self.action()
    @abstractmethod
    def action(self):
        pass
    
class Sub(Super1):
    def action(self): print('spam')

X = Sub()
X.delegate()
        
       

