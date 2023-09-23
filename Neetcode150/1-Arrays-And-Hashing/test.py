
final = []
for i, item in enumerate(nums):
    temp = nums
    del temp[i]
    value = 1
    for item in temp:
        value = value * item
    final.append(value)