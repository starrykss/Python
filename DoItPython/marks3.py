# marks3.py
marks = [90, 25, 67, 45, 80]
for number in range(len(marks)):
    if marks[number] < 60: continue   # 점수가 60점 미만이면 맨 처음으로 돌아간다.
    print("%d번 학생 축하합니다. 합격입니다." % (number+1))
