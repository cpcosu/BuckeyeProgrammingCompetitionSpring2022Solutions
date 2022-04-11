# standard_input = open("random.in", "r").readlines()[0]

total = 0
alt = 1

n = int(input())

for i in input()[::-1]:
	total += alt * int(i)
	alt = -alt

print(total % 11)