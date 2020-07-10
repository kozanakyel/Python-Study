L = [1,2]
b = L
b[0] = 'spam'
print(L)

def multiple(x,y):
    x = 2
    y = [3,4]
    return x, y
x = 1
L = [1,2]
x,L = multiple(x,L)
print(x,L)

#ARGUMETS
def kwonly(a,*b,c):
    print(a,b,c)
    
kwonly(1,2,c=3)

def k2(a,*b,c=6,**d): print(a,b,c,d)

print(k2(1,2,3,x=4,y=5))

def f(a,c=6,*b,**d): print(a,b,c,d)
print(f(1,2,3,x=4))

def min1(*args):
    res = args[0]
    for arg in args[1:]:
        if arg < res:
            res = arg
    return res
def min2(first, *res):
    for arg in rest:
        if arg < first:
            first = arg
    return first
def min3(*args):
    tmp = list(args)
    tmp.sort()
    return tmp[0]

print(min1(3,4,1,2))

def minmax(test,*args):
    res = args[0]
    for arg in args[1:]:
        if test(arg,res):
            res = arg
    return res
def lessthan(x,y): return x < y
def grtrthan(x,y): return x > y

print(minmax(lessthan,4,2,1,5,6,3))
print(minmax(grtrthan,4,2,1,5,6,3))

def intersect(*args):
    res = []
    for x in args[0]:
        for other in args[1:]:
            if x not in other: break
        else:
            res.append(x)
    return res
def union(*args):
    res = []
    for seq in args:
        for x in seq:
            if not x in res:
                res.append(x)
    return res