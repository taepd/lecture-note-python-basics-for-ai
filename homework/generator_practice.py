#######################
# Generator           # 
#######################

"""
1. 어떠한 sequence의 접두사 (prefix)는 empty sequence를 포함하여, 첫번째 아이템, 첫 두 아이템 등등을 의미합니다. 
또 어떠한 sequence의 접미사 (suffix)는 empty sequence를 포함하여, 제일 마지막 한 아이템, 제일 마지막 두 아이템 등등을 의미합니ㅏㄷ. 
인풋으로 받은 sequence의 접두사 (prefix), 접미사 (suffix)를 yield하는 함수를 만드세요. 

>>> list(prefixes([1, 2, 3]))
[[], [1], [1, 2], [1, 2, 3]]
>>> list(suffixes([1, 2, 3]))
[[1, 2, 3], [2, 3], [3], []]

 >>> list(prefixes("abc"))
 ['', 'a', 'ab', 'abc']
 >>> list(suffixes("abc"))
 ['abc', 'bc', 'c', '']
"""