score = int(input())
grade = ""

if score >= 90:
    print("In 90")
    grade = "a"
elif score >= 80:
    print("In 80")
    grade = "b"
elif score >= 70:
    print("In 70")
    grade = "c"
elif score >= 60:
    print("In 60")
    grade = "d"
else:
    print("Under 60")
    grade = "f"

print(grade)
