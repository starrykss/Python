# adddata.py
f = open("C:/Users/kss34/Desktop/������.txt", "a")
for i in range(11, 20):
    data = "%d��° ���Դϴ�.\n" % i
    f.write(data)
f.close()
