# 게시판 페이징하기


# m : 게시물의 총 건수
# n : 페이지당 보여줄 게시물 수

def getTotalPage(m, n):
    result = 0
    if m % n == 0:
        result = m / n
    else:
        result = m / n + 1

    return result

print(getTotalPage(30, 10))
