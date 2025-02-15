num: int = 1 # 이렇게까진 안하는 경우도 많지만

# 이렇게 prameter와 return 값의 타입 힌트는 일반적으로 사용합니다
def repeat(message: str, times: int) -> list[str]:
	return [message] * times

print(repeat("hello", 3)) # ['hello', 'hello', 'hello']
print(repeat(1, 3))       # [1, 1, 1]
