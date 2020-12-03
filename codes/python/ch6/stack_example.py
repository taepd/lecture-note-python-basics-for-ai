word = input("Input a word : ")
word_list = list(word)
# print(word_list)
for _ in range(len(word_list)):
    print(word_list.pop())
    print(word_list)
