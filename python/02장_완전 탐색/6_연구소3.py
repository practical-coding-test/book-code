# https://www.acmicpc.net/problem/17142

from collections import deque
import sys

# 재귀 함수 한계 설정
sys.setrecursionlimit(10000)

N, M  = map(int, input().split())
# 방문을 int 형식으로 관리 (바이러스의 조합을 할 때마다 visit 초기화 방지)
visit = [[0]* N for _ in range(N)]
v = 0
area = 0
dr = (-1,0,1,0)
dc = (0,1,0,-1)

def bfs(arr, virus, visit):
    dq = deque([position for position in virus])

    for r,c in virus:
        visit[r][c] = v

    t = 0
    notEmpty = 0
    
    while dq:
        count = len(dq)
        
        # 조건문이 int 타입일 경우 int가 0이면 False, 이외에는 True
        while count:
            count -= 1
            r, c = dq.popleft()
            notEmpty += 1 if arr[r][c] == 0 else 0
            for d in range(4):
                nr, nc = r + dr[d], c + dc[d] 
                if (not (0 <= nr < N and 0 <= nc < N)) or visit[nr][nc] == v: continue
                if arr[nr][nc] == 1: continue
                visit[nr][nc] = v
                dq.append((nr, nc))

        # 빈칸이 모두 사라지면 반복문 탈출
        if area == notEmpty: break
        t += 1

    return t if area == notEmpty else 0x3f3f3f3f

def dfs(arr, virus, r, c):
    global v
    # base case
    if len(virus) == M:
        v += 1
        return bfs(arr, virus, visit)

    if r == N: 
        return 0x3f3f3f3f

    # 다음 좌표 계산
    nr = r + 1 if c + 1 == N else r
    nc = 0 if c + 1 == N else c + 1
    ret = 0x3f3f3f3f

    if arr[r][c] == 2:
        virus.append((r,c))
        ret = dfs(arr, virus, nr, nc)
        virus.pop()

    return min(ret, dfs(arr, virus, nr, nc))

arr = []

for i in range(N):
    arr.append(list(map(int, input().split())))

    for v in arr[-1]:
        # 삼항 연산자를 이용하여 빈 공간만 확인
        area += 1 if v == 0 else 0

ret = dfs(arr,[], 0, 0)
print(ret if ret != 0x3f3f3f3f else -1)