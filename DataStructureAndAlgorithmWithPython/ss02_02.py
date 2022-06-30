# Self Study 2-2
# 4행 3열짜리 리스트를 생성한 후, 12~3을 입력하고 출력해 보자.
# 추가로 배열의 모든 숫자 합계도 계산해보자.

myList1 = []
myList2 = []
value = 12
tot = 0

for i in range(0, 4):
    for k in range(0, 3):
        myList1.append(value)
        tot += value
        value -= 1
    myList2.append(myList1)
    myList1 = []

for i in range(0, 4):
    for k in range(0, 3):
        print("%3d" % myList2[i][k], end = " ")
    print(" ")

print("배열의 합계 ==> %d" % tot)