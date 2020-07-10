# Write a function that computes the volume of a sphere given its radius.
import math
def vol(rad):
    return (4*math.pi*(rad**3))/3
print(vol(2))

def ran_check(num,low,high):
    if num in range(low,high):
        print('yes it is intervals')
    return num in range(low,high)
print(ran_check(3,1,4))

import string
def up_low(sample):
    D = {'up':0,'low':0}
    for x in sample:
        if x.isupper():
            D['up'] += 1
        elif x.islower():
            D['low'] += 1
        else:
            pass
    
    print('Original string: {}'.format(sample))    
    print('Upper case char counts: ', D['up'])
    print('Lower case char counts: ', D['low'])

up_low('Bakhele kardes OLMadi böle')

def unique_list(lst):
    return list(set(lst))
print(unique_list([1,1,1,1,2,2,3,3,3,4,4,4,4,5]))

def multiply(args):
    m = 1
    for x in args:
        m *= x
    return m
print(multiply([1,2,3,4,5,-3]))
 
def is_palindrome(sample):
    return sample == sample[::-1]
print(is_palindrome('hleh'))

import string

def ispangram(str1, alphabet=string.ascii_lowercase):
    str1.lower()
    res = [a for a in alphabet]
    res1 = []
    for x in alphabet:
        if x in str1:
            res1.append(x)
    return res == res1

print(ispangram("The quick rown fox jumps over the azy dog"))
                