# 리스트 내포(List Comprehension)
a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)   # [3, 6, 9, 12]

a = [1, 2, 3, 4]
result = [num * 3 for num in a]  # 리스트 내포(List Comprehension)
print(result)   # [3, 6, 9, 12]

# 리스트 안에 for, if문 포함하기
a = [1, 2, 3, 4]
result = [num * 3 for num in a if num % 2 == 0]
print(result)  # [6, 12]