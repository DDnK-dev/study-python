"""
1번문제
def solution(nums):
    num = len(nums)
    kind = len(set(nums))
    if kind <= num/2:
        answer = kind
    else:
        answer = num/2
    return answer
"""


"""
2번문제
from collections import Counter
def solution(participant, completion):
    one = Counter(participant) - Counter(completion)
    answer = list(one.elements())[0]
    return answer      
"""