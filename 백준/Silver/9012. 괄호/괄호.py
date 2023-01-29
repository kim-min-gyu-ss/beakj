a = int(input())
st_list = []
for i in range(a):
    st_list.append(input())
for i in st_list:
    count_right = 0
    count_left = 0
    for j in i:
        if i[0] == ')':
            break
        if j == '(':
            count_right += 1
        elif j == ')':
            count_left += 1
            if count_right < count_left:
                break
    if count_left == count_right and count_right != 0:
        print("YES")
    else:
        print("NO")