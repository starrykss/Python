import turtle as t

angle = 89              # 거북이가 왼쪽으로 회전할 각도를 지정합니다(값을 바꿀 수 있음).
t.bgcolor("black")      # 배경색을 검은색으로 지정합니다.
t.color("yellow")       # 펜 색을 노란색으로 지정합니다.
t.speed(0)              # 거북이 속도를 가장 빠르게 지정합니다.
for x in range(200):    # x 값을 0에서 199까지 바꾸면서 200번 실행합니다.
    t.forward(x)        # x 만큼 앞으로 이동합니다.
    t.left(angle)       # 거북이가 왼쪽으로 89도 회전합니다.
