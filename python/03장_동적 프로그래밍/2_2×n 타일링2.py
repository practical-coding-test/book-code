# https://www.acmicpc.net/problem/11727

n = int(input())

# Bottom Up
tiles = [0]*(n+1)
tiles[0] = tiles[1] = 1

for i in range(2, n+1):
    tiles[i] = (tiles[i-1] + tiles[i-2]*2)%10007

print(tiles[n])