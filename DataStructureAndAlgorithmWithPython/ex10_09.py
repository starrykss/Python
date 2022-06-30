# 배열의 합계를 재귀 호출로 구현 (실행 결과는 실행할 때마다 다름.)

import random

def arySum(arr, n) :
	if n <= 0 :
		return arr[0]
	return arySum(arr, n-1) + arr[n]

ary = [random.randint(0, 255) for _ in range(random.randint(10, 20))]
print(ary)
print('배열 합계 -->', arySum(ary, len(ary)-1))
