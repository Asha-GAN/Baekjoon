n = int(input())
nums = list(input())

# 숫자 합 변수 지정
total = 0

# 리스트에 저장한 숫자를 불러와 정수로 변환 후 덧셈
for i in nums:
    total += int(i)

print(total)