# Self-Study 5-2
# ex05_08.py를 수정해서 랜덤하게 -100~100 숫자 중 7개를 뽑고(중복 허용), 이번에는 양수와 음수의 개수를 센다.
# 그리고 양수는 음수로, 음수는 양수로 변경한다.
# 0은 양수도 음수도 아닌 것으로 간주한다.

import random

## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__(self) :
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current.link == None :
        return
    print(current.data, end = ' ')
    while current.link != start :
        current = current.link
        print(current.data, end = ' ')
    print()

def countOddEven() :
    global memory, head, current, pre

    odd, even = 0, 0
    if head == None :
        return False
    current = head
    while True :
        if current.data % 2 == 0 :
            even += 1
        else :
            odd += 1
        if current.link == head :
            break
        current = current.link

    return odd, even

def makeZeroNumber(odd, even) :
    if odd > even :
        reminder = 1
    else :
        reminder = 0
    
    current = head
    while True :
        current.data *= -1
        
        if current.link == head :
            break
        current = current.link

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None

## 메인 코드 부분 ##
if __name__ == "__main__":
    dataArray = []
    for _ in range(7) :
        dataArray.append(random.randint(-100, 100))

    node = Node()
    node.data = dataArray[0]    # 첫 번째 노드
    head = node
    node.link = head
    memory.append(node)

    for data in dataArray[1:] :    # 두 번째 이후 노드
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        node.link = head
        memory.append(node)
    
    printNodes(head)
    
    oddCount, evenCount = countOddEven()
    print('홀수 -->', oddCount, '\t', '짝수 -->', evenCount)

    makeZeroNumber(oddCount, evenCount)
    printNodes(head)