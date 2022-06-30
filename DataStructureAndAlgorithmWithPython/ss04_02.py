# Self-Study 4-2
# ex04_09.py 를 수정해서 전화번호 대신에 dataArray에 키를 사용하자.
# 그리고 키 순서대로 단순 연결 리스트를 생성하자.
# dataArray = [["지민", 180], ["정국", 177], ["뷔", 183], ["슈가", 175], ["진", 179]]

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

def makeSimpleLinkedList(namePhone):
    global memory, head, current, pre
    printNodes(head)

    node = Node()
    node.data = namePhone
    memory.append(node)

    # 첫 번째 노드일 때
    if head == None:
        head = node
        return
    
    # 첫 번째 노드보다 작을 때
    if head.data[1] > namePhone[1]:    # 키 순서대로
        node.link = head
        head = node
        return
    
    # 중간 노드로 삽입하는 경우
    current = head
    while current.link != None:
        pre = current
        current = current.link
        if current.data[1] > namePhone[1]:    # 키 순서대로
            pre.link = node
            node.link = current
            return
        
    # 삽입할 노드가 가장 큰 경우
    current.link = node

## 전역 변수 선언 부분 ##
memory = []
head, current, pre = None, None, None
dataArray = [["지민", 180], ["정국", 177], ["뷔", 183], ["슈가", 175], ["진", 179]]

## 메인 코드 부분 ##
if __name__ == "__main__":
    for data in dataArray:
        makeSimpleLinkedList(data)
    
    printNodes(head)