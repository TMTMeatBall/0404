T = int(input())
for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    cost = [0 for _ in range(13)]

    for i in range(13):
        cost[i] = min(plan[i] * price[0], price[1]) + cost[i - 1]
        if i > 2:
            cost[i] = min(cost[i], price[2] + cost[i - 3])  # price[2]를 택하면 i, i-1, i-2까지의 세달을 전부 커버한다
    ans = min(cost[12], price[3]) #1~12개월까지의 비용최소합 vs 1년 플랜 가격 사이의 최소값 비교

    print(f'#{tc} {ans}')
    # 어떤 변수가 갱신되어야 하는가
    # 함수()
