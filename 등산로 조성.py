

def dfs(x, y, cnt, K):
    global max_cnt

    if max_cnt < cnt:
        max_cnt = cnt

    visited[x][y] = 1

    for dx, dy in [[-1, 0], [0, -1], [0, 1], [1, 0]]:
        nx, ny = x + dx, y + dy

        # if 0 <= nx < N and 0 <= ny < N and arr[x][y] < arr[nx][ny] and visited[nx][ny] == 0:
            #기저조건 사방탐색을 해도 더 갈 곳이 없으면 종료
            # if max_cnt < cnt:
            #     max_cnt = cnt


        if 0 <= nx < N and 0 <= ny < N and visited[nx][ny] == 0:
            if arr[x][y] > arr[nx][ny]:
                visited[nx][ny] = 1
                dfs(nx, ny, cnt + 1, K)

            elif K and K > arr[nx][ny] - arr[x][y] and visited[nx][ny] == 0:  # K가 아직 값을 갖고 있으며, K가 파낼 수 있는 크기가 충분할 때,
                a = arr[nx][ny]
                arr[nx][ny] = arr[x][y] - 1 #진행할 수 있도록 arr[ni][nj] 값을 깎아서 진행하고, 다시원래대로 돌려서(필요있나?)
                visited[nx][ny] = 1 #cnt가 갱신 잘 될 수 있도록 갈림길마다 표시 위치 잘 잡기
                dfs(nx, ny, cnt + 1, 0)
                arr[nx][ny] = a


    visited[x][y] = 0 #cnt 경우의 수
T = int(input())
for tc in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    # 가장 높은 곳부터 시작함
    start = 0
    max_cnt = 0
    visited = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if start < arr[i][j]:
                start = arr[i][j]

    for i in range(N):
        for j in range(N):
            if arr[i][j] == start:  # 가장 높은 포인트일 때에, 거기서부터 탐색하는 함수를 돌린다.
                dfs(i, j, 1, K)  # i,j는 무조건 갱신되어야 하고, K도 사용한 경우, 아닌 경우 갱신, 현재 등산로 길이(시작점 찍고 가므로 1부터)
    print(f'#{tc} {max_cnt}')

# 종료
# 가지치기
# 메인
# 갱신 및 초기화**
# 대소관계를 따라 움직이는데 visited를 기록할 필요가 있나? 있다. 이동가능한 곳이 1개를 넘어간 경우에 필요하다.
# 미로탐색하듯이 넘어가서 어디서 막혔는지. 막힌 순간까지 세고 다시 돌아왔을 때에 visited기록되어있지 않으면 무한히 돌게 된다.(index오류남)