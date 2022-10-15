# 최솟값, 최댓값 입력 받음
min, max = map(int, input().split())

# 최솟값, 최댓값 사이의 수의 갯수
answer = max - min + 1

# 갯수만큼의 리스트 생성
divisibleByTheSquare = [False] * (max - min + 1)

# 에라토스테네스의 체
for i in range(2, int(max ** 0.5 + 1)):
    square = i ** 2
    for j in range((((min - 1) // square) + 1) * square, max + 1, square):
        # 제곱수의 배수이면 True로 변경
        if not divisibleByTheSquare[j - min]:
            divisibleByTheSquare[j - min] = True
            answer -= 1

print(answer)