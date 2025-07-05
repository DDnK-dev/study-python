import functools

def  is_multiple(x):
    def  my_decorator(func):
        @functools.wraps(func) # 추가 됐다
        def  my_func(*args, **kwargs):
            result = func(*args, **kwargs)
            print(f'function name : {my_func.__name__}')
            if result %x == 0:
                print(f"{x}'s multiple number!")
            else:
                print(f"{x}'s non-multiple number!")
            return result 
        return my_func
    return my_decorator

@is_multiple(2)
def  add(a, b):
    sum = a+b
    print(f"sum : {sum}")
    return sum

print(add(2,  1)) 
print(add(10,  22))