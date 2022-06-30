# Self-Study 10-2
# ex10_07.py 를 수정해서 각 단이 세로로 나오도록 코드를 작성하자.

def gugu(dan, num) :
    print("%dx%d=%2d" % (dan, num, dan * num), end = '  ')
    if dan < 9:
        gugu(dan + 1, num)

for num in range(1, 10) :
    gugu(2, num)
    print()