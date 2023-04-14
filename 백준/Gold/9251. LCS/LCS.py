string1 = input()
string2 = input()
result = [0 for _ in range(len(string2))]
for i in range(len(string1)):
    tmp = 0
    for j in range(len(string2)):
        if tmp < result[j]:
            tmp = result[j]
        elif string1[i] == string2[j]:
            result[j] = tmp + 1
print(max(result))