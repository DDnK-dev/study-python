a = [('동해',1), ('물과',2),('백두',3),('산이',4)]
dic_1, dic_2 = {}, {}

# for 문을 사용하는 방법
for i,j in a:
	dic_1[i] = j

# dictcomp를 이용하는 방법 (더 빠르다)
dic_2 = {i:j for i,j in a}

print(dic_1)
print(dic_2)

d = {"one": 1, "two": 2, "three": 3}

# 같은 키를 쓰면 값을 업데이트 할 수 있다
d["one"]=11 # 11로 업데이트

# update를 사용해 한번에 업데이트가 될 수 있다 (없으면 추가)
d.update({'two': 22, 'three': 33, 'four': 44})

print(d)
