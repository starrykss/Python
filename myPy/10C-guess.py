import random

n = random.randint(1, 30)       # 1~30 사이에 있는 임의의 수를 뽑습니다.

while True:                     # 영원히 반복합니다.
    x = input("맞혀 보세요? ")
    g = int(x)                  # 입력받은 값을 비교할 수 있도록 정수로 바꿉니다.
    if g == n:
        print("정답")
        break                   # 정답을 맞히면 break로 while 반복 블록을 빠져 나갑니다.
    if g < n:
        print("너무 작아요.")
    if g > n:
        print("너무 커요.")
