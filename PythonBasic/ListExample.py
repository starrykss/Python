# LIST 예제

menu = [['칼국수', 6000], 
        ['비빔밥', 5500], 
        ['돼지국밥', 7000], 
        ['돈까스', 7000], 
        ['김밥', 2000], 
        ['라면', 2500]]

# Q1. 비빔밥과, 돈까스의 가격을 출력하시오.
#sol1
print('비빔밥 가격 : {}'.format(menu[1][1]))
print('돈까스 가격 : {}'.format(menu[3][1]))

#sol2
for k, v in menu:
    if k in ('비빔밥', '돈까스'):
        print('{} 가격 : {}'.format(k, v))

# Q2. 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가하는 코드를 작성하시오.
name = input('메뉴명 : ')
price = int(input('가격 : '))
menu.append([name, price])
print(menu)

# Q3. 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가 할 때 기존에 동일한 메뉴가 존재하는 경우 가격만 변경 되도록 코드를 작성하시오.
name = input('메뉴명 : ')
price = int(input('가격 : '))
flag = 0
for idx in range(len(menu)):
    if menu[idx][0] == name:
        flag = 1
        menu[idx][1] = price
if flag == 0:
    menu.append([name, price])
print(menu)

# Q4. 메뉴를 자동으로 선택하여 출력하는 코드를 작성하시오.
from random import random
seed = int(random() * len(menu))
print('메뉴 : {} \n가격 : {}'.format(menu[seed][0], menu[seed][1]))
