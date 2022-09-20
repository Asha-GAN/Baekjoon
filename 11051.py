# math 모듈에서 factorial 함수 가져옴
from math import factorial

# 입력받은 두 수를 공백을 기준으로 나누어서 n, k에 삽입
n, k = map(int, input().split())

# 팩토리 공식
result = factorial(n) // (factorial(k) * factorial(n - k))

print(result % 10007)

