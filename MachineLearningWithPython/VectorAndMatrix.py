### 벡터와 행렬

## 벡터(Vector)

# Numpy 이용
'''
- 파이썬에서 벡터나 행렬을 처리하기 위한 라이브러리
- import numpy as np
- 벡터는 1차원 배열로 처리 가능
- 요소의 참조 및 수정은 List와 동일
'''
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print(x + y) # (5, 7, 9)

type(x)  # numpy.ndarray

# 연속된 정수 벡터의 생성
print(np.arrange(10))       # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(np.arrange(5, 10))    # [5, 6, 7, 8, 9]

# ndarray형의 주의점 : ndarray는 값을 복사하지 않고 주소를 전달 (C++의 Call By Reference와 비슷함)
a = np.array([1, 1])    # a = [1, 1]
b = a                   # b = [1, 1] (call by reference)
b[0] = 2                # b = [2, 1], a = [2, 1] (call by reference)
print(a[0])             # 2

a = np.array([1, 1])    # a = [1, 1]
b = a.copy()            # b = [1, 1] (벡터 a의 값을 벡터 b에 복사)
b[0] = 2                # b = [2, 1], a = [1, 1] 
print(a[0])             # 1


## 행렬(Matrix)

# ndarray의 2차원 배열로 정의
import numpy as np

x = np.array([1, 2, 3], [4, 5, 6])
print(x)   
'''
[[1 2 3] 
 [4 5 6]]
'''
x.shape # (2, 3) : 행렬의 사이즈 출력
h, w = x.shape
print(h, w) # 2 3

# 요소의 참조 및 수정
print(x[1, 2]) # 6
x[0, 2] = 10   # x = [[1 2 10], [4 5 6]]

# 요소가 0과 1인 ndarray 만들기
print(np.zeros(10))     # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0,]
print(np.zeros((2, 3))) 
'''
[[0, 0, 0,]
 [0, 0, 0,]]
'''
print(np.ones(10))  # [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

# 요소가 랜덤인 행렬 생성
x = np.random.rand(2, 3)    # 0~1 사이의 랜덤 수
print(x)
'''
[[0.2321323 0.3323213  0.0231232]
 [0.9532042 0.21321394 0.9542131]]
'''

y = np.random.randn(2, 3)   # 0~1 사이의 정규 분포(Normal Distribution)
print(y)
'''
[[-0.213213 1.213123 1.21323123]
 [ 0.123213 1.12132 -1.31232133]]
'''

z = np.random.randint(-3, 3, (2, 3)) # -3~2 사이의 랜덤 수
print(z)
'''
[[2 -3 -3]
 [2  2  1]]
'''

# 크기 변경
a = np.arange(10)
print(a)    # [0 1 2 3 4 5 6 7 8 9]

a.reshape(2, 5)
'''
array([0, 1, 2, 3, 4],
      [5, 6, 7, 8, 9])
'''

# 사칙 연산
x = np.array([1, 1, 1], [2, 2, 2])
y = np.array([3, 3, 3], [4, 4, 4])
z = x + y
print(z)
'''
[[4 4 4]
 [6 6 6]]
'''

print(z * 10)
'''
[[40 40 40]
 [60 60 60]]
'''

# 산술 함수 : exp(), sqrt(), log(), round(), mean(), std(), max(), min()
x = np.array([1, 2, 3], [4, 5, 6])
print(np.exp(x))

# 행렬의 곱셈 : dot()
v = np.array([1, 2, 3], [4, 5, 6])
w = np.array([[1, 1], [2, 2], [3, 3]])
print(v.dot(w))
'''
[[14 14]
 [32 32]]
'''


## 슬라이싱
'''
- 변수명[:n], 변수명[n:] : 0~n-1, n~끝
- 변수명[n1:n2]         : n1~n2-1
- 변수명[n1:n2:dn]      : n1~n2-1까지 dn 간격으로 참조
- 변수명[::-1]          : reverse
'''

# 1차원 이상
y = np.array([1, 2, 3], [4, 5, 6], [7, 8, 9])
print(y)
print(" ")
print(y[:2, 1:2])
'''
[[1 2 3]
 [4 5 6]
 [7 8 9]]

[[2]
 [5]]
'''


## 조건을 이용한 데이터 수정
x = np.array([1, 1, 2, 3, 5, 8, 13])
b = x > 3
print(b)    # [False False False False  True  True  True]

x[x > 3]    # array([ 5,  8, 13])

x[x > 3] = 999
print(x)    # [  1   1   2   3 999 999 999]

y = x[x > 100]
print(y)    # [999 999 999]