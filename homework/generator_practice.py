#######################
# Generator           # 
#######################

"""
어떠한 sequence의 접두사 (prefix)는 empty sequence를 포함하여, 
    첫번째 아이템, 첫 두 아이템 등등을 의미합니다. 
또 어떠한 sequence의 접미사 (suffix)는 empty sequence를 포함하여, 
    제일 마지막 한 아이템, 제일 마지막 두 아이템 등등을 의미합니다. 
인풋으로 받은 sequence의 접두사 (prefix), 접미사 (suffix)를 yield하는 함수를 만드세요. 
"yield" in Python Doc: https://www.python.org/dev/peps/pep-0255/ 
"""

def get_prefixes(a_sequence):
    '''
    주어진 sequence의 접두사를 반환함

        Parameters: 
            a_sequence: string 또는 한가지 타입으로 구성된 리스트

        Yields:
            접두사 하나씩을 yield함 

        Examples:
            >>> import generator_practice as gp 
            >>> a_seq1 = [1, 2, 3]
            >>> list(gp.get_prefixes(a_seq1))
            [[], [1], [1, 2], [1, 2, 3]]
            >>> a_seq2 = "abc"
            >>> list(gp.get_prefixes(a_seq2))
            ['', 'a', 'ab', 'abc']
    '''
    prefix_sequence = None
    return prefix_sequence

def get_suffixes(a_sequence):
    '''
    주어진 sequence의 접미사를 반환함

        Parameters: 
            a_sequence: string 또는 한가지 타입으로 구성된 리스트

        Yields:
            접미사 하나씩을 yield함 

        Examples:
            >>> import generator_practice as gp 
            >>> a_seq1 = [1, 2, 3]
            >>> list(gp.get_suffixes(a_seq1))
            [[1, 2, 3], [2, 3], [3], []]
            >>> a_seq2 = "abc"
            >>> list(gp.get_suffixes(a_seq2))
            ['abc', 'bc', 'c', '']
    '''
    suffix_sequence = None
    return suffix_sequence