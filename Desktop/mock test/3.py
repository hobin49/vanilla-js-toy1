# 재서기는 수현이와 숨바꼭질 중 재서기는 수혀니가 1번 헛간부터 찾을 것을 알고 있다. 모든 헛간은 M개의 양방향
# 최대한 숨길 수 있는 헛간을 찾을 수 있게 도와주자
# bfs...문제
# 냄새는 1번 헛간에서의 거리(지나야 하는 길의 최소 개수)가 멀어질수록 감소한다고 한다.

from collections import deque


n, m = map(int, input().split())

# 양방향 그래프
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    n1, n2 = map(int, input().split())
    graph[n1].append(n2)
    graph[n2].append(n1)

# 방문표시
visited = [0] * (n + 1)


def bfs(x):
    queue = deque()
    # 시작 지점 추가
    queue.append(x)
    # 방문처리
    visited[x] = 1
    while queue:
        x = queue.popleft()
        for adj in graph[x]:
            # 방문하지 않은 곳이면
            if visited[adj] == 0:
                # 각 노드에 갈 떄까지 거리를 기록해준다.
                visited[adj] = visited[x] + 1
                queue.append(adj)


bfs(1)
max_ = max(visited)

cnt = 0
for i in visited:
    if max_ == i:
        cnt += 1

# 숨어야 하는 헛간, 헛간까지의 거리, 헛간과 같은 거리를 갖는 개수
print(visited.index(max_), max_ - 1, cnt)
