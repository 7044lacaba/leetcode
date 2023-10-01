numbers = [2,3,4]
target = 6

index_1 = 0
index_2 = 1

dict = {}

while index_1 != index_2:

    # Add first into dict
    value = target - numbers[index_1]
    dict[value] = index_1

    # Check item at index 2
    if numbers[index_2] in dict:
        ret = [(dict[numbers[index_2]] + 1), (index_2 +1)]
        print(ret)
    
    # Increment
    if index_2 + 1 == len(numbers):
        index_1 += 1
    else:
        index_1 += 1
        index_2 += 1

