# Day 2 - Git과 파이썬 변수

## Git

---

### git이란 무엇인가

- git은 버전 관리 시스템입니다.
    - git은 파일의 변화를 시간에 따라 기록합니다.
    - git은 여러 명의 사용자들이 파일을 공유하고 합칠 수 있습니다.
    - git은 로컬 저장소와 원격 저장소를 가집니다.
        - 로컬 저장소는 내 컴퓨터에 있는 저장소입니다.
        - 원격 저장소는 다른 컴퓨터에 있는 저장소입니다.
    - git은 브랜치를 가집니다.
        - 브랜치는 각각의 작업을 독립적으로 진행할 수 있게 해줍니다.
    - git은 커밋을 가집니다.
        - 커밋은 파일의 변화를 저장하는 것입니다.
- 일반적으로 git은 협업을 위해 필수적으로 사용됩니다.

### git 명령어 알아보기

#### 기본 설정

git을 사용하기 위해서는 먼저 설정을 해야 합니다.
다음 명령어로 git 설정을 지정합니다.

```git
git config --global user.email "내메일@naver.com"
git confog --global user.name  "내이름"
```

#### 기록 남기기

git의 기본적인 사용법을 익혀봅시다.

다음 명령어로 새로운 폴더를 git에게 인식시킵니다

```bash
git init
```

파일을 하나 만들어 봅니다.
```bash
# Linux 기준, 파일 생성
$ touch app.txt

# 어떤 파일이 수정되었는지 확인해봅니다
$ git status

# 어떤 내용이 수정되었는지 확인해봅니다
$ git diff

# 기록 대상으로 추가 (스테이징에 추가합니다)
$ git add app.txt # 혹은 git add .

# 스테이징을 취소하고 싶으면 아래 명령어를 사용합니다
$ git restore --staged app.txt

# git add를 좀 더 편하게 사용하려면 아래 명령어를 사용합니다
$ git add .
```

작업 내용을 기록으로 남깁니다
```bash
git commit -m "이러이러해서 커밋합니다"
```

기록 내용을 확인합니다
```bash
git log --all --oneline --graph
```

> 얼마나 자주 커밋을 해야하나요?

일반적으로 기능,작업 단위로 커밋을 합니다.
commit template을 사용하면 커밋 메시지를 통일할 수 있습니다.

```bash
# commit template 사용
$ git config --global commit.template ~/.gitmessage

$ cat ~/.gitmessage
[fea/fix/ref] 제목은 50자 이내로
  
본문은 한 줄에 72자 이내로
본문은 한 줄을 띄워 분리합니다.

[issue #n]
```

#### 오늘의 용어 정리: staging & repository

![staging](https://git-scm.com/book/en/v2/images/areas.png)

1. **Staging area**는 commit 하기 전에 commit 할 파일들을 골라놓는 곳\
git add 명령어로 staging 할 수 있습니다.\
(모든 파일을 저장할 필요는 없으며, .gitignore 파일을 통해 불필요한 파일을 추적 대상에서 제외할 수 있습니다)

2. **Repository**는 commit이 저장되는 곳\
commit을 하면 staging area에 있는 파일들이 repository로 이동합니다.\
(실체가 궁금하면 .git 폴더를 열어보세요)

### Branch로 작업하기

![branch](https://codingapple-cdn.b-cdn.net/wp-content/uploads/2022/06/%EA%B7%B8%EB%A6%BC3-1.png)

커밋하면서 계속 코드짜다보면 갑자기 새로운 기능을 추가하거나 그래야하는 경우가 있습니다.

그럴 때는 원본파일에 코드를 추가하고 커밋해도 되겠지만

혹시나 잘못해서 지금까지 짰던 프로그램이 망가지거나 그러면 어떻게하죠? 

그럴 걱정 없이 안전하게 새로운 기능을 추가하고 싶으면

프로젝트의 복사본을 만들어서 거기에 먼저 개발해보는것도 나쁘지않습니다. 

![branch](https://codingapple-cdn.b-cdn.net/wp-content/uploads/2022/06/%EA%B7%B8%EB%A6%BC45.png)

git 안에선 branch 기능을 이용해서 복사본을 쉽게 만들 수 있습니다. 

branch가 뭐냐면 그냥 프로젝트 복사본

예시와 함께 branch 하나 만들어봅시다.

```bash
git branch 브랜치이름
```
예를 들어 coupon 브랜치라면
```bash
git branch coupon
```

이제 coupon branch로 이동해봅시다.
```bash
# 옛날 버전
git checkout dev

# 최신 버전
git switch dev
```

다시 돌아가고 싶으면 `git switch main`을 사용합니다.
어느 브랜치인지 모르겠으면 `git branch` 혹은 `git branch`를 사용합니다.

#### Branch 합치기

작업을 다 했으면 이제 브랜치를 합쳐야 합니다.

```bash
# main branch로 이동
git switch main

# 브랜치 합치기
git merge coupon
```

## Git 사용 전략

![gitflow](https://techblog.woowahan.com/wp-content/uploads/img/2017-10-30/git-flow_overall_graph.png)

## 더 읽어볼거리

- [우린 Git-flow를 사용하고 있어요](https://techblog.woowahan.com/2553/)