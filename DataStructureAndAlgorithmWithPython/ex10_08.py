# N제곱 계산을 재귀 호출로 구현

tab = ''
def pow(x, n) :
	global tab
	tab += '	'
	if  n == 0 :
		return 1
	print(tab+"%d*%d^(%d-%d)" % (x, x, n, 1))
	return x * pow (x, n-1)

print('2^4')
print('답 -->', pow(2, 4))
