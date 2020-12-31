kor_score = [49, 79, 20, 100, 80]
math_score = [43, 59, 85, 30, 90]
eng_score = [49, 79, 48, 60, 100]
midterm_score = [kor_score, math_score, eng_score]

student_score = [0, 0, 0, 0, 0]
i = 0

for subject_score in midterm_score:
    for personal_score in subject_score:
        student_score[i] += personal_score
        i += 1
    i = 0

i = 0
for value in student_score:
    print("{0}번째 사람의 평균점수는 {1:.2f}점입니다.".format(i, value / 3))
    i += 1
