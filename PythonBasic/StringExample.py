# 문자열 예제

# Q1. 다음 조건을 보고 회원가입을 위한 프로그램 코드를 작성하시오.
#   - 아이디는 반드시 10자리 이상
#   - 패스워드는 반드시 8 ~ 16자리 사이
#   - 패스워드에 아이디가 포함되면 안됨
#   - 패스워드에는 다음의 특수 문자가 반드시 하나 이상 포함 (~, !, @, #, $, %, ^, &, *, _, ?)

# sol1 - my way
chars = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '?']
count = 0

while True:
    id = input('ID(10자리 이상): ')
    if len(id) < 10:
        print('잘못된 ID입니다!')
        continue
    else:
        print('ID가 설정되었습니다.')
        break

while True:
    pw = input('PW(8~16자리) : ')
    if 8 <= len(pw) <= 16:
        if pw.count(id) >= 1:
            print('잘못된 PW입니다!')
        else:
            for v in chars:
                if pw.count(v) >= 1:
                    count = count + 1

            if count != 0:
                print('PW가 설정되었습니다.')
                break
            else:
                print('잘못된 PW입니다!')
    else:
        print('잘못된 PW입니다!')

print('\n당신의 ID : {}'.format(id))
print('당신의 PW : {}'.format(pw))

# sol2 - 모범답안
# 10자리 이상 입력한 경우에만 가입 승낙
while True:
    username = input('아이디 입력 : ')
    if len(username) < 10:
        print('아이디는 반드시 10자리 이상 입력하시오.')
    else:
        break

# 8자리 이상 16자리 이하
# 패스워드에 아이디는 포함하지 않는다.
# 패스워드에 반드시 특수문자 포함
while True:
    password = input('패스워드 입력 : ')
    if 8 <= len(password) <= 16:
        if username not in password:
            # 특수문자 ~!@#$%^&*_?
            chk = 0
            for s in '~@#$%^&*_?':
                if s in password:
                    chk = 1
                    break
            if chk == 0:
                print('패스워드에는 특수문자가 하나 이상 포함 되어야 합니다.')
            else:
                break
        else:
            print('아이디가 패스워드에 포함되면 안됩니다.')
    else:
        print('패스워드는 반드시 8자리 이상 16자리 이하로 구성되어야 합니다.')        