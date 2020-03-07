# DICTIONARY 예제

# Q1. 다음의 메뉴와 가격을 Key와 Value로 사용하여 사전형 자료를 만드시오. (변수명은 menu)
#     칼국수(6000원), 비빔밥(5000원), 돼지국밥(7000원), 돈까스(7000원), 김밥(2000원), 라면(2500원)

menu = {'칼국수':6000, '비빔밥':5500, 
        '돼지국밥':7000, '돈까스':7000, 
        '김밥':2000, '라면':2500}

# Q2. 위에서 만든 사전형 자료 menu 변수에서 가격이 6000원 미만에 해당하는 메뉴와 가격을 출력하는 코드를 작성하시오.

# sol1)
for k, v in menu.items():
    if v < 6000:
        print('{} : {}'.format(k, v))

# sol2)
for key in menu.keys():
    if menu[key] < 6000:
        print('{} : {}'.format(key, menu[key]))

# Q3. 사용자 입력으로 메뉴와 가격을 입력 받아 menu 변수에 자료를 추가할 수 있도록 하시오. (동일한 메뉴는 가격만 변경)

name = input('메뉴명 : ')
price = int(input('가격 : '))

menu.update({name:price})
print(menu)

# Q4. 메뉴를 자동으로 선택하여 출력하는 코드를 작성하시오.

from random import random

key = tuple(menu.keys()) 
seed = int(random() * len(key))

print('{} : {}'.format(key[seed], menu[key[seed]]))