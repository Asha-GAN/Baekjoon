# 입력받은 수를 문자열로 바꾼 뒤 문자열 인덱싱을 통해 리스트에 삽입
num = list(map(int, str(input())))

# 내장 함수 sort 함수 사용하여 reverse로 역순으로 정렬
num.sort(reverse=True)

for i in num:
    print(i, end='')