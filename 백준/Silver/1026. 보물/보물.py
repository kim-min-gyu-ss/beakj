a = int(input())
a_list = list(map(int,input().split()))
b_list = list(map(int,input().split()))

a_list = sorted(a_list)
b_list = sorted(b_list, reverse= True)

sum = 0
for i in range(len(a_list)):
    hab = a_list[i] * b_list[i]
    sum += hab
    
print(sum)