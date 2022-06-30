# Self-Study 13-2
# ex13_03.py 를 수정해서 랜덤하게 0과 100000 사이의 숫자 100000개를 생성한 후 0과 1000000 사이의 숫자 하나를 랜덤하게
# 뽑아서 찾도록 코드를 작성하자. 또 몇 번 반복해서 검색에 성공하거나 실패했는지도 확인하자.

import random

## 함수 선언부
def binSearch(ary, fData) :
    global  count
    pos = -1
    start = 0
    end = len(ary) - 1

    while (start <= end) :
        count += 1
        mid = (start + end ) // 2
        if fData == ary[mid] :
            return mid
        elif fData > ary[mid] :
            start = mid + 1
        else :
            end = mid - 1

    return pos

## 전역 변수부
dataAry = [ ]
findData =  0
count = 0

## 메인 코드부
dataAry = [random.randint(0,100000) for _ in range(100000)]
dataAry.sort()
findData = random.randint(0,100000)
print('배열일부 -->', dataAry[:5], '~~~~', dataAry[-6:-1])
position = binSearch(dataAry, findData)
if position == -1 :
    print(findData,'(이)가 없네요.')
else :
    print(findData,'(은)는 ', position, '위치에 있음')
print('##', count, "회 검색함")