f = open("yesterday.txt", "r")
yesterday_lyric = ""
while True:
    line = f.readline()
    if not line:
        break
    yesterday_lyric = yesterday_lyric + line.strip() + "\n"
f.close()

n_of_yesterday = yesterday_lyric.upper().count("YESTERDAY")  # 대소문자 구분 제거
print("Number of a Word 'YESTERDAY'", n_of_yesterday)
