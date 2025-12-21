# https://www.acmicpc.net/problem/2533

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n = int(input())
adj = [[] for _ in range(n+1)]

# 0: 지지자 안보냄 , 1: 지지자 보냄
supporter = [[0x3f3f3f3f] * (n + 1) for _ in range(2)]
visit = [False]*(n+1)

for i in range(n-1):
    a, b = map(int, input().split())
    adj[a].append(b)
    adj[b].append(a)

def get_min_supporter(send, now):
    # 이미 계산된 경우
    if supporter[send][now] != 0x3f3f3f3f:
        return supporter[send][now]
    visit[now] = True

    if send == 1:
        supporter[send][now] = 1
    else:
        supporter[send][now] = 0

    # 지지자가 이 부서로 보내진 경우
    if send == 1:
        for child in adj[now]:
            if visit[child]: continue
            # 자식 부서는 지지자를 보내지 않아도 되기 때문에 둘 중 작은 수를 선택합니다.
            supporter[send][now] += min(get_min_supporter(0, child), get_min_supporter(1, child))
    else:
        for child in adj[now]:
            if visit[child]: continue
            # 지지자가 이 부서로 안보내진 경우 자식 노드들에게 모두 지지자를 보내야 합니다.
            supporter[send][now] += get_min_supporter(1, child)
    
    visit[now] = False
    
    return supporter[send][now]

print(min(get_min_supporter(0, 1),get_min_supporter(1, 1)))