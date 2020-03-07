# Function 예제

# Q1. programInfo() 함수를 만들어서 다음과 같은 정보가 표시 될 수 있도록 하시오.
#   Version : 1.0
#   Update Date : 2017-01-01
#   Author : Project Python

# sol1 - my way
def programInfo():
    print('Version : 1.0')
    print('Update Date : 2017-01-01')
    print('Author : Project Python')

programInfo()

# sol2 - 모범답안
def programInfo():
    res = 'Version : 1.0\n'
    res = res + 'Update Date : 2017-01-01\n'
    res = res + 'Author : Project Python'
    return res

print(programInfo())

# Q2. 1개 이상의 정수, 실수 값을 인자로 받아 가장 큰 값 또는 가장 작은 값을 반환하는 pyMax(), pyMin()함수를 만드시오

def pyMax(*args):
    mx = args[0]
    for x in args[1:]:
        if mx < x:
            mx = x
    return mx

def pyMin(*args):
    mn = args[0]
    for x in args[1:]:
        if mn > x:
            mn = x
    return mn

# Q3. 0 ~ N까지 또는 M ~ N까지의 임의 값을 반환하는 함수를 만드시오.

from random import random

# 0 ~ N, M ~ N
def myRandom(min, max=0):
    if max == 0:
        min, max = max, min
    
    return int(random() * (max-min+1)) + min

print(myRandom(5))
print(myRandom(1,10))