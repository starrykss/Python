# Self Study 2-1
# 100과 20의 더하기, 빼기, 곱하기, 몫, 나머지, 제곱이 출력되도록 프로그램을 구현하자.

def multi(v1, v2):
    retList = []
    retList.append(v1 + v2)    # append()의 매개변수는 1개만 올 수 있다.
    retList.append(v1 - v2)
    retList.append(v1 * v2) 
    retList.append(v1 / v2)
    retList.append(v1 % v2)
    retList.append(v1 ** v2)

    return retList[0], retList[1], retList[2], retList[3], retList[4], retList[5]    # 파이썬에서는 값을 여러 개 반환하는 문법을 허용한다.

if __name__ == "__main__":
    print("multi()에서 반환한 값 ==> [%d, %d, %d, %d, %d, %d]" % multi(100, 20))