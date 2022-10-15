# 입력받는 시간 줄이기위해서 사용
import sys
input = sys.stdin.readline

# 친구 수, 친구 관계 수 입력 받음
n, m = map(int, input().split())
arr = [[] for i in range(n)]

# 방문 표시 리스트
visited = [False] * n

# 친구 관계 입력 받음
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    # 관계 수정
    arr[a].append(b)
    arr[b].append(a)


# dfs 사용
def dfs(idx, number):
    if number == 4:
        print(1)
        exit()
    for i in arr[idx]:
        if not visited[i]:
            visited[i] = True
            dfs(i, number + 1)
            visited[i] = False


# 노드를 순서대로 방문, dfs 수행
for i in range(n):
    visited[i] = True
    dfs(i, 0)
    visited[i] = False

print(0)