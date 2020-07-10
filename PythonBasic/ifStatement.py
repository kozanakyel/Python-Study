answer = '20'
b = int(answer)**2
print(b)

for all in [(1,2,3,4),(5,6,7,8)]:
    a,b,c = all[0],all[1:3],all[3]
    print(a,b,c)
a = b = []
b.append(42)
print(a,b)

L = [1,2]
L =  L + [3]
L.append(4)

L = [1,2]
M = L
L = L + [3,4]
print(L,M)

L += [3,4]
print(L, M)
#L = L.sort()
sorted(L)
print(L)

x=1
y=2
z=3
log = open('data.bin','w')
print(x,y,z,sep='')
print(x,y,z,end='');print(x,y,z)
print(x,y,x, sep='...',file = log)
log.close()
print(open('data.bin').read())

choice = 'ham'
print({'spam':1.25,
       'ham':1.99,
       'eggs':0.99}[choice])

x = 'SPAM'
if 'rubbery' in 'shrubbery':
    print(x * 8)
    x += 'NI'
    if x.endswith('NI'):
        x *= 2
        print(x)

while True:
    reply = input('Enter text: ')
    if reply == 's':break
    elif not reply.isdigit():   
        print('Bad!' * 8)
    else:
        num = int(reply)
        if num < 20:
            print('low')
        else:    
            print(num ** 2)
print('Bye')