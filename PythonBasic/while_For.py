
x = 10
while x:
    x -= 1
    if x % 2 == 0: 
        print(x, end=' ')
while True:
    name = input('Enter name: ')
    if name == 's':break
    age = input('Enter age: ')
    print('hello', name, '=>', int(age) ** 2)

    
g = [1,2,3]
for num in g:
    pass
print('no error')

T = [(1,2),(3,4),(5,6)]
for a,b in T: print(a,b)

D = {'a':1,'b':2,'c':3}
for key in D:
    print(key, '=>',D[key])

for key,value in D.items(): print(key,'=>',value)

for both in T:
    a, b = both
    print(a,b)
for ((a,b),c) in [((1,2),3),((4,5),6)]:
    print(a,b,c)

    