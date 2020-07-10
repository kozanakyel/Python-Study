def mysum(L):
    print(L)
    if not L:        
        return 0
    else:
        return L[0] + mysum(L[1:])
mysum([1,2,3,4,5])

def mysum(L):
    return 0 if not L else L[0] + mysum(L[1:])
  
L = [1,2,3,4,5]
sum = 0
while L:
    sum += L[0]
    L = L[1:]
    
print(sum)

def sumtree(K):
    tot = 0
    for x in K:
        if not isinstance(x,list):
            tot += x
        else:
            tot += sumtree(x)
    return tot

K = [1,[2,3,[4,5,6,7]],8]
print(sumtree(K))

def echo(message):
    print(message)

def indirect(func,arg):
    func(arg)
indirect(echo,'argument!')

sc = [(echo, 'spam!'),(echo,'HAM')]
for (func,arg) in sc:
    func(arg)

L = [lambda x: x** 2,
     lambda x: x ** 3,
     lambda x: x **4]
for f in L:
    print(f(2))
    
print(L[0](3))

lower = (lambda x,y:x if x < y else y)

def action1(x):
    return (lambda y: x+y)
act = action1(99)
print(act(2))

print(list(map(pow,[1,2,3],[2,3,4])))
list(filter((lambda x: x > 0),range(-5,5)))
