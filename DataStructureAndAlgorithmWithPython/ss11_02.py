# Self-Study 11-2
# ex11_05.py를 수정해서 랜덤하게 0~200 사이의 숫자 10개를 생성한 후, 내림차순으로 정렬하도록 코드를 작성하자. (실행 결과는 실행할 때마다 다름.)

import  random
## 함수 선언부
def findInsertIdx(ary, data) :
    findIdx = -1  # 초기값은 없는 위치로
    for i in range(0, len(ary)) :
        if (ary[i] < data) :    # 내림차순 정렬
            findIdx = i
            break
    if findIdx == -1 : # 큰값을 못찾음 == 제일 마지막 위치
        return len(ary)
    else :
        return findIdx

## 전역 변수부
before = []
after = []

## 메인 코드부
before = [random.randint(0,200) for _ in range(10)]
print('정렬 전 -->', before)
for i in range(len(before)) :
    data = before[i]
    insPos = findInsertIdx(after, data)
    after.insert(insPos, data)
print('정렬 후 -->', after)