hash_table = [0 for i in range(11)]
hash_table2 = [0 for j in range(11)]

def save_oa(key, value):
    index = hash(key) % len(hash_table)

    # index(key의 주소)부터 hash_table끝까지 선형 탐색
    for i in range(index, len(hash_table)):

        # 빈 공간이면 데이터 저장
        if hash_table[i] == 0:
            hash_table[i] = [key, value]
            return

        # 빈 공간이 아니고, 데이터의 key값이 같다면, 업데이트
        elif hash_table[i][0] == key:
            hash_table[i][1] = value
            return

def save_sc(key, value):
    # 임의의 해시함수
    index = hash(key) % len(hash_table2)

    # 만약 해시함수값(index)의 버킷이 이미 찼다면
    if hash_table2[index] != 0:

        # 해당 버킷에 링크드 리스트가 구현되어 있을 수도 있고,
        # 그 안에 해당 key값이 이미 저장되어 있을 수 있으니 찾아본다.
        for data in hash_table2[index]:
            if data[0] == key:
                data[1] = value  # 이미 저장되어 있다면 업데이트
                return

        # 처음 저장하는 데이터라면 뒤에 붙여준다.
        return hash_table2[index].append([key, value])

    # 애초에 빈 버킷이었다면 2차원 리스트(링크드 리스트 흉내)로 버킷 업데이트
    hash_table2[index] = [[key, value]]
    return

key_candidates = ['a','b','c','d','e','f','g','h']

for i in range(7):
    save_oa(key_candidates[i], hash(key_candidates[i]) % len(hash_table))
    save_sc(key_candidates[i], int(hash(key_candidates[i]) % len(hash_table2)))
print(hash_table)
print(hash_table2)
