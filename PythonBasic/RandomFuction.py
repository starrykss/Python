# random() : 0.0~1.0 미만의 임의의 값 생성

from random import random

print(random())               # 0.0~1.0 미만 임의의 실수형 값
print(random() * 10)          # 0.0~10.0 미만 임의의 실수형 값
print(int(random() * 10))     # 0~9까지의 임의의 정수형 값
print(int(random() * 10) + 1) # 1~10까지의 임의의 정수형 값

# randint()

from random import randint
print(randint(5, 10))   # 5~10까지의 임의의 값 생성

# randrange()

from random import randrange

print(randrange(5, 10))     # 5~10미만 까지의 임의의 값 생성
print(randrange(5, 10, 2))  # 5부터 2씩 증가된 값에 대해 10미만까지 임의 값 생

# chr() 함수를 이용한 임의의 문자 생성

from random import randint

print(chr(randint(65, 90)))     # 'A', 'Z'
print(chr(randint(97, 122)))    # 'a', 'z'
