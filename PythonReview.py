### CH1. Python 출력 함수 및 주석

# 홑 따옴표, 쌍 따옴표
print('Hello Python')       # Hello Python
print("Hello Python")      # Hello Python

# 정수 및 실수 출력
print(10)        # 10
print(11.12)   # 11.12

# 사칙연산 결과 출력
print(10 + 11)  # 21
print(12 - 13)  # -1
print(4 * 5)    # 20
print(6 / 3)    # 2
print(10 + 11, 12 - 13) # 21 -1
print(4 * 5, 6 / 3)     # 20 2

# 문자열과 정수, 실수 출력
print('10 + 11 =', 10 + 11) # 10 + 11 = 21
print('12 / 6 =', 12 / 6)   # 12 / 6 = 2

# sep(separation)
print('010', '1234', '5678', sep='-')    # 010-1234-5678
print('나이', 30, sep=':')               # 나이:30

# end
print(10, end='%')  # 10%
print(30, end='$')  # 30$

# 이스케이프 문자 : 문자열을 출력하기 위해서 사용 되는 기능 외의 부가적인 기능을 사용하기 위해서 쓰임
'''
\n : 다음 줄로 이동 (개행)
\r : 해당 줄의 처음으로 이동
\t : 8칸 공백
\' : ' 문자
\" : " 문자
\\ : \ 문자
'''

# \n
print('다음 줄에 이어서\n출력')
''' 
다음 줄에 이어서
출력
'''
print(1, 2, 3, 4, sep='\n')
'''
1
2
3
4
'''

# \r
print('다음 줄에 이어서\r출력')  # 출력 줄에 이어서
print(1, 2, 3, 4, sep='\r')    # 4

# \t
print('탭\t공백')   # 탭    공백

# \', \", \\
print('문자열에 \'홑\' 따옴표 사용')       # 문자열에 '홑' 따옴표 사용
print('문자열에 \"쌍\" 따옴표 사용')       # 문자열에 "쌍" 따옴표 사용
print('문자열에 \\역슬래쉬\\ 따옴표 사용')  # 문자열에 \역슬래쉬\ 따옴표 사용

# 한 줄 주석(Inline) : #
print('코드와 같이') # 주석 사용    # 코드와 같이

# 여러 줄 주석(Multi-line) : ''', """
""" 주석입니다.
    '''주석 안에 주석입니다.'''
"""

### CH2. Python 내장 함수

# max(), min()
max(3, 7, -1, 5, 4) # 7
min(3, 7, -1, 5, 4) # -1

# sum(), pow()
sum([2, 4, 6, 8, 10]) # 30
pow(2, 3) # 8
pow(3, 3) # 27

# divmod()
divmod(10, 3) # (3, 1)
divmod(10, 2) # (5, 0)

# 진법 표현 방법
'''
2진법 : 0b (0, 1)
8진법 : 0o (0, 1, 2, 3, 4, 5, 6, 7)
10진법  (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
16진법 : 0x (0, 1, 2, 3, 4, 5, 6, 7, 8, 9, A, B, C, D, E, F)
'''

# 진법 표현 방법
0b100 # 10진수 = 4
0o100 # 10진수 = 64
100 # 10진수 = 100
0×100 # 10진수 = 256

# 진법 변환
'''
bin() : 2진수 값으로 변환
oct() : 8진수 값으로 변환
hex() : 16진수 값으로 변환
'''
bin(100) # 0b110010
oct(100) # 0o144
hex(100) # 0x64

bin(0b100) # 0b100
oct(0b100) # 0o4
hex(0b100) # 0x4

bin(0x1A) # 0b11010
oct(0x1A) # 0o32
hex(0x1A) # 0x1A

bin(4 + 4) # 0b1000
oct(0xA + 0xB) # 0o25
hex(0b10 * 5) # 0xA

# round()
round(11.56, 1) # 11.6
round(11.12, 1) # 11.1
round(5 / 3, 3) # 1.667

# abs()
abs(-5) # 5
abs(-5) # 5

### CH3. Python 서식 문자

# 기본 서식 문자
''' (C스타일 Python3 : 설명)
%s   {}     : 문자열 출력
%d   {}     : 정수 출력
     {:b}   : 표현식 없는 2진수 값 출력
%o   {:o}   : 표현식 없는 8진수 값 출력
%x   {:x}   : 표현식 없는 16진수 값 출력
%f   {:f}   : 실수 출력
%.2f {:.2f} : 소수점 2자리 까지의 실수 출력
%6d  {:6}   : 6자리 고정 출력   
'''

# 문자열과 정수 출력 예제
print('%s : %d' % ('나이', 30))         # 나이 : 30
print('{} : {}'.format ('나이', 30))    # 나이 : 30

# 실수 출력 예제
print('%f, %.2f' % (1.123, 1.123))          # 1.123000, 1.12
print('{:f}, {:.2f}'.format(1.123, 1.123))  # 1.123000, 1.12

# 진법 출력 예제
print('%o, %x, %X' % (10, 10, 10))  # 12, a, A
print('{:b}, {:o}'.format(10, 10))  # 1010, 12
print('{:x}, {:X}'.format(10, 10))  # a, A

# 고정 길이 출력
print('|%5d|' % 123)    # |  123|                     // 숫자는 우축 기본 정렬
print('|%5s|' % 'abc')  # |  abc|                     // 문자는 우측 기본 정렬

print('|{:5}|'.format(123))     # |  123|             // 숫자는 우측 기본 정렬
print('|{:5}|'.format('abc'))   # |abc  |             // 문자는 좌측 기본 정렬

# 고정 길이의 정렬
print('|%-5d|' % 123)           # |123  |
print('|%5s|' % 'abc')          # |  abc|
print('|{:<5}|'.format(123))    # |123  |
print('|{:>5}|'.format('abc'))  # |  abc|
print('|{:^5}|'.format('abc'))  # | abc |

# 여백 채우기
print('|%05d|' % 123)           # |00123|
print('|{:_>5}|'.format('abc')) # |__abc|
print('|{:-^5}|'.format('abc')) # |-abc-|
print('|{:05}|'.format(123))    # |00123|

# 정수, 실수 단위 구분
print('{:,}'.format(1000000))       # 1,000,000
print('{:,.2f}'.format(1000000))    # 1,000,000.00

### CH4. Python 변수

# 작명 규칙
'''
1. 알파벳, 숫자, 언더스코어(_)로 구성
2. 알파벳은 대/소문자 구분
3. 한글 사용 가능
4. 변수명의 시작은 숫자로 할 수 없음
5. 공백이나 특수 기호는 포함 할 수 없음
6. Python 예약어는 사용하면 안됨
'''

# 자료형 종류
'''
1. 부울형 : True, False만을 가지는 값
2. 정수 : 0과 음수, 양수 값을 포함하는 숫자 값
3. 실수 : 소수점을 사용하는 숫자 값
4. 문자열 : 따옴표로 묶여 있는 값
5. 리스트 : 정수, 실수 및 문자열 등 자료들의 집합 (값의 집합)
6. 튜플 : 정수, 실수 및 문자열 등 자료들의 집합 (값의 집합)
7. 사전 : 정수, 실수, 및 문자열 등 자료들의 집합 (키와 값이 쌍으로 존재)
'''

# 변수 정의
'''
변수명 = 값
변수명1, 변수명2 = 값1, 값2
'''

# 자료형 확인
'''
type(변수명)
'''

# 자료형 확인
x, y, z = 10, 10.0, '10'
type(x) # <class 'int'>
type(y) # <class 'float'>
type(z) # <class 'str'>

# 자료형 관련 에러
x, y = 10, '10'
print(x + y)
'''
Traceback (most recent call last):
File "<stdin>", line 1, in <module>
TypeError: unsupported operand type(s) for +: 'int' and 'str' 
'''

# 자료형 변환
'''
bool() : 부울형 자료로 변환
int() : 정수형 자료로 변환
str() : 문자열 자료로 변환
float() : 실수형 자료로 변환
'''
x, y, z = 10, 10.0, '10'
x + int(z)  # 20
y + z       # TypeError
x + z       # TypeError

a, b = 0, ''
bool(a) # False
bool(b) # False

### CH5. Python 사용자 입력

# 사용자 입력 값 받기
input()
input('값을 입력 하시오 : ')    # 값을 입력 하시오 :

# 사용자 입력 값 변수에 저장
userin = input()
userin = input('값을 입력 하시오 : ')   # 값을 입력하시오 :

# 사용자 입력 값의 자료형
userin = input('값 입력 : ')    # 값 입력 : 
type(userin)                   # <class 'str'>

# 사용자 입력 활용
age = input('나이 : ')
name = input('이름 : ')
print('{}님의 나이는 {}세 입니다'.format(name, age)


### CH6. Python 연산자

# 산술 연산자
'''
+ : 값을 더한 결과를 반환
- : 값을 뺀 결과를 반환
* : 값을 곱한 결과를 반환
/ : 값을 나눈 결과를 반환(실수 값)
// : 값을 나눈 결과의 몫 반환(정수 값)
% : 값을 나눈 결과의 나머지 반환
** : 거듭 제곱의 결과 반환 (ex. 3**2)
'''

# 비교 연산자
'''
==  : 두 피 연산자 값을 비교하여 동일하면 True, 동일하지 않으면 False
!=  : 두 피 연산자 값을 비교하여 동일하면 False, 동일하지 않으면 True
>   : 두 피 연산자 값을 비교하여 왼쪽의 값이 크면 True, 그렇지 않으면 False
<   : 두 피 연산자 값을 비교하여 왼쪽의 값이 작으면 True, 그렇지 않으면 False
>=  : 두 피 연산자 값을 비교하여 왼쪽의 값이 크거나 같으면 True, 그렇지 않으면 False
<=  : 두 피 연산자 값을 비교하여 왼쪽의 값이 작거나 같으면 True, 그렇지 않으면 False
'''

# 논리 연산자
'''
and : 두 피 연산자가 전부 True인 경우에만 True (논리곱)
or  : 두 피 연산자가 전부 False인 경우에만 False (논리합)
not : 오른쪽 피 연산자에 대한 부정
'''

# 멤버 연산자
'''
in     : 왼쪽 피 연산자의 값이 오른쪽 피 연산자 멤버 중 일치하는 값이 존재 하면 True (ex. 1 in (1, 2, 3))
not in : 왼쪽 피 연산자의 값이 오른쪽 피 연산자 멤버 중 일치하는 값이 존재 하지 않으면 True (ex. 1 not in (1, 2, 3))
'''

# 식별 연산자
'''
is     : 두 피 연산자의 식별 값을 비교하였을 때 동일한 객체이면 True (ex. type(1) is int)
is not : 두 피 연산자의 식별 값을 비교하였을 때 동일한 객체이면 False (ex. type('1') is not int)
'''

# 비트 연산자
'''
& : 두 피 연산자의 and 비트 연산을 수행함 (ex. 10 & 5)
| : 두 피 연산자의 or 비트 연산을 수행함 (ex. 10 | 5)
^ : 두 피 연산자의 xor 비트 연산을 수행함 (ex. 10 ^ 5)
<< : 왼쪽 피 연산자의 비트를 왼쪽으로 2개 비트 이동 (ex. 10 << 2)          // X << Y : X * 2^Y
>> : 왼쪽 피 연산자의 비트를 오른쪽으로 2개 비트 이동 (10 >> 2)            // X >> Y : X / 2^Y
'''

### CH7. Python 랜덤 함수

# 0.0 ~ 1.0 미만의 임의의 값 생성
from random import random
print(random())

# 0.0 ~ 10.0 미만의 임의의 값 생성
from random import random
print(random() * 10)

# 0 ~ 10 미만의 임의의 값 생성
from random import random
print(int(random() * 10))

# 1 ~ 10 까지의 임의의 값 생성
from random import random
print(int(random() * 10) + 1)

# randint()
from random import randint
print(randint(5, 10)) # 5 ~ 10 까지의 임의 값 생성

# randrange()
from random import randrange
print(randrange(5, 10))    # 5 ~ 10 미만 까지의 임의 값 생성
print(randrange(5, 10, 2)) # 5 부터 2씩 증가 된 값에 대해 10 미만까지 임의 값 생성

# chr() 함수
from random import randint
print(chr(randint(65, 90))) # 'A', 'Z'
print(chr(randint(97, 122))) # 'a', 'z'

### CH8. Python 조건문

# 기본 사용법
'''
if 조건식 :
    (indent) 수행 코드
    수행코드
'''

# 조건 - Boolean
if True :
    print('a')  # a

if False :
    print('b')

# 조건 - 비교 연산자
x = 15
if x > 10 :
    print('x는 10보다 크다.')   # x는 10보다 크다.

# 조건 - 멤버 연산자
x = 15
if x in (10, 11, 12) :
    print('x는 10, 11, 12 중 하나에 포함 된다.')

# 조건 - 식별 연산자
x = 15
if type(x) is int :
    print('x는 int형 자료이다.')    # x는 int형 자료이다.

# 조건 - 비교, 논리 연산자
x = 15
if x > 10 and x != 15 :
    print('x는 10보다 크면서 15는 아니다.')

# if … else 문
'''
if 조건식 :
    수행 코드
else :
    수행 코드
'''
number = int(input('정수 값 입력 : '))
if x % 3 == 0 :
    print('3의 배수 이다.')
else :
    print('3의 배수가 아니다.')

# if … elif … else 문
score = int(input('점수 입력 : '))
if 90 <= score <= 100 :
    print('수 입니다.')
elif 80 <= score < 90 :
    print('우 입니다.')
elif 70 <= score < 80 :
    print('미 입니다.')
elif 60 <= score < 70 :
    print('양 입니다.')
else :
    print('가 입니다.')

# if문의 반복 사용과 다른 점
'''
if 조건식 :
    수행 코드
'''

'''
if 조건식 :
    수행 코드
else :
    수행 코드
'''

score = int(input('점수 입력 : '))
90 <= score <= 100 :
    print('수 입니다.')
if 80 <= score < 90 :
    print('우 입니다.')
if 70 <= score < 80 :
    print('미 입니다.')
if 60 <= score < 70 :
    print('양 입니다.')
else :
    print('가 입니다.')
''' 
점수 입력 : 90
수 입니다.
가 입니다.
'''

# 중첩 if 문
'''
if 조건식 :
    if 조건식 :
        수행 코드
        수행 코드
'''
score = int(input('점수 입력 : '))
if 0 <= score <= 100 :
    if 90 <= score <= 100 :
        print('수 입니다.')
    elif 80 <= score < 90 :
        print('우 입니다.')
    elif 70 <= score < 80 :
        print('미 입니다.')
    elif 60 <= score < 70 :
        print('양 입니다.')
    else :
        print('가 입니다.')
else :
    print('잘못된 입력 값 입니다.')

### CH9. Python 반복문(for)

# 기본 사용법
'''
for 변수명 in range(반복횟수) :
    수행코드
    수행코드
'''
for cnt in range(10):
    print('반복 출력')
'''
반복 출력
반복 출력
반복 출력
반복 출력
반복 출력
반복 출력
반복 출력
반복 출력
반복 출력
반복 출력
'''

for cnt in range(10):
    print('{}번째 반복'.format(cnt))
'''
0번째 반복
1번째 반복
2번째 반복
3번째 반복
4번째 반복
5번째 반복
6번째 반복
7번째 반복
8번째 반복
9번째 반복
'''

# range() 함수 응용
'''
range(종료값)
range(시작값, 종료값)
range(시작값, 종료값, 증가값)
'''
for x in range(10):
    print(x)
'''
0
1
2
3
4
5
6
7
8
9
'''

for x in range(1, 10, 2):
    print(x)
'''
1
3
5
7
9
'''

for x in range(5, 10):
    print(x)
'''
5
6
7
8
9
'''

for x in range(10, 0, -1):
    print(x, end=' ')
'''
10 9 8 7 6 5 4 3 2 1
'''

# range() 함수 대신 사용 하는 방법
for char in 'abcde' :
    print(char)
'''
a
b
c
d
e
'''

for tup in (1, 2, 3, 4, 5) :
    print(tup)
'''
1
2
3
4
5
'''

# 중첩 반복
'''
for x in range(3) : 
    for y in range(5) :
        수행 코드
        수행 코드
'''

for x in range(1, 10):
    for y in range(1, 10):
        print(x * y)

### CH10. Python 반복문(while)

# 기본 사용 법
'''
while 조건문 :
    수행 코드
    수행 코드
'''

# 비교 연산자 사용
'''
x = 0
while x < 3 :
    수행 코드
    x = x + 1
'''

# 멤버 연산자 사용
'''
x = 0
while x in (0, 1, 2) : 
    수행 코드
    x = x + 1
'''

# 무한 반복 (Ctrl + C 단축키로 강제 종료)
x = 0
while True :
    print(x)
    x = x + 1 

# 반복의 종료

x = 0
while True :
    if x % 2 == 0 :
        break
    print(x)
    x = x + 1

# 반복의 처음으로 이동
x = 0
while True : 
    if x % 2 == 0 :
        continue
    print(x)
    x = x + 1

# 중첩 반복문의 break, continue
x = 0
while True:
    while True:
        if x == 5:
            y = y + 1
            break
        x = x + 1

x = 0
while True:
    while True:
        if x == 5:
            y = y + 1
            continue
        x = x + 1

### CH11. Python 튜플

# 기본 사용법
'''
변수명 = (value1, value2, …)
변수명 = tuple([value1, value2, …])
'''

# 인덱싱 - Indexing
'''
  0   1   2   3   4   5
( 1 , 2 , 3 , 4 , 5 , 6 )
 -4  -3  -2  -1
( 1 , 2 , 3 , 4 )
'''

tup = (1, 2, 3)
print(tup)    # (1, 2, 3)
print(tup[0]) # 1
print(tup[1]) # 2

tup = (1, 2, 3)
print(tup)      # (1, 2, 3)
print(tup[-1])  # 3
print(tup[-3])  # 1

# 슬라이싱 - Slicing
'''
0  1  2  3  4  5 6
(1, 2, 3, 4, 5, 6)
-4 -3 -2 -1
 (1, 2, 3, 4)
'''

tup = (1, 2, 3)
print(tup)      # (1, 2, 3)
print(tup[0:2]) # (1, 2)
print(tup[1:3]) # (2, 3)

tup = (1, 2, 3)
print(tup)         # (1, 2, 3)
print(tup[-3:-1])  # (1, 2)
print(tup[-2:])    # (2, 3)

# 튜플 - 반복문
tup = ('a', 'b', 'c', 'd')
for idx in range(4) :
    print(tup[idx])
'''
a
b
c
d
'''

tup = ('a', 'b', 'c', 'd')
for idx in range(4) :
    print(tup[idx])

'''
a
b
c
d
'''

tup = ('a', 'b', 'c', 'd')
for val in tup :
    print(val)
'''
a
b
c
d
'''

# Packing, Unpacking
'''
변수명 = value1, value2, …
변수명1, 변수명2, … = (1, 2, …)
'''

p = (1, 2), (3, 4)  # ((1, 2), (3, 4))
x, y = p
print(x) # (1, 2)
print(y) # (3, 4)

# 2차 튜플
tup = (('a', 'b'), ('c', 'd'), ('e', 'f'))
print(tup[0])     # ('a', 'b')
print(tup[1])     # ('c', 'd')
print(tup[2][0])  # e

tup = (('a', 'b'), ('c', 'd'), ('e', 'f'))
for val in tup:
    print(val[0], val[1])
'''
a b
c d
e f
'''

tup = (('a', 'b'), ('c', 'd'), ('e', 'f'))
for val1, val2 in tup:
    print(val1, val2)
'''
a b
c d
e f
'''

# Tuple 함수
'''
count(value) : 튜플에서 일치하는 값의 수를 반환함
index(value) : 튜플에서 일치하는 값의 인덱스 번호를 반환함
'''

# count 예제
tup = (1, 2, 3, 1, 2)
tup.count(2)    # 2

# index 예제
tup = (1, 2, 3, 1, 2)
tup.index(2)    # 1

### CH12. Python 리스트

# 기본 사용법
'''
변수명 = []
변수명 = [value1, value2, …]
변수명 = list((value1, value2, …))
'''

# 인덱싱 - Indexing
'''
 0  1  2  3  4  5
[1, 2, 3, 4, 5, 6]
 -4 -3 -2 -1
[ 1, 2, 3, 4 ]
'''

lst = [1, 2, 3]
print(lst)      # [1, 2, 3]
print(lst[0])   # 1
print(lst[1])   # 2

lst = [1, 2, 3]
lst[0] = 'a'
lst[2] = lst[1] * 2
lst[1] = lst[0] * lst[2]
print(lst)  # ['a', 'aaaa', 4]

lst = [1, 2, 3]
print(lst)      # [1, 2, 3]
print(lst[-1])  # 3
print(lst[-3])  # 1

lst = [1, 2, 3]
lst[-3] = 'b'
lst[-1] = lst[1] * 2
lst[-2] = lst[0] * lst[2]
print(lst) # ['b', 'bbbb', 4]

# 슬라이싱 - Slicing
'''
0 1  2  3  4  5  6
[1, 2, 3, 4, 5, 6]
 -4 -3 -2 -1
  [1, 2, 3, 4]
'''

lst = [1, 2, 3]
print(lst)      # [1, 2, 3]
print(lst[0:2]) # [1, 2]
print(lst[1:3]) # [2, 3]

lst = [1, 2, 3]
lst[0:2] = [2, 4]
lst[1:3] = 'a', 'b'
print(lst)  # [2, 'a', 'b']

lst = [1, 2, 3]
print(lst)        # [1, 2, 3]
print(lst[-3:-1]) # [1, 2] 
print(lst[-2:])   # [2, 3]

lst = [1, 2, 3]
lst[-3:-1] = [4, 8]
lst[-2:] = 'c', 'd'
print(lst)  # [4, 'c', 'd']

# 리스트 - 반복문
lst = [1, 2, 3]
for value in lst:
    print(value)
'''
1
2
3
'''

lst = [1, 2, 3]
for idx in range(3):
    lst[idx] = lst[idx] + 1
    print(lst[idx])
'''
2
3
4
'''

lst = [1, 2, 3]
for idx in range(len(lst)):
    lst[idx] = lst[idx] + 1
    print(lst[idx])
'''
2
3
4
'''

# 2차 리스트
lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]
print(lst[0])    # ['a', 'b']
print(lst[1])    # ['c', 'd']
print(lst[2][0]) # 'e'

lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]
for val in lst :
    print(val[0], val[1])
'''
a b
c d
e f
'''

lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]
for val in lst :
    for x in val :
        print(x, end=' ')
    print()
'''
a b
c d
e f
'''

lst = [['a', 'b'], ['c', 'd'], ['e', 'f']]
for idx in range(len(lst)) :
    for idy in range(len(lst[idx])) :
        lst[idx][idy] = idx + idy
        print(lst[idx][idy], end=' ')
    print()
'''
0 1
1 2
2 3
'''

### CH13. 리스트 함수

# 리스트 함수
'''
append(value)         : 리스트 끝에 값을 추가 함
extend(iter)          : 리스트 끝에 list, tuple, dict의 값을 하나씩 추가 함
insert(idx, value)    : 특정 인덱스 위치에 값을 추가 함
pop([idx])            : 마지막 인덱스의 값을 반환 후 삭제 함
                        인덱스 번호를 지정 할 수도 있음
remove(value)         : 특정 값에 해당하는 것을 찾아 삭제 함
clear()               : 모든 값을 삭제하여 빈 리스트만 남김
count(value)          : 리스트에서 일치하는 값의 수를 반환 함
index(value)          : 리스트에서 일치하는 값의 인덱스 번호를 반환 함
reverse()             : 리스트의 모든 값을 뒤집어 나열 함
sort([reverse=False]) : 리스트의 값을 오름차순(False), 내림차순(True) 정렬 함
'''

# append 예제
lst = [1, 2, 3]
lst.append('a')
lst.append([4, 'b'])
print(lst)  # [1, 2, 3, 'a', [4, 'b']]

# extend 예제
lst = [1, 2, 3]
lst.extend(['a', 'b', 'c'])
print(lst)  # [1, 2, 3, 'a', 'b', 'c']

# insert 예제
lst = [1, 2, 3]
lst.insert(1, 'b')
print(lst)  # [1, 'b', 2, 3]

# pop 예제
lst = [1, 2, 3]
lst.pop()   # 3
lst.pop(0)  # 1
print(lst)  # [2]

# remove 예제
lst = [1, 2, 3]
lst.remove(2)
print(lst)  # [1, 3]

# clear 예제
lst = [1, 2, 3]
lst.clear()
print(lst)  # []

# count 예제
lst = [1, 2, 3, 1]
lst.count(1)    # 2

#  index 예제
lst = [1, 2, 3, 1]
lst.index(1)    # 0
lst.index(1, 1) # 3

# reverse 예제
lst = [1, 3, 2]
lst.reverse()
print(lst) # [2, 3, 1]

# sort 예제
lst = [1, 3, 2]
lst.sort()
lst.sort(reverse=True)
print(lst)  # [3, 2, 1]

### CH14. Python 사전

# 기본 사용법
'''
변수명 = {}
변수명 = {key1:value1, key2:value2, …}
변수명 = dict([(k1, v1), (k2, v2), …])
'''

# 키를 가지고 값에 접근
'''
print(dic[key])
dic[key] = value # 값 변경
'''

dic = {'a':1, 'b':2, 'c':3}
print(dic['a'])
dic['c'] = 5 * dic['b']
print(dic['c'])
print(dic)  # {'a': 1, 'b': 2, 'c': 10}

# 사전 - 반복문
dic = {'a':1, 'b':2, 'c':3}
for k in dic :
    print(k, dic[k])
'''
a 1
b 2
c 3
'''

# 사전 - 리스트
dl = {'음료':['탄산', '과일', '우유', '물'],
      '식사':['김밥', '라면', '돈까스', '비빔밥']}
for key in dl :
    print(dl[key])
'''
['탄산', '과일', '우유', '물']
['김밥', '라면', '돈까스', '비빔밥']
'''

# 리스트 - 사전
ld = [{'name':'Park', 'age':25, 'blood':'B'},
      {'name':'Kim', 'age':27, 'blood':'A'}]
for dic in ld :
    print(dic['name'], dic['age'], dic['blood'])
'''
Park 25 B
Kim 27 A
'''
# 사전 - 사전
dd = {'Park':{'age':25, 'blood':'B'},
      'Kim':{'age':37, 'blood':'A'}}
for name in dd :
    print(name, dd[name]['age'], dd[name]['blood'])
'''
Park 25 B
Kim 37 A
'''

# 사전 함수
'''
update(dict)            : 사전형 자료에 값을 추가 함
fromkeys(iter[, value]) : 리스트, 튜플에 존재하는 값을 키로 사전형 자료를 생성하여 반환함
get(key[, value])       : 사전형의 키를 통해 값을 반환 함
keys()                  : 사전형의 모든 키를 반환 함
values()                : 사전형의 모든 값을 반환 함
items()                 : 사전형의 모든 키-값의 쌍을 튜플로 반환 함
pop(key)                : 사전형의 키를 통해 값을 반환 후 삭제 함
popitem()               : 사전형의 키-값의 쌍을 튜플로 반환 후 삭제 함
clear()                 : 사전형의 모든 키-값을 삭제하여 빈 사전형 자료만 남김
'''

# update 예제
dic = {'a':1, 'b':2, 'c':3}
dic.update({'a':4, 'd':5})
print(dic)  # {'a': 4, 'b': 2, 'c': 3, 'd': 5}

# fromkeys 예제
k = ['a', 'b', 'c', 'd']
dic1, dic2 = {}, {}
dic1 = dic1.fromkeys(k)
dic2 = dic2.fromkeys(k, 1)
print(dic1) # {'a': None, 'b': None, 'c': None, 'd': None}
print(dic2) # {'a': 1, 'b': 1, 'c': 1, 'd': 1}

# get 예제
dic = {'a':1, 'b':2, 'c':3}
dic.get('b')    # 2
dic.get('d', 'Not exist key') # 'Not exist key'

# keys 예제
dic = {'a':1, 'b':2, 'c':3}
for key in dic.keys():
    print(key)
'''
a
b
c
'''

# values 예제
dic = {'a':1, 'b':2, 'c':3}
for value in dic.values():
    print(value)
'''
1
2
3
'''

# items 예제
dic = {'a':1, 'b':2, 'c':3}
for key, value in dic.items():
    print(key, value)
'''
a 1
b 2
c 3
'''

# pop 예제
dic = {'a':1, 'b':2, 'c':3}
dic.pop('b')    # 2
print(dic)      # {'a': 1, 'c': 3}

# popitem 예제
dic = {'a':1, 'b':2, 'c':3}
dic.popitem()   # ('c', 3)
print(dic)      # {'a': 1, 'b': 2}

# clear 예제
dic = {'a':1, 'b':2, 'c':3}
dic.clear()
print(dic)  # {}

### CH15. Python 문자열

# 인덱싱 - indexing
st = 'string indexing'
print(st[0])    # s
print(st[7])    # i

# 슬라이싱 - slicing
st = 'string slicing'
print(st[:6])   # string
print(st[7:])   # slicing

# 문자열 - 반복문
st = 'string for'
for x in st :
    print(x)
'''
s
t
r
i
n
g
 
f
o
r
'''

st = 'string for'
for x in st :
    print(x, end="")
'''
string for
'''
# 문자열 함수
'''
find(str)         : 문자열에서 특정 문자열을 찾아 해당 문자의 Index 값을 반환 함
count(str)        : 문자열에서 특정 문자열을 찾아 해당 문자열의 수를 반환 함
lower()           : 문자열에서 영문자를 소문자로 변경하여 반환 함
upper()           : 문자열에서 영문자를 대문자로 변경하여 반환 함
strip()           : 문자열의 앞뒤 공백을 제거함
lstrip()          : 문자열의 왼쪽 공백을 제거함
rstrip()          : 문자열의 오른쪽 공백을 제거함
replace(old, new) : 문자열의 특정 문자열을 변경함
split(str)        : 문자열의 특정 문자열을 기준으로 분리함
'''

# find 예제
st = 'python string'
print(st.find('string'))    # 7

# count 예제
st = 'python string'
print(st.count('t'))    # 2

# lower 예제
st = 'PYTHON STRING'
print(st.lower())   # python string

# upper 예제
st = 'python string'
print(st.upper())   # PYTHON STRING

# strip 예제
st = ' python string '
print(st.strip())   # python string

# lstrip 예제
st = ' python string '
print(st.lstrip())  # python string 

# rstrip 예제
st = ' python string '
print(st.rstrip())  #  python string

# replace 예제
st = 'python string'
print(st.replace('string', '문자열'))   # python 문자열

# split 예제
st = 'python string'
print(st.split(' '))    # ['python', 'string']

### CH16. Python 함수

# 함수 기본 생성 방법
'''
def 함수이름():
    수행 코드
    수행 코드
'''

# 함수의 문서화
"""
def func():
    '''함수에 대한 문서화'''
    수행 코드
    수행 코드
"""

# pass
'''
def func():
    pass
'''
# 함수의 호출
'''
def func():
    수행 코드
    수행 코드
func()
'''

'''
func() # Error      // 함수가 먼저 선언되어야 함
def func():
    수행 코드
    수행 코드
'''

# 함수 사용 예
def funcHello():
    print('Hello Python')
def funcVersion():
    print('Title : Python Programming Basic \nVersion : 1.0 Ver')
funcHello() 
funcVersion()
'''
Hello Python
Title : Pythong Programming Basic 
Version : 1.0 ver
'''

# 반환 값이 잆는 함수
'''
def func():
    retrun 반환값
func()
'''

# 반환 값 - 정수, 실수, 문자열
def funcInt():
    return 10
var = funcInt() + 10
print(var)  # 20

def funcFloat():
    return 0.1
var = funcFloat() + 10
print(var)  # 10.1

def funcStr():
    return 'string'
var = funcStr() + 'python'
print(var)  # stringpython

# 반환 값 - 튜플, 리스트, 사전
def funcTuple():
    return (1, 2, 3)
var = funcTuple()
print(var[0], var[1], var[2])   # 1 2 3

def funcList():
    return [1, 2, 3]
var = funcList()
print(var[0], var[1], var[2])   # 1 2 3

def funcDict():
    return {'a':1, 'b':2}
var = funcDict()
print(var['a'], var['b'])   # 1 2

# argument(인자)
def func(arg):
    print(arg)
func(1) # 1

def func(arg1, arg2):
    print(arg1, arg2)
func('a', 'b')  # a b
func('c')       # Error

# default argument(기본 인자)
def func(arg=1):
    print(arg)
func(5) # 5
func()  # 1

def func(arg1, arg2=2):
    print(arg1, arg2)
func(5, 10) # 5 10
func(5)     # 5 2

# keyword argument(키워드 인자)
def func(arg1, arg2):
    print(arg1, arg2)
func(5, 10)             # 5 10
func(arg2=3, arg1=1)    # 1 3

def func(arg1, arg2=1, arg3=2):
    print(arg1, arg2, arg3)
func(5, 2, 4)   # 5 2 4
func(5, arg3=4) # 5 1 4

# variable argument(가변 인자)
def func(arg, *args):
    print(arg, args)
func(1, 2, 3, 4, 5) # 1 (2, 3, 4, 5)

# keyword variable argument(키워드 가변 인자)
def func(arg, **kwargs):
    print(arg, kwargs)
func(1, key1=10, key2='a')  # 1 {'key1': 10, 'key2': 'a'}

# global 변수
a = 1
b = 2
def func():
    print(a, b)
func()      # 1 2
print(a, b) # 1 2

# local 변수
def func():
    a = 1
    b = 2
    print(a, b)
func()      # 1 2
print(a, b) # Error

# global, local
a, b = 1, 2
def func():
    a, b = 3, 4
    print(a, b)
func()      # 3 4
print(a, b) # Error