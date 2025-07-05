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
def taxi_algorithm(start_point: str, end_point:str) ->str:
    return f"{start_point}에서 {end_point}로 택시를 타고 가는데 걸리는 시간은 300분입니다"

def ktx_algorithm(start_point: str, end_point:str) ->str:
    return f"{start_point}에서 {end_point}로 KTX를 타고 가는데 걸리는 시간은 120분입니다"

class TimeCalculator:
    def __init__(self,algorithm):
        self.algorithm = algorithm

    def calculate(self, start_point: str, end_point:str) ->str:
        return self.algorithm(start_point, end_point)

if __name__ == "__main__":
    taxi = TimeCalculator(taxi_algorithm)
    ktx = TimeCalculator(ktx_algorithm)

    print(taxi.calculate("서울", "부산"))
    print(ktx.calculate("서울", "부산"))
