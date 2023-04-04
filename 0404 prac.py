# #MST 실습
# '''
# 노드 갯수, 간선정보
# 시작정점,끝 정점,가중치 정보
# 6 11
# 0 1 32
# 0 2 31
# 0 5 60
# 0 6 51
# 1 2 21
# 2 4 46
# 2 6 25
# 3 4 34
# 3 5 18
# 4 5 40
# 4 6 51
# '''
#노드 갯수 N, 간선 M
N, M = map(int,input().split())

#인접 리스트
graph = [[] for _ in range(N+1)] #배열 인덱스는 0부터 시작하지만, 노드 인덱스는 1부터 시작하므로 0번 배열인덱스를 쓰지 않고
#N+1까지 배열 인덱스 잡고 노드와 배열을 일체화한다

#간선정보 받기
for _ in range(M):
    u, v, w = map(int,input().split())
    graph[u].append((v,w)) #u -> v 로 가는 간선 가중치 가 w
    # graph[v].append((u.w)) 무방향 그래프일 경우 같이 사용함

# import heapq
# # 프림 알고리즘
# # 반환값이 MST의 모든 가중치를 합한 값
# def prim(graph):
#     #선택한 정점에 대해서 방문여부를 체크할 리스트를 만든다
#     visited = [False] * len(graph) #[[0] for _ in range(len(graph))]
#     #최소힙
#     pq = [(0, 0)] #시작 정점과 가중치 0
#     total_weight = 0 #모든 가중치의 합
#     #중지조건 - 선택할 정점이 더 없을 때까지. 모든 정점에 대한 방문. 힙큐가 완전히 빌 때까지
#     while pq:
#         w, u = heapq.heappop(pq) #가중치, 정점
#         if visited[u]:
#             continue #이미 방문했다면, 필요x
#             visited[u] = True #1
#             total_weight += w #가중치 정보를 가산
#
#             #v정점에 인접한 정점에 간선 정보를 pq에 넣는 과정을 진행함
#             #u - 시작정점, v - 도착정점, w - 가중치 #관례적 표현
#             for v, w in graph[u]:
#                 if visited[v] == False: #아직 방문하지 않은 가중치가 있는 도착정점이 있다면,
#                     heapq.heappush(pq,(w,v))
#
#     return total_weight
#
# print(prim(graph))
#
#
#
# #크루스칼 알고리즘 (서로소인 집합 - 유니온 파인드 셋 알고리즘을 기본적으로 사용함)
#
# def kruskal(graph):
#     #부모배열 초기화까지 한꺼번에
#     p = [i for i in range(len(graph))]
#     def find(i): # i를 받았을 떄에 유니온 파인드 셋 형태로 반환하는 함수 find를 설정
#         if p[i] == i:
#             return i
#         p[i] = find(p[i])
#         return p[i]
#
#     #간선의 정보를 가중치로 오름차순 정렬
#     edges = []
#     for u in range(len(graph)):
#         for v, w in graph[u]:
#             edges.append((u,v,w))
#     edges.sort(key=lambda x: x[2])#람다를 통한 x[2]를 기준한 오름차순 정렬
#
#     #MST간선 가중치의 합
#     total_weight = 0
#
#     #간선을 총 n-1개 뽑아야 함
#     for u, v, w in edges:
#         #간선 하나에 대한 정점 u와 정점 v에 대한 대표자를 확인
#         x = find(u)
#         y = find(v)
#         #대표자가 같다면 사이클 o -> 간선을 pass함
#
#         if x != y:
#             #union과정 진행
#             p[y] = x
#             #해당되는 간선 정보를 합해준다
#             total_weight += w
#
#     return total_weight
#
# print(kruskal(graph))
#
# 다익스트라 알고리즘
# 최단 경로를 계산하는 알고리즘
# 시작 정점 s 에서 걸리는 거리값을 distance 배열에 저장함
import heapq

INF = 100000000000000  # 를 쓰거나 또는,

def dijkstra(graph, start):
    dist = [float('inf') for _ in range(len(graph))]  # 시작 정점 start 에서 다른 노드들과의 거리. 처음 시작할때는 아주아주 큰 값으로 주는 것으로 초기화해둬야 한다

    pq = [(0, start)]  # 가중치와 시작 정점
    dist[start] = 0

    while pq:
        w, u = heapq.heappop(pq)
        # 큐에서 뽑은 값의 가중치가 현재 갱신되어 있는 거리값인 dist보다 크다면 더 진행하지 않음.
        if dist[u] < w:
            continue
        #정점 u에 대해서 인접한 간선 정보를 뽑아서 dist값을 갱신해주고, 새롭게 갱신한 가중치와 해당 정점을 pq에 삽입
        for v, w in graph[u]:
            new_weight = dist[v] + w
            if new_weight < dist[v]:
                dist[v] = new_weight
                #시작정점 -> v 로 가는 최소거리값을 갱신함
                heapq.heappush(pq, (dist[v], v))
                #dist안에는 시작점으로부터 목표 정점으로 가는 최소이동값을 담는다.
    return dist
# 시작정점을 0 으로 잡고 시작
print(dijkstra(graph, 0))
