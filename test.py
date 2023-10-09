list = [3,2,1,0]

convert_val = 2


total_water = 0
for item in list:
    water = convert_val - item
    if water < 0:
        pass
    else:
        total_water += water

print(total_water)