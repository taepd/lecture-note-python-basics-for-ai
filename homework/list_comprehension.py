#######################
# List Comprehension  # 
#######################

def concatenate(any_sequence):
    """
    인풋으로 받은 연속적인 배열 (sequence) 안의 아이템들을 하나의 list로 연결시키는 함수를 적으세요. 
    이 함수는 한줄을 넘지 않는 single list comprehension으로 적어야합니다. 

        Parameters:
            any_sequence (list): 여러가지 다양한 type으로 구성된 list
            ex - [[1, 2], [3, 4]], ["abc", (0, [0])]
        
        Returns:
            concatenated_list (list): 배열안에 있는 모든 아이템들이 하나씩 풀어진 list
        
        Examples:
            >>> import list_comprehension as lc
            >>> any_seq = [[1, 2], [3, 4]]
            >>> lc.concatenate(any_seq)
            [1, 2, 3, 4]
            >>> any_seq2 = ["abc", (0, [0])]
            >>> concatenate(any_seq2)
            ['a', 'b', 'c', 0, [0]]
            >>> any_seq2 = ["abc", (0, [0], [0, 0])]
            ['a', 'b', 'c', 0, [0], [0, 0]]
    """
    concatenated_list = None
    return concatenated_list