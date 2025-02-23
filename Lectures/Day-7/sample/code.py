def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

counter_instance = counter()
print(counter_instance())  # Output: 1
print(counter_instance())  # Output: 2
print('자유 변수명 확인:',counter_instance.__code__.co_freevars)
print('자유 변수값 확인:',counter_instance.__closure__[0].cell_contents)