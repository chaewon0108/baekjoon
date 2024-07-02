# baekjoon2475

> pps 캠프 1일차
일주일에 코딩 20개 이상씩(일요일은 day off)
1일차 3번째 문제 시작!!

2번째 문제를 생각보다 일찍 끝내게 되어 기분이 좋다 :)
자신감 UP!!

---
# 문제
컴퓨터를 제조하는 회사인 KOI 전자에서는 제조하는 컴퓨터마다 6자리의 고유번호를 매긴다. 고유번호의 처음 5자리에는 00000부터 99999까지의 수 중 하나가 주어지며 6번째 자리에는 검증수가 들어간다. 
검증수는 고유번호의 처음 5자리에 들어가는 5개의 숫자를 각각 제곱한 수의 합을 10으로 나눈 나머지이다.

예를 들어 고유번호의 처음 5자리의 숫자들이 04256이면, 각 숫자를 제곱한 수들의 합 0+16+4+25+36 = 81 을 10으로 나눈 나머지인 1이 검증수이다.

## 입력
첫째 줄에 고유번호의 처음 5자리의 숫자들이 빈칸을 사이에 두고 하나씩 주어진다.

## 출력
첫째 줄에 검증수를 출력한다.

---

# 내 생각 정리
1. 입력할 5숫자를 받기
2. 입력된 고유번호의 5자리에 들어가는 5개의 숫자를 int형으로 변환
3. 이 숫자들을 split으로 나눠서 각 숫자를 제곱하기
4. 제곱한 수의 합을 10으로 나눈 나머지를 구하기 -> 구해야 하는 검증수가 됨

---
# 사용한 파이썬 문법 정리
## 1. 제곱
- 파이썬 표현 : x ** y

1) 숫자를 직접 입력
```
print(2 ** 10) # 2의 10제곱
```
**2) 변수를 이용하여 제곱을 구하는 방법**
```
a = 2
b = 10
print(a ** b) # a의 b제곱
```
3) 변수 + 숫자의 제곱
```
x = 2
print(x ** 11) #x의 11제곱
```

## append
- 두번째 오류를 해결하기 위해 사용했다.

- append : list에 데이터를 추가하기 위한 방법 중 하나
- 리스트이름.append(데이터값)

---
# 오류

## 첫번째 오류
처음으로 정리했던 생각에서
- 숫자 받기 -> int형 변환 -> split으로 분류
- 이 과정이 될 거라고 생각했는데, TypeError: int() argument must be a string, a bytes-like object or a real number, not 'list' 이러한 오류가 발생하여 순서를 아래와 같이 바꿔 코드를 짰다.

1. 숫자 받기
2. for문 선언
3. for문 안에서 num[i]들을 각각 int로 만들어버리기


## 두번째 오류
```
init_num = input()
num = init_num.split()
int_num = list(map(int, num))

squ_num = []


for i in range(len(init_num)):

  squ_num = (int_num[i] ** 2)

squ_num_sum = sum(squ_num)
rest = squ_num_sum % 10
print(rest) # 검증수
```
코드를 이렇게 짰다가, 
squ_num_sum = sum(squ_num)
TypeError: 'int' object is not iterable
이런 오류가 나왔다 ^^;...

squ_num 변수를 리스트로 선언했지만, 반복문 안에서 정수로 덮어쓰고 있고,
squ_num_sum = sum(squ_num) 부분에서 squ_num이 리스트가 아닌 정수라서 오류가 발생한다고 한다.

따라서 코드를 수정했다.

```
squ_num.append(int_num[i] ** 2)
```
이렇게만!!
그랬더니 오류가 사라졌다.

## 세번째 오류
```
init_num = input()
num = init_num.split()
int_num = list(map(int, num))

squ_num = []

for i in range(len(init_num)):
  squ_num.append(int_num[i] ** 2)

squ_num_sum = sum(squ_num)
rest = squ_num_sum % 10
print(rest) # 검증수
```
이렇게 했다가
squ_num.append(int_num[i] ** 2)
IndexError: list index out of range

이런 오류를 발견했다..
따라서 인덱스의 범위를 수정했고

인덱스 범위 수정에 따라 init_num을 굳이 사용하지 않아도 된다고 판단하여 맨 처음 부분도 수정했다

---
# 결과
열심히 오류를 해결한 결과이다.

```
num = input()
num = num.split()
int_num = list(map(int, num))

squ_num = []

for i in range(len(int_num)):
  squ_num.append(int_num[i] ** 2)

squ_num_sum = sum(squ_num)
rest = squ_num_sum % 10
print(rest) # 검증수
```
<img width="703" alt="image" src="https://github.com/chaewon0108/baekjoon2475/assets/174469937/2620ed05-4abf-4ee0-b860-3a8c5075cedb">

---

# 소감
> 이번 문제는 input들을 int로 바꾸고, split하는 부분에서도 시간이 많이 소요됐고, append를 몰라 시간을 많이 소요했다 ㅎ
list를 사용할 때 int로 바꾸고, split 할 수 있는 순서와
append를 사용하는 방법을 꼭 기억해야겠다.

---
# 참고 자료
https://blockdmask.tistory.com/377 

https://creatorjo.tistory.com/entry/%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EB%A6%AC%EC%8A%A4%ED%8A%B8list-%EB%8D%B0%EC%9D%B4%ED%84%B0-%EC%B6%94%EA%B0%80-append
