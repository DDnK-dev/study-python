import functools
import time

@functools.lru_cache()
def fibonacci(n):
    if n < 2:
      return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    # check elapsed time
    start = time.time()
    print(fibonacci(100))
    print(f'Elapsed time: {time.time()-start}')