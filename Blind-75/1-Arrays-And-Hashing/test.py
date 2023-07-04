

nums = [4,4,1,1,1,1,2,2,2,3]


nums = sorted(nums)

print(nums)


dict = {}
        
for num in nums:
    dict[num] = dict.get(num, 0) + 1


print(dict)
k = 2
list = [0] * k
print(list)

#for item in dict:
#    for spot in list:
#        if dict[item] > spot