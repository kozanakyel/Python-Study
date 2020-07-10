def lesser_of_two_evens(a,b):
    if a%2 == 0 and b%2 == 0:
        return min(a,b)
    else:
        return max(a,b)
    
print(lesser_of_two_evens(2,5))

def animal_crackers(text):
    L = text.split(' ')
    return L[0][0].lower() == L[1][0].lower()

print(animal_crackers('Level llama'))

def makes_twenty(a,b):
    return a == 20 or b == 20 or sum((a,b)) == 20

print(makes_twenty(1,8))

def old_macdonald(name):
    out = []
    for x in range(len(name)):
        if x == 0 or x == 3:
            out.append(name[x].upper())
        else:
            out.append(name[x])
    return ''.join(out)      
    
print(old_macdonald('macdonald'))

def master_yoda(text):
    out = list(text.split(' '))
    out = out[::-1]
    return ' '.join(out)
        
print(master_yoda('ı am home'))

def almost_there(n):
    return n in range(90,111) or n in range(190,211)

print(almost_there(209))

def has_33(liste):
    for x in range(len(liste)):
        if liste[x] == 3 and liste[x + 1] == 3:
            return True
        else:
            return False
    
print(has_33([3,1,3]))

def paper_doll(text):
    result = ''
    for x in range(len(text)):
        result += 3*text[x]
    return result

print(paper_doll('missiipiii'))

def blackjack(a,b,c):
    if a+b+c <= 21:
        return sum((a,b,c))
    elif 11 in (a,b,c):
        return sum((a,b,c)) - 10
    else:
        return 'BUST'
    
print(blackjack(9,9,11))

def summer_69(arr):
    total = 0
    for x in arr:
        if not 6 in arr:
            total += x            
        else:
            for y in range(len(arr)):
                if arr[y] == 6:
                    first = y
                elif arr[y] == 9:
                    last = y
            del arr[first:last+1]
    return sum(arr)  
            
print(summer_69([2,1,6,9,11]))
                
def spy_game(nums):
    zeroK = []
    
    for x in range(len(nums)):
        if not zeroK and nums[x] == 0:
            zeroK.append(0)
            first0 = x
        elif zeroK and nums[x] == 0:
            last0 = x
        elif nums[x] == 7:
            seven = x
    return seven > first0 and seven > last0       

print(spy_game([1,0,4,5,2,7,0]))  
    
    