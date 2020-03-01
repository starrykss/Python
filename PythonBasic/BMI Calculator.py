# BMI Calculator

name = input('Input Name. : ')
height = float(input('Input Height.(cm) : '))
weight = float(input('Input Weight.(kg) : '))

std_weight = (height - 100) * 0.9
BMI = weight / std_weight * 100

print('The BMI of {} is {:.2f}%.'.format(name, BMI))
