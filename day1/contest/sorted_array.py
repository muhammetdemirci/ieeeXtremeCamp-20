n = int(input())
array = [int(item) 
    for item in input().split(" ")]
sorted_array = sorted(array)

if array == sorted_array:
    print('yes\n 1 1')
    exit()

lr = []
for i in range(n):
    if (array[i] != sorted_array[i]):
        lr.append(i)
rvs = array[lr[0]:lr[-1]+1]
rvs.reverse()
if (rvs == sorted_array[lr[0]:lr[-1]+1]):
    print("yes\n"+str(lr[0]+1)+" "+str(lr[-1]+1))
    exit()
else:
    print("no")
    exit()
