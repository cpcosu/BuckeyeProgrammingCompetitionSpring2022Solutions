from math import gcd, inf

def lcm(a:int, b:int) -> int:
    return abs(a * b) // gcd(a , b)


n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


poss = {(0, 0, grid[0][0])}

best = inf

while len(poss) > 0:
    p = min(poss, key= lambda x: x[2])
    poss.remove(p)

    # print(p)

    x = p[0]
    y = p[1]
    val = p[2]

    if x == n - 1 and y == n - 1:
        if val < best:
            best = val
    else:
        if y + 1 < n:
            newVal = lcm(val, grid[y + 1][x])
            if newVal < best:
                poss.add((x, y + 1, newVal))
        if x + 1 < n:
            newVal = lcm(val, grid[y][x + 1])
            if newVal < best:
                poss.add((x + 1, y, newVal))
    
print(best)