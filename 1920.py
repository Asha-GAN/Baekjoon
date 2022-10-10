n = int(input())
n_list = list(map(int, input().split()))
n_list.sort()

m = int(input())
m_list = list(map(int, input().split()))

# m_list의 각 원소별 이분 탐색
for num in m_list:
    lt, rt = 0, n - 1   # lt = 맨 앞, rt = 맨 뒤
    isExist = False     # 존재 여부

    # 이분 탐색
    while lt <= rt:             # lt가 rt보다 커지면 반복문 탈출
        mid = (lt + rt) // 2    # mid는 lt와 rt의 중간값
        if num == n_list[mid]:  # num이 n_list[mid]값과 같다면
            isExist = True      # isExist -> True 변경, 1 출력
            print(1)
            break

        elif num > n_list[mid]: # n_list[mid]가 num보다 작으면
            lt = mid + 1        # lt를 높임

        else:			        # n_list[mid]가 num보다 크다면
            rt = mid - 1        # rt를 낮춤

    if not isExist:
        print(0)