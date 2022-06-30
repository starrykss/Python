# Self-Study 6-1
# ex06_04.py의 isStackFull() 함수를 없애고, 대신에 push() 함수만으로 그 기능을 모두 구현한다.
# 실행 결과는 ex06_04.py와 동일하다.

def push(data) :
    global SIZE, stack, top
    if (top >= SIZE - 1):
        print("스택이 꽉 찼습니다.")
        return

    top += 1
    stack[top] = data

SIZE = 5
stack = ["커피", "녹차", "꿀물", "콜라", None]
top = 3

print(stack)
push("환타")
print(stack)
push("게토레이")