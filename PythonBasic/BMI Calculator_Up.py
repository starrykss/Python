# BMI Calculator (UPGRADED)

name = input("Name : ")
height = float(input('Height(cm) : '))
weight = float(input('Weight(kg) : '))

std_weight = (height - 100) * 0.9
BMI = weight / std_weight * 100

if BMI < 100:
    print('{}님의 BMI는 {:.2f}%로 {}입니다.'.format(name, BMI, 'Low Weight(저체중)'))
elif 100 <= BMI < 110:
    print('{}님의 BMI는 {:.2f}%로 {}입니다.'.format(name, BMI, 'Normal(정상)'))
elif 110 <= BMI < 120:
    print('{}님의 BMI는 {:.2f}%로 {}입니다.'.format(name, BMI, 'Overweight(과체중)'))
elif 120 <= BMI < 130:
    print('{}님의 BMI는 {:.2f}%로 {}입니다.'.format(name, BMI, 'Obese(비만)'))
elif 130 <= BMI:
    print('{}님의 BMI는 {:.2f}%로 {}입니다.'.format(name, BMI, 'Seriously Obese(고도비만)'))
