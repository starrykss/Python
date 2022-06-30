# Self-Study 8-2
# ex08_04.py를 수정해서 nameAry에 잇지의 여자친구를 추가하자. 그리고 검색할 이름을 input() 함수로 입력받은 후 검색하도록 하자.
## 찾을 그룹이름-->잇지
## 잇지 을(를) 찾았음.
## 찾을 그룹이름-->소녀시대
## 소녀시대 이(가) 트리에 없음.

## 함수 선언부
class TreeNode() :
    def __init__ (self) :
        self.left = None
        self.data = None
        self.right = None

## 전역 변수 선언부
memory = []
root = None
nameAry = ['블랙핑크', '레드벨벳', '마마무', '에이핑크',  '걸스데이', '트와이스', '잇지',
           '여자친구']

## 메인 코드부
node = TreeNode()
node.data = nameAry[0]
root = node
memory.append(node)

for name in nameAry[1:] :

    node = TreeNode()
    node.data = name

    current = root
    while True :
        if name < current.data :
            if current.left == None :
                current.left = node
                break
            current = current.left
        else :
            if current.right == None:
                current.right = node
                break
            current = current.right

    memory.append(node)


findName = input('찾을 그룹이름-->')

current = root
while True:
    if findName == current.data:
        print(findName, '을(를) 찾았음.')
        break
    elif findName < current.data :
        if current.left == None :
            print(findName, '이(가) 트리에 없음')
            break
        current = current.left
    else:
        if current.right == None :
            print(findName, '이(가) 트리에 없음')
            break
        current = current.right