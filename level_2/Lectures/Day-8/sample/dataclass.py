from dataclasses import dataclass, field
import random


# isbn 생성함수
def generate_isbn():
    # 13자리 숫자 생성
    return "".join([str(random.randint(0, 9)) for _ in range(13)])

@dataclass
class Book:
    language = "Learn Err Day"  # 클래스 변수
    # writer = field(init=False)    # 이렇게 초기화 하지 않고 남길수도 있습니다
    # writer: str                   # 이러면 인스턴스 변수

    title: str  # 인스턴스 변수, 반드시 할당해줘야 합니다

    is_sale: bool = True  # 이렇게 기본 값을 정해줄 수도 있습니다


    # shared_list: list = []        # err! (mutable 한 값을 할당할 수 없습니다)

    # 때문에 아래와 같이 field를 사용해야 합니다
    unshared_list: list = field(default_factory=lambda: ["hello", "world"])

    # 다음과 같이 입력받을 값을 정할 수 도 있습니다
    isbn: str = field(init=False, default_factory=generate_isbn)

    # 기존 field들로 새로운 필드를 만들수도 있습니다
    def __post_init__(self) -> None:
        self.searchh_str = f"{self.title} - {self.isbn}"

    def __str__(self) -> str:
        return f"{self.title} - {self.isbn}"

hamlit = Book("Hamlet")
print(hamlit.__dict__)

# 위 코드를 데이터클래스를 사용하지 않고 작성하면 다음과 같습니다

class MyBook:
    language = "Learn Err Day"  # 클래스 변수

    def __init__(self, title, is_sale=True, writer=None, unshared_list=None, isbn=None):
        self.title = title
        self.is_sale = is_sale
        if unshared_list is None:
            shared_list = ["hello", "world"]
        self.isbn = generate_isbn()
        self.search_str = f"{self.title} - {self.isbn}"

    def __str__(self):
        return f"{self.title} - {self.isbn}"

