nums = [1,1,1,2,2,3]
k = 2


dict = {}
list = []
for i in range(len(nums) + 1):
    sub = []
    list.append(sub)

for item in nums:
    dict[item] = 1 + dict.get(item, 0)
for k, v in dict.items():
    list[v].append(k)

print(dict)
print(list)
final = []
for i in range(len(list) - 1, 0, -1):
    for n in list[i]:
        final.append(n)
        if len(final) == k:
            break

print(final)