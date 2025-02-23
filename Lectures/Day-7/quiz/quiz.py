"""
Quiz 1.

각 fibonacci 함수의 호출 시간을 출력하는 데코레이터를 작성하시오.
이때, 함수의 이름은 function_name, 함수의 호출 시간은 elapsed_time으로 출력하시오.
데코레이터의 이름은 timer로 하시오.
"""

def fibonacci(n):
    if n < 2:
      return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(10))
