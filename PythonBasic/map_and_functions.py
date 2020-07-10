def square(num):
    return num**2


my_nums = [1,2,3,4,5]

print(map(square, my_nums))
for item in map(square, my_nums):
    print(item)
print(list(map(square, my_nums)))

def splicer(mystring):
    if len(mystring)%2 == 0:
        return 'EVEN'
    else:
        return mystring[0]
names = ['ali', 'uğur','kamil']
print(list(map(splicer,names)))


def check_even(num):
    return num%2 == 0
mynums = [1,2,3,4,5,6]
print(filter(check_even,mynums))
print(list(filter(check_even,mynums)))

for n in filter(check_even,mynums):
    print(n)
    
squar = lambda num: num ** 2

print(square(5))

print(list(map(lambda num:num**2,mynums)))
print(list(filter(lambda num:num%2 == 0,mynums)))

#GLOBAL
name = 'Global'

def greet():
    #ENCLOSING
    #name = 'Sammy'
    def hello():
        #LOCAL
        #name = 'Local'
        print('hello ' + name)
    hello()
greet()

def intersect(a,b):
    res = []
    for x in a:
        if x in b:
            res.append(x)
    return res
print(intersect([1,2,3],(1,4)))

def f1():
    X = 88
    def f2():
        print(X)
    return f2

action = f1()
action()

def func1():
    x = 4
    action = (lambda n: x**n)
    return action

x = func1()
print(x(2))

def makeActions():
    acts = []
    for i in range(5):
        acts.append(lambda x: i**x)
        return acts
    
acts = makeActions()
print(acts[0](2))

X='Spam'
def func2():
    global X
    X = 'NI'
    print(X)
    
func2()
print(X)

import sys
print(sys.path)