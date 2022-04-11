from collections import defaultdict
from math import inf

n, e = map(int, input().split())
target = int(input())

data = [tuple(map(int, input().split())) for i in range(e)]

connections = defaultdict(list)

for (u, v, dis) in data:
	connections[u].append((v, dis))
	connections[v].append((u, dis))

places = defaultdict(lambda: (inf, inf, None))
places[1] = (0, 0, None)
queue = set()
queue.add((0, 0, 1))
visited = set()

while queue:
	curr = min(queue, key=lambda x: (x[0], -x[1]))

	queue.remove(curr)


	days = curr[0] + 1
	u_dis = curr[1]
	u = curr[2]

	if u not in visited:
		for (v, v_dis) in connections[u]:
			if days < places[v][0] or (days == places[v][0] and u_dis + v_dis > places[v][1]):
				places[v] = (days, u_dis + v_dis, u)
				queue.add((days, u_dis + v_dis, v))
	visited.add(u)

ans = places[target]
print(ans[0], ans[1])



