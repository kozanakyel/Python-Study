
class Number:
    def __init__(self,start):
        self.data = start
    def __sub__(self,other):
        return Number(self.data - other)
    
class Indexer:
    data = [5,6,7,8,9]
    def __getitem__(self,index):
        print('getitem: ',index)
        return self.data[index]
    
    def __setitem__(self,index,value):
        self.data[index] = value
        
        
X = Indexer()
print(X[2])

L = [5, 6, 7, 8, 9]
print(L[slice(2, 4)])
print(L[2:4])

class stepper():
    def __getitem__(self, i):
        return self.data[i]
    
A = stepper()
A.data = "spam"
print(A[1])
for item in A:
    print(item, end=' ')
    
print('p' in A)
print([c for c in A])
print(list(map(str.upper,A)))

print(list(A),tuple(A), ''.join(A))

