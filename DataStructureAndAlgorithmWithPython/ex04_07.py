# 단순 연결 리스트의 노드 삭제 함수

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

# 노드 삭제 함수
def deleteNode(deleteData):
    global memory, head, current, pre

    # 첫 번째 노드 삭제
    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return
    
    current = head

    # 첫 번째 외 노드 삭제
    while current.link != None:
        pre = current
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

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

    deleteNode("다현")
    printNodes(head)

    deleteNode("쯔위")
    printNodes(head)
    
    deleteNode("지효")
    printNodes(head)
    
    deleteNode("상순")
    printNodes(head)
    