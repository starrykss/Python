# Self-Study 6-2
# ex06_06.py의 isStackEmpty() 함수를 없애고, 대신에 pop() 함수만으로 그 기능을 모두 구현한다.
# 실행 결과는 ex06_06.py와 동일하다.

def pop() :
    global SIZE, stack, top
    if (top == -1) :
        print("스택이 비었습니다.")
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

SIZE = 5
stack = ["커피", None, None, None, None]
top = 0

print(stack)
retData = pop()
print("추출한 데이터 -->", retData)
print(stack)
retData = pop()