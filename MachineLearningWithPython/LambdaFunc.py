# Lambda 함수
'''
- 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 함
- 함수를 한 줄로 간결하게 만들 때 사용
- lambda 매개변수1, 매개변수2, ... : 매개변수를 이용한 표현식
'''

add = lambda a, b: a + b
result = add(3, 4)
print(result)   # 7

avg = lambda a: sum(a) / len(a)
result = avg([1, 2, 3])
print(result)   # 2
