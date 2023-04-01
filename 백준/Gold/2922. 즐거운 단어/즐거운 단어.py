def check(s,cnt):
    global mo, ja, result

    if cnt == L:
        m_tmp = j_tmp = 0
        if 'L' not in s:
            return
        tmp = 1
        for i in s:
            if i in mo or i == '1':
                m_tmp += 1
                j_tmp = 0
                if i == '1':
                    tmp *= 5
            elif i in ja or i == '2':
                j_tmp += 1
                m_tmp = 0
                if i == '2':
                    tmp *= 20
            if m_tmp >= 3 or j_tmp >= 3:
                return
        result += tmp
        return

    for i in range(len(s)):
        if s[i] == '_':
            s = s[:i] + '1' + s[i + 1:]
            check(s,cnt + 1)
            s = s[:i] + '2' + s[i + 1:]
            check(s, cnt + 1)
            s = s[:i] + 'L' + s[i + 1:]
            check(s, cnt + 1)

strin = input()
mo = ['A','E','I','O','U'] # 5
ja = ['B','C','D','F','G','H','J','K','L','M','N','P','Q','R','S','T','V','W','X','Y','Z'] # 20
result = 0
L = strin.count('_')
check(strin, 0)
print(result)