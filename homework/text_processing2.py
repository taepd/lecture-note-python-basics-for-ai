#######################
# Test Processing II  # 
#######################

"""
1. 인풋으로 받은 스트링에서 숫자만 추출하여 단어로 반환하는 함수를 적어보세요. 
반환하는 단어들은 영어 소문자여야 하며, 띄어쓰기 한칸으로 나눠져야 합니다. 
만약 인풋 스트링에서 숫자가 존재하지 않는 다면, 빈 문자열 (empty string)을 반환하세요. 

>>> digits_to_words("Zip Code: 19104")
'one nine one zero four'
>>> digits_to_words("Pi is 3.1415...")
'three one four one five'
"""

def digits_to_words(string):
    pass 

"""
2. 컴퓨터 프로그래밍에 많은 명명 규칙이 있지만, 두 규칙이 특히 흔히 쓰입니다. 
첫번째로는, 변수 이름을 'underscore'로 나눠준다거나, (ex. mixed_case_variable)
두번째로는, 변수 이름을 대소문자 구별해 구분자 (delimiter)없이 쓰는 경우가 있습니다. 
이 경우에는 첫번째 단어는 소문자로, 그 후에 오는 단어들의 첫번째 글자들은 대문자로 쓰입니다 (ex. camelCaseVariable). 

이 문제에서 첫번째 규칙에서 두번째 규칙으로 변환하는 함수를 적어보세요. 
* 앞과 뒤에 여러개의 'underscore'는 무시해도 됩니다. 
* 만약 어떤 변수 이름이 underscore로만 이루어 진다면, 빈 문자열만 반환해도 됩니다. 

>>> to_mixed_case("to_mixed_case")
'toMixedCase'
>>> to_mixed_case("__EXAMPLE__NAME__")
'exampleName'
"""

def to_mixed_case(string):
    pass