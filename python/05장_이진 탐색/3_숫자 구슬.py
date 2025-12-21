# https://www.acmicpc.net/problem/2613

def determine(bead, dest, m):
    bead_sum = 0
    bead_num = []
    num = 0
    
    group_num = 1
    for b in bead:
        if bead_sum + b > dest:
            if group_num == m: return (False, [])
            group_num+=1
            bead_num.append(num)
            bead_sum = 0
            num = 0
        num += 1
        bead_sum += b
    bead_num.append(num)
    return (True, bead_num)

def parametric_search(m, bead):
    start = 0
    bead_num = []
    for b in bead:
        start = max(b, start)
    end = sum(bead)+1

    while start < end:
        mid = (start+end)//2

        result, bead_num_result = determine(bead, mid, m)
        if not result:
            start = mid+1
        else:
            end = mid
            bead_num = bead_num_result
    return start, bead_num

n,m = map(int, input().split())
bead = list(map(int, input().split()))

result, bead_num = parametric_search(m, bead)
new_bead_num = []
need = m - len(bead_num)

for b in bead_num:
    while need != 0 and b != 1:
        new_bead_num.append(1)
        b -=1
        need-=1
    new_bead_num.append(b)

print(result)
for b in new_bead_num:
    print(b, end=' ')