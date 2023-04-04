def n_queen(n):
    global cnt

    if n == N:  # 종료조건 행에 하나씩 8행까지 놓였음. 행체크 할필요 x
        cnt += 1
        return

    else:
        for j in range(N):
            if prom(n, j):
                visited[n][j] = 1
                n_queen(n + 1)
                visited[n][j] = 0
                #전체 리스트를 보고 cnt를 갱신시키는 형태의 문제에서는 재귀호출하면서 방문여부 꼭 초기화


def prom(x, y):
    for dx, dy in [[-1, -1], [-1, 1], [-1, 0], [1, -1], [1, 1], [1, 0]]: #행 제외 6방탐색
        nx, ny = x + dx, y + dy
        while 0 <= nx < N and 0 <= ny < N:
            if visited[nx][ny]:
                return 0
            nx, ny = nx + dx, ny + dy #범위가 허락하는 한 끝까지 탐색
    return 1


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    visited = [[0] * N for _ in range(N)]
    cnt = 0
    n_queen(0)
    print(f'#{tc} {cnt}')
# visited 이차원배열로 대각선, 가로, 세로를 보고, 그 때 0이 아니고 1이 하나라도 있으면 넘긴다.
