# Self-Study 7-1
# ex07_04.py의 isQueueFull() 함수를 없애고, 대신에 enQueue() 함수 안으로 그 기능을 모두 구현한다.

def enQueue(data) :
    global SIZE, queue, front, rear
    if (rear == SIZE-1) :
        print("큐가 꽉 찼습니다.")
        return
    rear += 1
    queue[rear] = data

SIZE = 5
queue = ["화사", "솔라", "문별", "휘인", None]
front = -1
rear = 3

print(queue)
enQueue("선미")
print(queue)
enQueue("재남")