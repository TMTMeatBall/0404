def calc(n, cost):
    global min_cost
    # 기저조건
    if n > 12:
        min_cost = min(cost, min_cost)
        return

    else:
        calc(n + 1, cost + price[0] * plan[n])

        calc(n + 1, cost + price[1])

        calc(n + 3, cost + price[2])

    #여러 경우의 수를 만드는 재귀 호출

T = int(input())
for tc in range(1, T + 1):
    price = list(map(int, input().split()))
    plan = [0] + list(map(int, input().split()))
    min_cost = price[3]
    calc(1, 0)
    print(f'#{tc} {min_cost}')
# 1일권 vs1개월권 min(plan[i]*price[0],price[1])
# 지금까지의 비용 중 i-3까지 + 3개월 플랜 vs 그냥 지금까지 1일vs1개월 가격비교한 것 단,
# 최종 12개월까지의 금액 vs 1년 플랜
# 재귀함수 호출로 가능할까?
# 갱신해줘야 할 것 - 매 달에 대한 함수는 다음 달을 재귀 호출로 불러와야 함, 마지막에 더해온 비용vs1년 플랜과 최소비교 해야함
