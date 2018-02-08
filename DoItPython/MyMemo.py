# 간단한 메모장 만들기

# C:/Python/memo.py
import sys

option = sys.argv[1]

if option == '-a':      # -a : 메모 추가
    memo = sys.argv[2]
    f = open('memo.txt', 'a')
    f.write(memo)
    f.write('\n')
    f.close()
elif option == '-v':    # -v : 메모 출력
    f = open('memo.txt')
    memo = f.read()
    f.close()
    print(memo)
