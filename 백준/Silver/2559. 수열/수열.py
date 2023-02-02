a, b = map(int,input().split())
num_list = list(map(int,input().split()))
mx_num = sum(num_list[:b])
tem_num = mx_num
for i in range(0,len(num_list) - b):
    tem_num = tem_num - num_list[i] + num_list[i + b]
    if tem_num > mx_num:
        mx_num = tem_num
print(mx_num)