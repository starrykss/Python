# Self-Study 5-1
# ex05_07.py 를 수정해서 데이터를 찾은 경우와 찾지 못한 경우를 출력하도록 한다.
# 예로 첫 번째 노드가 찾는 데이터이면 "첫 노드에서 찾음"이, 중간 노드가 찾는 데이터이면 "중간 노드에서 찾음"이, 찾는 노드가 없으면 "찾는 노드가 없음"이 출력되도록 한다.


## 클래스와 함수 선언 부분 ##
class Node() :
    def __init__(self) :
        self.data = None
        self.link = None

def printNodes(start) :
    current = start
    if current.link == None:
        return
    print(current.data, end = ' ')

    while current.link != start :
        current = current.link
        print(current.data, end = ' ')
    print()

def findNode(findData) :
    global memory, head, current, pre

    current = head
    if current.data == findData :
        print("# 첫 노드에서 찾음 #")
        return current
    while current.link != head :
        current = current.link
        if current.data == findData :
            print("# 중간 노드에서 찾음 #")
            return current
    print("# 찾는 노드가 없음 #")
    return Node()    # 빈 노드 반환

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__":
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

    fNode = findNode("다현")
    print(fNode.data)

    fNode = findNode("쯔위")
    print(fNode.data)

    fNode = findNode("상순")
    print(fNode.data)