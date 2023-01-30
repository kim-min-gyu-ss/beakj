while True:
    a = input()
    if a == '.':
        break
    st_list = []
    for i in a:
        if i == '(':
            st_list.append(i)
        elif i == '[':
            st_list.append(i)
        elif i == ')':
            if len(st_list) == 0:
                st_list.append('x')
                break
            q = st_list.pop()
            if q != '(':
                st_list.append('x')
                break
        elif i == ']':
            if len(st_list) == 0:
                st_list.append('x')
                break
            w = st_list.pop()
            if w != '[':
                st_list.append('x')
                break
        else:
            continue
    if len(st_list) == 0:
        print('yes')
    else:
        print('no')