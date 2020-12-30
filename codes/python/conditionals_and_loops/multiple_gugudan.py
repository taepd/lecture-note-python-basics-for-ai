def print_x_dan(dan):
    for x in range(1, 10):
        result = dan * x
        print("{} X {} = {}".format(dan, x, result))


while True:
    user_input = input("구구단 몇 단을 계산까요(1~9)")
    if user_input == "0":
        print("구구단 게임을 종료합니다")
        break
    if user_input not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        print("잘못입력하셨습니다")
    print_x_dan(int(user_input))
