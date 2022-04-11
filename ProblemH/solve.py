
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(m)]
dyn = [[-1 for _ in range(n)] for _ in range(m)]

for r in range(0, m):
    for i in range(n):
        if r == 0:
            if grid[0][i] > dyn[0][i]:
                dyn[0][i] = grid[0][i]
        else:
            if dyn[r - 1][i] >= 0 and grid[r][i] > grid[r - 1][i]:
                tempDyn = dyn[r - 1][i] + grid[r][i]
                if tempDyn > dyn[r][i]:
                    dyn[r][i] = tempDyn
        
        if dyn[r][i] != -1:
            #backwards direction
            for b in range(i - 1, -1, -1):
                if grid[r][b] > grid[r][b + 1]:
                    tempDyn = dyn[r][b + 1] + grid[r][b]
                    if tempDyn > dyn[r][b]:
                        dyn[r][b] = tempDyn 
                    else:
                        break
                else:
                    break
            
            #forward direction
            if i + 1 < n and grid[r][i + 1] > grid[r][i]:
                dyn[r][i + 1] = dyn[r][i] + grid[r][i + 1]
        # print("----------------------", r, i)
        # print(dyn)
            

# print(grid)    
# print(dyn)
print(max(dyn[-1]))