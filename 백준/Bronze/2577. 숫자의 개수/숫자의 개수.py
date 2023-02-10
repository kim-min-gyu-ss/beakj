a = int(input())
b = int(input())
c = int(input())
hap = a * b * c
result = {'0':0,'1':0,'2':0,'3':0,'4':0,'5':0,'6':0,'7':0,'8':0,'9':0}
for i in str(hap):
    result[i] += 1
for j in result.values():
    print(j)