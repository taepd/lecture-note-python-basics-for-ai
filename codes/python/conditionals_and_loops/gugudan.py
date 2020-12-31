print("구구단 몇 단을 계산할까요?")
dan = int(input())

if dan < 2 or dan > 9:
    print("하기 싫군요!!!")
else:
    print("구구단 {} 단을 계산합니다.".format(dan))
    for idx in range(1, 10):
        print(dan, "X", idx, "=", dan * idx)
