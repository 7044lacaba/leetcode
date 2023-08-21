list = [1,2,3,1]

copy = list

for i, item in enumerate(list):
    copy.pop(0)
    print(copy)