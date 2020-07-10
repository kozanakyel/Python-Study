import stdio

myfile = open('myfile.text')
contents = myfile.read()
print(contents)
myfile.seek(0)
lines = myfile.readlines()
print(lines)
myfile.close()
with open('myfile.text') as new_file:
    contents1 = new_file.read()
    print(contents1)
with open('myfile.text', mode='a') as f:
    f.write('\nfourth lines')
with open('myfile.text') as new_file:
    contents1 = new_file.read()
    print(contents1)
with open('galatasaray.text',mode = 'w+') as f:
    f.write('en buyuk cimbom' + str(1))
with open('galatasaray.text') as f:
    cont = f.read()
    print(cont)
