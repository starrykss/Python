# 원형 연결 리스트의 구현

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

def insertNode(findData, insertData) :
    global memory, head, current, pre

    if head.data == findData :    # 첫 번째 노드 삽입
        node = Node()
        node.data = insertData
        node.link = head
        last = head                     # 마지막 노드를 첫 번째 노드로 우선 지정
        while last.link != head:        # 마지막 노드를 찾으면 반복 종료
            last = last.link            # last를 다음 노드로 지정
        last.link = node                # 마지막 노드의 링크에 새 노드 지정
        head = node
        return

    current = head
    while current.link != head:     # 중간 노드 삽입
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            return
    
    node = Node()       # 마지막 노드 삽입
    node.data = insertData
    current.link = node
    node.link = head

def deleteNode(deleteData) :
    global memory, head, current, pre

    if head.data == deleteData :    # 첫 번째 노드 삭제
        current = head
        head = head.link
        last = head
        while last.link != current :    # 마지막 노드를 찾으면 반복 종료
            last = last.link            # last를 다음 노드로 변경
        last.link = head                # 마지막 노드의 링크에 head가 가리키는 노드 지정
        del(current)
        return
    
    current = head      # 첫 번째 외 노드 삭제
    while current.link != head :
        pre = current
        current = current.link
        if current.data == deleteData :    # 중간 노드를 찾았을 때
            pre.link = current.link
            del(current)
            return

def findNode(findData) :
    global memory, head, current, pre

    current = head
    if current.data == findData :
        return current
    while current.link != head :
        current = current.link
        if current.data == findData :
            return current
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

    # 삽입 예
    insertNode("다현", "화사")
    printNodes(head)

    insertNode("사나", "솔라")
    printNodes(head)

    insertNode("지민", "문별")
    printNodes(head)

    # 삭제 예
    deleteNode("다현")
    printNodes(head)

    deleteNode("쯔위")
    printNodes(head)

    deleteNode("지효")
    printNodes(head)

    deleteNode("지민")
    printNodes(head)

    # 검색 예
    fNode = findNode("다현")
    print(fNode.data)

    fNode = findNode("쯔위")
    print(fNode.data)

    fNode = findNode("지민")
    print(fNode.data)