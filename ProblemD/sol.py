
n = m = int(input())
num = int(input())

total = m + n
poss = min(num - 1, total - num + 1)
ans = poss / (m * n)

print(str(round(ans * 1000)) + "/1000")
