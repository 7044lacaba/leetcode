nums = [1,2,3,4]

final = []
for i, item in enumerate(nums):
    temp = nums.copy()
    temp.pop(i)
    value = 1
    for item in temp:
        value = value * item
    final.append(value)

print(final)