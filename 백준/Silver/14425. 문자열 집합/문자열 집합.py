a,b = map(int,input().split())
list1 = []
list2 = []
for i in range(a):
    list1.append(input())
for j in range(b):
    list2.append(input())
count = 0
for k in list2:
    if k in list1:
        count += 1
print(count)