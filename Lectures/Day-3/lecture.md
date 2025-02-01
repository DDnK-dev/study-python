# Day 3 - python 입문과 그 특징

## 파이썬이란

---

![python-logo](https://www.python.org/static/img/python-logo.png)

- 1989년 12월, 네덜란드 출신의 프로그래머인 귀도 반 로섬(Guido van Rossum)이 개발한 인터프리터 언어입니다.
    - 인터프리터 언어란, 소스 코드를 바로 실행할 수 있는 프로그램을 말합니다.

- 원칙은 간단합니다.
  - 읽기 쉬워야 한다
  - 사용자가 원하는 모듈 패키지를 쉽게 만들고, 설치할 수 있어야 한다

![python-usage](https://codingmart.com/wp-content/uploads/2024/01/image_2024-01-24_121129247-e1706078513951.png)
- 많은 곳에서 사용중입니다
  - 구글이 만든 소프트웨어의 50% 이상이 파이썬으로 작성 되었다고 합니다.
  - 웹 개발, **데이터 분석**, **머신러닝** 등

## 파이썬 특징

---

1. 문법이 인간답습니다

```python
if 3 in [1, 2, 3, 4]:
    print("3이 있습니다.")
```
2. 다른 언어에 비해 문법이 간결하고 쉽습니다.
```python
languages = ['python', 'perl', 'c', 'java']

for lang in languages:
    if lang in ['python', 'perl']:
        print("%6s need interpreter" % lang)
    elif lang in ['c', 'java']:
        print("%6s need compiler" % lang)
    else:
        print("should not reach here")
```
이걸 자바로 했을 때
```java
String[] languages = {"python", "perl", "c", "java"};

for (String lang : languages) {
    if (lang.equals("python") || lang.equals("perl")) {
        System.out.printf("%6s need interpreter\n", lang);
    } else if (lang.equals("c") || lang.equals("java")) {
        System.out.printf("%6s need compiler\n", lang);
    } else {
        System.out.println("should not reach here");
    }
}
```

3. 빠르게 개발 가능

> Life is too short, You need Python

## PEP 8

---

![pep8](https://files.realpython.com/media/PEP-8-Tutorial-Python-Code-Formatting-Guide_Watermarked.9103cf7be328.jpg)

- PEP 은 파이썬 개선 제안서(Python Enhancement Proposal)의 약자
  - 파이썬 커뮤니티에 파이썬 언어의 기능을 개선하거나 추가하기 위한 제안서
  - PEP 전체 목록을 보고 싶다면 [여기](https://peps.python.org/#)를 클릭하세요.
- PEP 8은 파이썬 코드를 작성할 때의 스타일 가이드
  - 들여쓰기, 변수명, 함수명, 클래스명 등의 작성 방법을 제시
- [PEP 8](https://www.python.org/dev/peps/pep-0008/) 전체 내용을 보고 싶다면 클릭하세요.
  - 한 번쯤 읽어보는 것을 추천
- Pycharm에서 코드를 작성할 때 PEP 8을 지키지 않는다면 빨간 줄로 표시해줍니다.
  - 이를 지키는 것이 좋습니다.
- PEP 8을 지키지 않아도 코드는 잘 동작합니다.
  - 하지만, PEP 8을 지키는 것이 좋은 이유는 코드의 가독성을 높여주기 때문입니다.

### 파이썬 철학

---

- 파이썬에는 파이썬 다운 방식(Pythonic way)이라는 철학이 있습니다.
- 언어 차원에서 Zen of Python이라는 이름으로 이런 철학을 제시합니다.
- Tim Peters가 작성한 Zen of Python은 파이썬 인터프리터에서 `import this`를 실행하면 볼 수 있습니다.
```text
>> import this

The Zen of Python, by Tim Peters
아름다움이 추함보다 낫다.
명시적인 것이 암시적인 것보다 낫다.
단순한 것이 복잡한 것보다 낫다.
복잡한 것이 난해한 것보다 낫다.
평평한 것이 중첩된 것보다 낫다.
희소한 것이 밀집된 것보다 낫다.
가독성은 중요하다.
특별한 경우라고 해서 규칙을 어기는 것이 좋은 것은 아니다.
비록 실용성은 순수성을 능가한다 해도.
오류는 절대 조용히 지나가면 안된다.
명시적으로 조용히 지나가도록 한 것이 아니라면.
모호함이 있을 때는 추측을 하지 말아야 한다.
문제를 풀 수 있는 (바람직하고 유일한) 분명한 방법이 있어야 한다.
비록 그 방법이 처음에는 분명하지 않을 수도 있지만 (네덜란드 사람이 아니라면). # 로섬이 네덜란드 출신이기 때문
지금 하는 것이 아예 안 하는 것보다 낫다.
비록 아예 안 하는 것이 지금 *당장* 하는 것보다 나을 때도 많다.
구현이 설명하기 어렵다면, 그것은 나쁜 아이디어다.
구현이 설명하기 쉽다면, 그것은 좋은 아이디어일 수 있다.
네임스페이스는 정말 훌륭한 아이디어다 -- 더 많이 사용하자!
```

## 파이썬 기초 문법

---

### 인덴트 (Indentation)

- 파이썬은 코드 블록을 들여쓰기로 구분합니다.
- PEP 8에서는 공백 4칸을 권장합니다. 따라서 탭(tab)을 사용하지 않고 공백(space) 4칸을 사용하는 것이 좋습니다.

```python
def hello():
    print("Hello, Python!")
    if True:
        print("True")
    else:
        print("False")
```

### 변수 (Variable)

- 변수는 값을 저장하는 공간입니다.

```python
a = 3
b = 4
print(a + b)  # 7
```

- 다만 파이썬에서는 변수를 값에 붙이는 라벨이라고 생각하는 것이 더 정확합니다.

```python
a = 3
b = a
a = 4
print(b)  # 4
```

- 파이썬은 동적 타이핑 언어입니다.
  - 변수를 선언할 때 타입을 지정하지 않습니다.
  - 변수에 값이 할당될 때 타입이 결정됩니다.
```python
a = 3
print(type(a))  # <class 'int'>
a = 3.14
print(type(a))  # <class 'float'>
```

- 파이썬에는 원시 타입이 없습니다.
  - 모든 것이 객체입니다.
  - 따라서 모든 변수는 객체에 대한 참조입니다.
  - 이때문에 

```python
a = 3
print(type(a))  # <class 'int'>
a.bit_length()  # 2
```

#### 네이밍 컨벤션

- 변수명과 함수명은 소문자로 작성하고, 여러 단어일 경우 `_`로 구분합니다.
  - 이를 스네이크 케이스(Snake Case)라고 합니다.
  - 이를 지키지 않을 시 IDE에서 경고를 표시합니다.

```python
# Camel Case
def helloWorld():
    print("Hello, World!")
# Snake Case
def hello_world():
    print("Hello, World!")
```

### 숫자형

- 파이썬은 정수형, 실수형, 복소수형을 지원합니다.
- 정수형은 `int`, 실수형은 `float`, 복소수형은 `complex`로 표현합니다.

```python
a = 3
print(type(a))  # <class 'int'>
b = 3.14
print(type(b))  # <class 'float'>
c = 3 + 4j
print(type(c))  # <class 'complex'>
```

- 다른 언어에서, 대부분의 int는 4바이트, 8바이트로 표현됩니다.
- 파이썬은 메모리가 허용하는 한 무한대의 정수를 표현할 수 있습니다.
  - 숫자형이 표현 가능한 범위를 넘어가면 자동으로 메모리를 늘려줍니다.
  - 다만 이때 속도가 느려질 수 있습니다.

```python
import sys

a = 2
for i in range(10000):
    a *= 2
    print(sys.getsizeof(a))
```
