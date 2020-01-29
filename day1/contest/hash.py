n = int(input())
outs = []
for i in range(n):
    money = int(input())
    num_of_cost = int(input())
    dic = {}
    index = 1
    for cost in input().split(" "):
        cost = int(cost)
        if (money - cost) in dic:
            outs.append(str(dic[money-cost]) + " " + str(index))
        else:
            dic[cost] = index

        index += 1
print("\n".join(outs))
