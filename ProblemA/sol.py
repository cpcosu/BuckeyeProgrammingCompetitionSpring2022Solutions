

w, h = map(int, input().split())
text = input()

for i in range(h):
	print(text[i * w:(i + 1)*w])