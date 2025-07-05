"""
Quiz 1.

각 fibonacci 함수의 호출 시간을 출력하는 데코레이터를 작성하시오.
이때, 함수의 이름은 function_name, 함수의 호출 시간은 elapsed_time으로 출력하시오.
데코레이터의 이름은 timer로 하시오.
"""
import functools
import time


def timer(function):
    @functools.wraps(function)
    def put_function(n):
        print(f'{put_function.__name__}')
        start_time = time.time()
        function(n)
        elapsed_time = time.time() - start_time
        return elapsed_time
    return put_function

@ timer
def fibonacci(n):
    if n < 2:
      return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    print(fibonacci(10))
