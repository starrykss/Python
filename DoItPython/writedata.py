# writedata.py
f = open("C:/Users/kss34/Desktop/������.txt", 'w')
for i in range(1, 11):     # 1���� 10���� i�� ����
    data = "%d��° ���Դϴ�.\n" % i
    f.write(data)          # data�� ���� ��ü f�� ���.
f.close()
