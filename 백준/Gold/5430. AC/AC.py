a = int(input())
for i in range(a):
    r_d = input()
    leng = int(input())
    num_list = input()
    if num_list == '[]':
        result = []
    else:
        num_list = num_list[1:-1]
        result = list(map(int,num_list.split(',')))

    # if len(r_d) != 1:
    #     for k in range(1,len(r_d)):
    #         if r_d[k-1] == r_d[k] == 'R':
    #             r_d = r_d.replace(r_d[k],'')
    #             r_d = r_d.replace(r_d[k],'')
    side = 0
    error = 0
    for j in r_d:
        if j =='R':
            side += 1
        elif j == 'D':
            if len(result) == 0:
                print('error')
                error += 1
                break
            else:
                if side % 2 == 0:
                    del result[0]
                else:
                    del result[-1]
    if error != 1:
        if side % 2 == 0:
            print('['+','.join(map(str,result))+']')
        else:
            print('['+','.join(map(str,result[::-1]))+']')