def gen_numbers(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for i in gen_numbers(5):
    print(i)
