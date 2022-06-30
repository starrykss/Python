# Self-Study 13-1
# ex13_01.py 를 수정해서 중복된 데이터가 여러 개 있을 때, 위치 여러 개를 리스트로 만들어 반환하도록 코드를 변경하자.
# 코드 중 dataAry와 findData는 다음과 같이 변경한다.
# dataAry = [188, 50, 150, 168, 50, 162, 105, 120, 177, 50]
# findData = 50

## 함수 선언 부분 ## 
def seqSearch(ary, fData) :
    pos = -1
    size = len(ary)
    print('## 비교한 데이터 ==> ', end = '')
    for i in range(size) :
        print(ary[i], end = ' ')
        if ary[i] == fData :
            pos = i
            break
    print()
    return pos

## 전역 변수 선언 부분 ## 
dataAry = [188, 150, 168, 162, 105, 120, 177, 50]
findData = 0

## 메인 코드 부분 ## 
findData = int(input('* 찾을 값을 입력하세요. --> '))
print('배열 -->', dataAry)
position = seqSearch(dataAry, findData)
if position == -1 :
    print(findData, '(이)가 없네요.')
else :
    print(findData,'(은)는 ', position, '위치에 있음')
