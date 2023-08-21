list = [1,2,3,1]

copy = list

for i in range(len(list)):
    current = copy[0]
    copy.pop(0)


    if current in copy:
        print("True")
    else:
        print("False")
