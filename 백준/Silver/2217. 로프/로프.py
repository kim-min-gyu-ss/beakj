import sys
input = sys.stdin.readline
a = int(input())
rope = []
for i in range(a):
    rope.append(int(input()))
rope = sorted(rope, reverse= True)
result = []
count = 1
for i in range(len(rope)):
    result.append(rope[i] * count)
    count += 1
print(max(result))