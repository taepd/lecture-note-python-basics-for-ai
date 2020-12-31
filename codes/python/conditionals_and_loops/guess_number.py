import random

guess_number = random.randint(1, 100)
user_input = 999
counter = 0

print("숫자를 맞춰보세요(1 ~ 100)")
# Loop
while user_input != guess_number:
    user_input = int(input("숫자를 입력하세요"))
    counter += 1

    if user_input == guess_number:
        print("정답!!")
        print("당신은 {} 입력하셨습니다.".format(counter))

    # 1) 크면 크다고 알려준다
    elif user_input > guess_number:
        print("입력된 숫자가 큽니다. DOWN!")

    # 2) 작으면 작다고 알려준다.
    elif user_input < guess_number:
        print("입력된 숫자가 작습니다. UP!")

print("프로그램이 종료되었습니다.")
