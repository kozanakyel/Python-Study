import random

result = random.randint(1,100)
print("WELCOME TO GUESS ME!")
print("I'm thinking of a number between 1 and 100")
print("If your guess is more than 10 away from my number, I'll tell you you're COLD")
print("If your guess is within 10 of my number, I'll tell you you're WARM")
print("If your guess is farther than your most recent guess, I'll say you're getting COLDER")
print("If your guess is closer than your most recent guess, I'll say you're getting WARMER")
print("LET'S PLAY!")

gStore = ['starting']
while True:
    gues = int(input('new Guess:... '))
    distance = abs(result - gues)
    if gues < 0 or gues > 100:
        print('index out of bounds!')
    elif distance < 11:
        print('WARM!')
        gStore.append(gues)
        break
    elif distance > 10:
        print('COLD!')
        gStore.append(gues)
        break
    elif gues == result:
        print('Congragulations! you Win in first appropriate guessing')
        break
while not result in gStore:
    gues = int(input('new Guess:... '))
    distance = abs(result - gues)
    if gues < 0 or gues > 100:
        print('index out of bounds!')
    elif gues == result:
        print('Congragulations! you Win!!')
        break
    elif distance > abs(result - gStore[-1]):
        print('COLDER!')
        gStore.append(gues)
    elif distance <= abs(result - gStore[-1]):
        print('WARMER!')
        gStore.append(gues)
print('Your prior false but appropriate guessing... ', gStore)  

    