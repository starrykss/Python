# Self-Study 4-1
# ex04_07.py를 수정해서 데이터가 삭제되면서 삭제되는 위치가 출력되도록 하자.
# 예) 첫 번째 노드가 삭제되면 '첫 노드가 삭제됨'이, 중간 노드가 삭제되면 '중간 노드가 삭제됨.'이, 삭제된 노드가 없으면 '삭제된 노드가 없음'이 출력되도록 하자.

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

        print("첫 노드가 삭제됨.")
        return
    
    current = head

    # 첫 번째 외 노드 삭제
    while current.link != None:
        pre = current
        current = current.link

        if current.data == deleteData:
            pre.link = current.link
            del(current)

            print("중간 노드가 삭제됨.")
            return
        else:
            print("삭제된 노드가 없음.")

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
    