def n_queen(n):
    global cnt

    if n == N:  # 종료조건 행 정보
        cnt += 1
        return

    for j in range(N):  # 열 정보
        if v_1[j] == 0 and v_2[n + j] == 0 and v_3[n - j] == 0:
            v_1[j] = v_2[n + j] = v_3[n - j] = 1
            n_queen(n + 1)
            v_1[j] = v_2[n + j] = v_3[n - j] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    cnt = 0
    v_1 = [0] * N  # 열 배치 여부
    v_2 = [0] * 2 * N  # 좌상 우하 대각선 배치 여부 이차원배열 탐색을 룩업테이블화 하므로 총 범위를 2N으로
    v_3 = [0] * 2 * N  # 좌하 우상 대각선 배치 여부
    n_queen(0)
    print(f'#{tc} {cnt}')

#이차원배열 완전탐색으로 풀어보기?