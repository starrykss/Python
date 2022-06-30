# Self Study 3-1
# ex03_03.py 를 수정하여 입력한 위치 이후가 모두 삭제되도록 하자.

katok = ['다현', '정연', '쯔위', '사나', '지효']

# 선형 리스트에서 데이터를 삭제하는 함수
def new_delete_data(position):
    if position < 0 or position > len(katok):
        print("데이터를 삭제할 범위를 벗어났습니다.")
        return
    
    kLen = len(katok)

    # 방법 1
    """
    for i in range(kLen - 1, position - 1, -1):
        katok.pop(i)   
    """

    # 방법 2
    katok[position] = None
    for i in range(position + 1, kLen):
        katok[i - 1] = katok[i]
        katok[i] = None
    
    for j in range(kLen - 1, position - 1, -1):
        katok.pop(j)


new_delete_data(1)
print(katok)
new_delete_data(3)
print(katok)