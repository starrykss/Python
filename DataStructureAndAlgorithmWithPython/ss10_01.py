# Self-Study 10-1
# ex10_03.py 를 수정해서 두 수를 입력받고 숫자 사이의 합계를 구하는 코드를 작성하자. 단, 입력하는 숫자는 작은 숫자 또는 큰 숫자 중 어느 것을 먼저 입력해도 같다.

def addNumber(num1, num2) :
    if num2 <= num1 :
        return num1
    return num2 + addNumber(num1, num2 - 1)

num1 = int(input('숫자1-->'))
num2 = int(input('숫자2-->'))

if num1 > num2 :
    num1, num2 = num2, num1
print(addNumber(num1, num2))