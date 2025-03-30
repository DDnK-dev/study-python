def coroutine_processor():
    """데이터를 받아 평균을 계산하는 코루틴"""
    total = 0
    count = 0
    try:
        while True:
            data = yield  # 데이터를 받음
            if data is None:  # 종료 신호
                print("코루틴 종료.")
                yield  # StopIteration 방지
                break
            total += data
            count += 1
            print(f"받은 값: {data}, 현재 평균: {total / count}")
    except GeneratorExit:
        print("코루틴이 종료되었습니다.")

# 사용 예시
coro = coroutine_processor()
next(coro)  # 코루틴 초기화

for value in [10, 20, 30, 40, 50]:
    coro.send(value)

coro.send(None)  # 종료 신호 전송