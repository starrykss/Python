# Self-Study 7-2
# ex07_06.py의 isQueueEmpty() 함수를 없애고, 대신에 deQueue() 함수 안으로 그 기능을 모두 구현한다.

def deQueue() :
    global SIZE, queue, front, rear
    if (front == rear) :
        print("큐가 비었습니다.")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
    return data

SIZE = 5
queue = ["화사", None, None, None, None]
front = -1
rear = 0

print(queue)
retData = deQueue()
print("추출한 데이터 -->", retData)
print(queue)
retData = deQueue()