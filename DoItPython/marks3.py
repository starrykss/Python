# marks3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue   # ������ 60�� �̸��̸� �� ó������ ���ư���.
    print("%d�� �л� �����մϴ�. �հ��Դϴ�." % (number+1))
