print([(x,y) for x in (1,2,30) for y in (3,2,4) if x != y])
vec = [-2, 2, -4, 0, 2]
print([x*2 for x in vec if x < 0])
print([(x,x**2) for x in range(6)])
vec1 = [[1,2,3,],[4,5,6],[7,8,9]]
print([n for el in vec1 for n in el])
del vec1[0:2]
singleton ='spam',
print(len(singleton))
a = set('abracadabra')
b = set('alacazam')
print(a^b)