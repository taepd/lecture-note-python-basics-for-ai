birth_year = int(input("당신의 태어난 년도를 입력해 주세요 : "))

age = 2021 - birth_year + 1

message = ""

if 20 <= age and age <= 26:
    message = "대학생"
elif 17 <= age and age < 20:
    message = "고등학생"
elif 14 <= age and age < 17:
    message = "중학생"
elif (8 <= age) and (age < 14):
    message = "초등학생"
else:
    print("학생이 아닙니다.")

print(message)
