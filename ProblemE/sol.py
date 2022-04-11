
def isPrime(n:int) -> bool:
    if n <= 1: return 0
    if n == 2: return 1
    if not n % 2: return 0
    if n < 9: return 1
    if not n % 3: return 0

    c = 5
    while c ** 2 <= n:
        if not n % c: return 0
        if not n % (c + 2): return 0
        c += 6
    
    return 1


s, l = map(int, input().split())
num = input()


best = 0
for leng in range(l, 0, -1):
    for s in range(0, len(num) - leng):
        string = num[s:s+leng]
        if(string[0] == "0"): continue
        cp = int(string)
        if cp > best and isPrime(cp):
            best = cp
    if best:
        break
else:
    best = "No Primes"
print(best)