# Decimal to Binary

integer = 1

while integer != 0:
    integer = int(input('Integer(END : 0) : '))
    print('Binary : {}'.format(bin(integer)))

#2

num = int(input('Integer : '))
res = ''

while True:
    Q = num % 2
    num = num // 2
    res = str(Q) + res
    if num == 0:
        print(res)
        break