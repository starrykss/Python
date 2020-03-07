# Dictionary(사전)

# 사전의 키 자료형으로는 정수형, 실수형, 문자, 튜플만 가능하다.
dic = {1:'a', 2:'b'}        # 정수형
dic = {1.1:'a', 2.1:'b'}    # 실수형
dic = {'a':1, 'b':2}        # 문자
dic = {(1,):'a', (2,):'b'}  # 튜플

dic = {[1,]:'a', [2,]:'b'}  # ERROR

# 사전의 값 자료형은 모든 자료형이 가능하다.
dic = {1:'a', 2:3, 3:2.3, 4:[1], 5:(1,)}

# 사전-반복문
dic = {'a':1, 'b':2, 'c':3}
for k in dic:
    print(k, dic[k])

# 사전-리스트
dl = {'음료':['탄산', '과일', '우유', '물'], '식사':['김밥', '라면', '돈까스', '비빔밥']}

for key in dl:
    print(dl[key])

# 리스트-사전
ld = [{'name':'park', 'age':25, 'blood':'B', {'name':'kim', 'age':27, 'blood':'A'}}]

for dic in ld:
    print(dic['name'], dic['age'], dic['blood'])

# 사전-사전
dd = {'Park':{'age':25, 'blood':'B'}, 'Kim':{'age':37, 'blood':'A'}}

for name in dd:
    print(name.dd[name]['age'], dd[name]['blood'])