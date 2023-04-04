from collections import deque


def bfs(i, j):
    distance[i][j] = 0

    queue = deque()
    queue.append((i, j))

    while queue:
        x, y = queue.popleft()

        for dx, dy in dxy:
            nx, ny = x + dx, y + dy

            if 0 <= nx < N and 0 <= ny < N:
                diff = 0

                if arr[nx][ny] > arr[x][y]:
                    diff = arr[nx][ny] - arr[x][y]

                if distance[x][y] +1 + diff < distance[nx][ny]:
                    distance[nx][ny] = distance[x][y] +1 + diff
                    queue.append((nx,ny))

    return distance[N-1][N-1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    INF = 10000000
    distance = [[INF] * N for _ in range(N)]
    dxy = [[-1, 0], [0, -1], [0, 1], [1, 0]]
    print(f'#{tc} {bfs(0,0)}')

    # 최소거리만을 따지면 BFS
    # 가중치까지 따지는 문제
    # 스패닝 트리 중 가중치 합이 가장 작은 트리를 찾는 문제
