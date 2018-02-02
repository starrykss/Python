import turtle as t

n = 50                  # 원을 50개 그립니다.
t.bgcolor("black")      # 배경을 검은색으로 지정합니다.
t.color("green")        # 펜 색을 녹색으로 지정합니다.
t.speed(0)              # 거북이 속도를 가장 빠르게 지정합니다.
for x in range(n):      # n번 반복합니다.
    t.circle(80)        # 현재 위치에서 반지름이 80인 원을 그립니다.
    t.left(360/n)       # 거북이가 360/n만큼 왼쪽으로 회전합니다.
