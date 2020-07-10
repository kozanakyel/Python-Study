ord('s')
res = []
for x in 'spam':
    res.append(ord(x))
print(res)
res = list(map(ord,'spam'))
res = [ord(x) for x in 'spam']

list(filter((lambda x: x%2==0),range(5)))
a = [x+y for x in 'spam' for y in'SPAM']

M = [[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

N = [[2, 2, 2],
 [3, 3, 3],
 [4, 4, 4]]

[[M[row][col] * N[row][col]] for row in range(3) for col in range(3)]

def gensquares(N):
    for i in range(N):
        yield i ** 2
        
for i in gensquares(5):
    print(i, end=' : ')
    
x = gensquares(4)

for x in [n**2 for n in range(5)]:
    print(x, end=' : ')
    
for x in map((lambda n: n**2), range(5)):
    print(x, end=' : ')
    
def gen():
    for i in range(10):
        x = yield i
        print(x)
G = gen()
print(next(G))
G.send(77)

S1 = 'abc'
S2 = 'xyz123'
b=list(zip(S1,S2))
print(b)

c = list(zip([-2,-1,0,1]))
print(c)

d = list(zip([1,2,3],[2,3,4,5,6,7,8,]))
print(d)

e = list(map(abs, [-2,-1,0,1,2,3,4]))
print(e)

def mymap(func,*seq):
    res = []
    for args in zip(*seq):
        res.append(func(*args))
    return res

def mymap(func,*seq):
    return [func(*args) for args in zip(*seq)]

def myzip(*seq):
    seqs = [list(S) for S in seqs]
    res = []
    while all(seqs):
        res.append(tuple(S.pop(0) for S in seqs))
    return res

dict((x,x*x) for x in range(10))
set(x*x for x in range(10))

res = set()
for x in range(10):
    res.add(x*x)
    
res = {}
for x in range(10):
    res[x] = x*x
print(res)    
print(res)

import time
reps = 1000
repslist = range(reps)

def timer(func,*pargs,**kargs):
    start = time.clock()
    for i in replist:
        ret = func(*pargs,**kargs)
    elapsed = time.clock() - start
    return (elapsed, ret)



