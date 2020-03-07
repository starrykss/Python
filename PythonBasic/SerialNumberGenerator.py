# Serial Number Generator [8 digits/16 digits]

from random import randint

print('{:-^19}'.format('8 digits'))
#1
for x in range(1, 81):
    if x % 8 == 0:
        print(chr(randint(97, 122)))
    else:
        print(chr(randint(97, 122)), end='')

print('{:-^19}'.format('-'))

#2
for x in range(10):
    for y in range(8):
        st = randint(97, 122)
        print(chr(st), end='')
    print()

print('{:-^19}'.format('16 digits'))

for x in range(10):
    for y in range(16):
        z = randint(0, 2)
        if z == 0:
            st = randint(0, 9)
            print(st, end = '')
        elif z == 1:
            st = randint(65, 90)
            print(chr(st), end = '')
        elif z == 2:
            st = randint(97, 122)
            print(chr(st), end = '')
    print()
