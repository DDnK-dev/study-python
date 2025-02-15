import sys

def my_print():
    print("hello world")

print(hex(id(my_print))) # 함수객체 주소
print(sys.getrefcount(my_print)) # 함수 객체의 레퍼런스 카운트
print(sys.getsizeof(my_print)) # 함수 객체의 사이즈
print(my_print.__annotations__) # 함수 객체의 어노테이션
print(type(my_print)) # 함수 객체의 타입 == class 'function'

def taxi_algorithm(start_point: str,end_point: str) -> str:
    return f"{start_point}에서 {end_point}로 택시를 타고 가는데 걸리는 시간은 300분 입니다."

def ktx_algorithm(start_point: str,end_point: str) -> str:
    return f"{start_point}에서 {end_point}로 KTX를 타고 가는데 걸리는 시간은 120분 입니다."

class TimeCalculator:
    def __init__(self,algorithm):
        self.algorithm = algorithm

    def calculate(self,start_point: str,end_point: str) -> str:
        return self.algorithm(start_point,end_point)

def main():
    taxi = TimeCalculator(taxi_algorithm)
    ktx = TimeCalculator(ktx_algorithm)

    print(taxi.calculate("서울","부산"))
    print(ktx.calculate("서울","부산"))
main()
