# 단순 연결 리스트의 노드 삽입 함수

## 클래스와 함수 선언 부분 ##
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = ' ')
    while current.link != None:
        current = current.link
        print(current.data, end = ' ')
    print()

# 노드 삽입 함수
def insertNode(findData, insertData):
    global memory, head, current, pre

    # 첫 번째 노드 삽입
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        return
    
    current = head

    # 중간 노드 삽입
    while current.link != None:
        pre = current
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            return

    # 마지막 노드 삽입
    node = Node()
    node.data = insertData
    current.link = node

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = ["다현", "정연", "쯔위", "사나", "지효"]

## 메인 코드 부분 ##
if __name__ == "__main__":
    # 첫 번째 노드
    node = Node() 
    node.data = dataArray[0]
    head = node
    memory.append(node)

    # 두 번째 이후 노드
    for data in dataArray[1:]:
        pre = node
        node = Node()
        node.data = data
        pre.link = node
        memory.append(node)
    
    printNodes(head)

    insertNode("다현", "화사")
    printNodes(head)

    insertNode("사나", "솔라")
    printNodes(head)

    insertNode("상순", "문별")    # 존재하지 않는 데이터인 상순 노드 앞에 문별 노드를 삽입한 후 출력 (맨 마지막에 삽입)
    printNodes(head)