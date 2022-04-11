

n = int(input())

defined = set()
undefined = set()

for _ in range(n):
	defintion = input().split()
	defined.add(defintion.pop(0))
	undefined.update(defintion)

undefined.difference_update(defined)

# print(defined)
# print(undefined)
print(len(undefined))
