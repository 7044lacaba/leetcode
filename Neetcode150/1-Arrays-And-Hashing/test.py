board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]



for row in range(len(board)):
    for collumn in range(len(board)):
        value = board[row][collumn]

        # Check if there is a value in the node
        if value == ".":
            pass
        else:

            # Check row for similar values
            counter = 0
            for item in board[row]:
                if item == value:
                    counter += 1
            if counter != 1:
                print("False")
            
            # Check collumn for similar values
            counter = 0
            for i in range(len(board)):
                if value == board[i][collumn]:
                    counter += 1
            if counter != 1:
                print("False")

            # Check box for similar values
            
            if row == 0 or row == 1 or row == 2:
                r = range(0,3)
            elif row == 3 or row == 4 or row == 5:
                r = range(3,6)
            else:
                r = range(6,9)
            
            if collumn == 0 or collumn == 1 or collumn == 2:
                c = range(0,3)
            elif collumn == 3 or collumn == 4 or collumn == 5:
                c = range(3,6)
            else:
                c = range(6,9)
            

            counter = 0 
            for i in r:
                for j in c:
                    if board[i][j] == value:
                        counter += 1
            if counter > 1:
                 print("False")