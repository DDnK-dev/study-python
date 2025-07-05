"""
data = [1, 2, 3, 4, 5]
for i in data:
    print(i)
"""

"""
name = ['Tom', 'Jerry', 'Mike', 'John']
score = [90, 30, 70, 80]
aa = list(zip(name,score))
new = sorted(aa, key=lambda x: x[1])
print(new[2][0])
"""

score = [90, 30, 70, 80, 50, 60, 40, 20, 10, 100, 90, 80, 70, 60, 50, 40, 30, 20, 0, 10]
for i, name in enumerate(score):
    number =
    a = list(zip(i,score[i]))
b = sorted(a, key= lambda x: x[1])
answer = b[-1][1]
print(answer)