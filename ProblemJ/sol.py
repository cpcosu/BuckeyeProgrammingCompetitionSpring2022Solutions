from collections import defaultdict
from math import inf, isinf
from copy import deepcopy

from itertools import chain, repeat, count, islice
from collections import Counter


def repeat_chain(values, counts):
    return chain.from_iterable(map(repeat, values, counts))


def unique_combinations_from_value_counts(values, counts, r):
    n = len(counts)
    indices = list(islice(repeat_chain(count(), counts), r))
    if len(indices) < r:
        return
    while True:
        yield tuple(values[i] for i in indices)
        for i, j in zip(reversed(range(r)), repeat_chain(reversed(range(n)), reversed(counts))):
            if indices[i] != j:
                break
        else:
            return
        j = indices[i] + 1
        for i, j in zip(range(i, r), repeat_chain(count(j), counts[j:])):
            indices[i] = j


def unique_combinations(iterable, r):
    values, counts = zip(*Counter(iterable).items())
    return unique_combinations_from_value_counts(values, counts, r)


def placeBox(container, box, posX, posY):
	for x in range(box[0]):
		for y in range(box[1]):
			if container[posY + y][posX + x]: return container, False
			container[posY + y][posX + x] = True
	return container, True

def tryAndFitRec(container, boxes):
	if len(boxes) == 0:
		return True
	containerWidth = len(container[0])
	containerHeight = len(container)

	box = boxes.pop()

	boxX = box[0]
	boxY = box[1]

	for x in range(containerWidth - boxX + 1):
		for y in range(containerHeight - boxY + 1):
			cont = [[i for i in row] for row in container]
			cont, placed = placeBox(cont, box, x, y)
			if placed:
				if tryAndFitRec(cont, boxes.copy()):
					return True		
	return False

def tryAndFit(container, boxes):
	lenBoxes = len(boxes)
	
	width = container[0]
	height = container[1]

	contArea = width * height

	if lenBoxes > contArea: return False
	
	area = 0
	for i in boxes:
		area += i[0] * i[1]
	
	if area > contArea: return False
	
	arr = [[False for _ in range(width)] for _ in range(height)]

	return tryAndFitRec(arr, boxes)



usedThiscombo = set()
def rec(allBoxes: dict, emptyBoxes:dict, fitInside: dict):
	global usedThiscombo

	tupleCreationAllBoxes = []
	for i in allBoxes:
		tupleCreationAllBoxes.append((i[0], i[1], allBoxes[i]))
	tupleCreationAllBoxes.sort()

	tupleCreationEmptyBoxes = []
	for i in emptyBoxes:
		tupleCreationEmptyBoxes.append((i[0], i[1], emptyBoxes[i]))
	tupleCreationEmptyBoxes.sort()

	test = (tuple(tupleCreationAllBoxes), tuple(tupleCreationEmptyBoxes))

	if test in usedThiscombo:
		return []
	usedThiscombo.add(test)

	# find box with least number of possible boxes inside
	smallestBox = -1
	numberOfBoxesInside = inf
	for i in emptyBoxes:
		numBox = len(fitInside[i])
		if numBox != 0 and numBox < numberOfBoxesInside:
			smallestBox = i
			numberOfBoxesInside = numBox
	
	# return this combination if no more boxes fit inside each other
	finalPossibilities = [allBoxes]
	if isinf(numberOfBoxesInside):
		return finalPossibilities

	# find boxes that can fit inside
	insideBoxes = []
	numberOfBoxesInside = 0
	for i in fitInside[smallestBox]:
		a = allBoxes[i]
		numberOfBoxesInside += a
		for _ in range(a):
			insideBoxes.append(i)

	for i in range(numberOfBoxesInside, 0, -1):
		# boxCombos = set(comb(insideBoxes, i))
		boxCombos = unique_combinations(insideBoxes, i)
		# print(i, fitInside[smallest], *boxCombos)
		for currBoxes in boxCombos:
			if tryAndFit(smallestBox, list(currBoxes)):
				tempBoxes = deepcopy(allBoxes)
				tempEmptyBoxes = deepcopy(emptyBoxes)
				tempFitInside = deepcopy(fitInside)

				tempEmptyBoxes[smallestBox] -= 1
				if tempEmptyBoxes[smallestBox] == 0:
					tempEmptyBoxes.pop(smallestBox)

				for i in currBoxes:
					tempBoxes[i] -= 1
					if tempBoxes[i] == 0:
						tempBoxes.pop(i)
						tempFitInside.pop(i)
						for k in tempFitInside:
							if i in tempFitInside[k]:
								tempFitInside[k].remove(i)
				finalPossibilities.extend(rec(tempBoxes, tempEmptyBoxes, tempFitInside))
		# for poss in 

	
	return finalPossibilities




n = int(input())
boxes = [tuple(map(int, input().split())) for _ in range(n)]

boxSizes = set(boxes)

fitInside = defaultdict(list)

boxCounts = defaultdict(lambda: 0)

for i in boxes:
	boxCounts[i] += 1

for i in boxSizes:
	curr = []
	for k in boxSizes:
		if i[0] == k[0] and i[1] == k[1]:
			continue
		if i[0] <= k[0] and i[1] <= k[1]:
			fitInside[k].append(i)


funcBoxes = [[b] for b in boxes]

# print(boxCounts)
# print(fitInside)
# print()

p = rec(boxCounts, boxCounts, fitInside)
# print(p)

best = min(p, key= lambda x: sum([i[0] * i[1] * x[i] for i in x]))


# print(len(p))
# print(best)
print(sum([i[0] * i[1] * best[i] for i in best]))

