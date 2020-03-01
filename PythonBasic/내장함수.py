## 내장함수

# (1) 크기 비교 함수
# max(), min() : 최댓값과 최솟값
print(max(3, 7, -1, 5, 4)) # 7
print(min(3, 7, -1, 5, 4)) # -1

# (2) 연산 함수
# sum(), pow() : 총합과 거듭제곱값
print(sum([2, 4, 6, 8, 10])) # 30
print(pow(2, 3))             # 8
print(pow(3, 3))             # 27

# divmod() : 몫(div)과 나머지(mod)
print(divmod(10, 3))    # (3, 1)
print(divmod(10, 2))    # (5, 0)

# (3) 진법 변환 함수
#
# 진법 표현 방법
#
# 진법            표현 문자                표현식
# 2  | 0,1                              | 0b   ; Binary
# 8  | 0,1,2,3,4,5,6,7                  | 0o   ; Octal
# 10 | 0,1,2,3,4,5,6,7,8,9              |
# 16 | 0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F  | 0x   ; heXadecimal
#

print(0b100) # 10진수 = 4
print(0x100) # 10진수 = 64
print(100)   # 10진수 = 100
print(0x100) # 10진수 = 256

# 진법 변환
# bin() : 2진수 값으로 변환
# oct() : 8진수 값으로 변환
# hex() : 16진수 값으로 변환

print(bin(100))   # 0b110010
print(oct(100))   # 0o144
print(hex(100))   # 0x64
print(bin(0b100)) # 0b100
print(oct(0b100)) # 0o4
print(hex(0b100)) # 0x4
print(bin(0x1A))  # 0b11010
print(oct(0x1A))  # 0o32
print(hex(0x1A))  # 0x1A
print(bin(4 + 4)) # 0b1000
print(oct(0xA + 0xB)) # 0o25
print(hex(0b10 * 5))  # 0xA

# (4) 그 외 함수
# round() : 반올림
print(round(11.56, 1)) # 11.6      ; 소수 첫째짜리까지 표현해라.
print(round(11.12, 1)) # 11.1
print(round(5 / 3, 3)) # 1.667

# abs() : 절댓값
print(abs(-5))  # 5
