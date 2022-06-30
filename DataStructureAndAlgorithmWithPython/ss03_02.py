# Self Study 3-2
# ex03_05.py 의 printPoly() 함수를 수정해서 계수가 0인 항은 출력되지 않도록 하자.
# 또 첫 번째 항의 + 부호도 출력되지 않도록 한다.

## 함수 선언 부분
def printPoly(p_x):
    term = len(p_x) - 1     # 최고차항 숫자 = 배열 길이 - 1
    polyStr = "P(x) = "

    for i in range(len(px)):
        coef = p_x[i]       # 계수

        if coef != 0:
            if (coef >= 0) and (term != len(p_x) - 1):
                polyStr += "+"
            polyStr += str(coef) + "x^" + str(term) + " "
            term -= 1

    return polyStr

def calcPoly(xVal, p_x):
    retValue = 0
    term = len(p_x) - 1     # 최고사항 숫자 = 배열 길이 - 1

    for i in range(len(px)):
        coef = p_x[i]       # 계수
        retValue += coef * xVal ** term
        term -= 1

    return retValue

## 전역 변수 선언 부분
px = [7, -4, 0, 5]      # =7x^3 - 4x^2 + 0x^1 + 5x^0

## 메인 코드 부분 ##
if __name__ == "__main__":
    pStr = printPoly(px)
    print(pStr)

    xValue = int(input("X 값--> "))

    pxValue = calcPoly(xValue, px)
    print(pxValue)