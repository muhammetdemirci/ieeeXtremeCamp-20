n = int(input())
dic = {}
line = input()
items = line.split()
for item in items:
    if item in dic:
        dic[item] += 1
    else:
        dic[item] = 1
print(max(dic.values()), len(dic.keys()))
