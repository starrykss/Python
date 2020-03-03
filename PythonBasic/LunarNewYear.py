# 윤년(Lunar New Year)
# 4의 배수는 윤년, 그 외는 평년
# 4의 배수이면서 100의 배수는 평년, 그 외는 윤년
# 4 그리고 100의 배수이면서 400의 배수인 경우 윤년, 그 외는 평년

year = int(input('연도 : '))

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('{}년은 {}입니다.'.format(year, '윤년'))
        else:
            print('{}년은 {}입니다.'.format(year, '평년'))

    else:
        print('{}년은 {}입니다.'.format(year, '윤년'))
else:
    print('{}년은 {}입니다.'.format(year, '평년'))