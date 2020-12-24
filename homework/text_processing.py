#######################
# Test Processing I   # 
#######################

"""
NLP에서 흔히하는 전처리는 소문자 변환, 앞뒤 필요없는 띄어쓰기를 제거하는 등의 텍스트 정규화 (text normalization)입니다. 
이번 숙제에서는 텍스트 처리 방법을 파이썬으로 배워보겠습니다. 
"""

"""
1. 인풋으로 받는 스트링을 정규화하는 함수를 적어보세요. 아래의 요건들을 충족시켜야합니다. 
   * 모든 단어들은 소문자로 되어야합니다.
   * 띄어쓰기는 한칸으로 되어야합니다. 
   * 앞뒤 필요없는 띄어쓰기는 제거해야합니다. 
   
>>> normalize("This is an example.")
'this is an example.'
>>> normalize("   EXTRA   SPACE   ")
'extra space'
"""

def normalize(string):
    pass 


"""
2. 인풋으로 받은 스트링에서 모든 모음 (a, e, i, o, u)를 제거시킨 스트링을 반환하는 함수를 적어보세요. 

>>> no_vowels("This Is An Example.")
'Ths s n xmpl.'
>>> no_vowels("We love Python!")
'W lv Pythn!'
"""

def no_vowels(string):
    pass

