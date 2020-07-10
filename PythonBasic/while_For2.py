items = ["aaa", 111, (4,5), 2.01]
tests = [(4,5), 3.14]

for key in tests:
    for item in items:
        if item == key:
            print(key, "was found")
            break
    else:
        print(key, "not found")

for key in tests:
    if key in items:
        print(key, "was found")
    else:
        print(key, "not found")
        
seq1 = "spam"
seq2 = "scam"
res = []
for x in seq1:
    if x in seq2:
        res.append(x)
print(res)

#File Scanners
file = open('test.txt','w')
file.write('galataray 23 champions\n fener 34 champions')
file.close()

file = open('test.txt','r')
print(file.read())

file = open('test.txt')
while True:
    line = file.readline()
    if not line: break
    print(line, end='')
    
for char in file.read():
    print(char)
    
S = 'lldfshkjjbsıubd'
list(range(0,len(S),2))

for i in range(0, len(S), 2): print(S[i], end=' ')

#better way
for c in S[::2]: print(c, end=' ')
# Error use range():  for b in len(S): print(b)

#ZIP items and for loops
L1 = [1,2,3,4]
L2 = [5,6,7,8]
print(list(zip(L1,L2)))
for (x,y) in zip(L1,L2):
    print(x,y,'--',x+y)
     
S1 = 'abc'
S2 = 'xyz123'
zip1 = list(zip(S1,S2))
print(zip1)

S = 'spam'
offset = 0
for item in S:
    print(item,'appears at offset',offset)
    offset += 1
#better way
for offset, item in enumerate(S):
    print(item, 'appears at offset', offset)
E = enumerate(S)
for e in range(len(S)):
    print(next(E))

for line in open('test.txt'):
    print(line.upper(), end=' ')

#Use for, .split(), and if to create a Statement
    #that will print out words that start with 's':
st = 'Print only the words that start with s in this sentence'
for x in st.split(' '):
    if x.startswith('s'):
        print(x)

#Use range() to print all the even numbers from 0 to 10.
for x in range(11):
    if x % 2 == 0:
        print(x)
        
#Use a List Comprehension to create a list of all
        #numbers between 1 and 50 that are divisible by 3.
L = [a for a in range(51) if a % 3 == 0]
print(L)

#Go through the string below and if
#the length of a word is even print "even!"
st = 'Print every word in this sentence that has an even number of letters'
for x in st.split(' '):
    if len(x) % 2 == 0:
        print(x, 'even')

#Write a program that prints the integers from 1 to 100. But for
        #multiples of three print "Fizz" instead of the number,
        #and for the multiples of five print "Buzz".
        #For numbers which are multiples of both three and five print "FizzBuzz".
for x in range(100):
    if x % 3 == 0 and x % 5 == 0:
        print('FizzBuzz')
    elif x % 3 == 0:
        print('Fizz')
    elif x % 5 == 0:
        print('Buzz')
    else:
        print(x)
        
#Use List Comprehension to create a list of the first letters of every word in the string below:
st = 'Create a list of the first letters of every word in this string'
L = [x[0] for x in st.split(' ') ]
print(L)
    







