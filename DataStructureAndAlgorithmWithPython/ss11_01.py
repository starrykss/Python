# Self-Study 11-1
# ex11-01.py 를 수정해서 최댓값 위치를 찾도록 코드를 작성하자.

def findMaxIdx(ary) :
    minIdx = 0
    for i in range(1, len(ary)) :
        if (ary[minIdx] < ary[i]) :
            minIdx = i
        return minIdx

testAry = [55, 88, 33, 77]
minPos = findMaxIdx(testAry)
print('최댓값 -->', testAry[minPos])