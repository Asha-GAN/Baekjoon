# collections 라는 모듈에서 deque 라는 확장형 자료구조 호출
from collections import deque

# N = 정점 개수, M = 간선 개수, V = 시작할 정점 번호
# 입력받은 값을 공백을 기준으로 분리하여 해당 변수에 삽입
N, M, V = map(int, input().split())

# 인접 영행렬 생성(2차원 배열)
graph = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    # 노드 연결
    graph[a][b] = graph[b][a] = 1


# 너비 우선 탐색
def bfs(start_v):
    visited = [start_v]  # 방문 리스트
    queue = deque()
    queue.append(start_v)

    while queue:
        v = queue.popleft()  # 방문한 노드 삭제
        print(v, end=' ')

        for w in range(N + 1):
            if graph[v][w] == 1 and (w not in visited):
                visited.append(w)
                queue.append(w)


# 깊이 우선 탐색
def dfs(start_v, visited=[]):
    visited.append(start_v)  # 방문 리스트
    print(start_v, end=' ')

    for w in range(N + 1):
        if graph[start_v][w] == 1 and (w not in visited):
            dfs(w, visited)


dfs(V)
print()
bfs(V)
