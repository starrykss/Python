# marks1.py
marks = [90, 25, 67, 45, 80]  # �л����� ���� ���� ����Ʈ
number = 0                    # �л����� �ٿ� �� ��ȣ
for mark in marks:            # 90, 25, 67, 45, 80�� ������� mark�� ����
    number = number + 1
    if mark >= 60:
        print("%d�� �л��� �հ��Դϴ�." % number)
    else:
        print("%d�� �л��� ���հ��Դϴ�." % number)
