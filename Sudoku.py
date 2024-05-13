
import copy


def getSquareCorners(pos):
    row, col = pos[0], pos[1]
    if 0 <= row < 3 and 0 <= col < 3:
        startRow, endRow = 0, 3
        startCol, endCol = 0, 3
    if 0 <= row < 3 and 3 <= col < 6:
        startRow, endRow = 0, 3
        startCol, endCol = 3, 6
    if 0 <= row < 3 and 6 <= col < 9:
        startRow, endRow = 0, 3
        startCol, endCol = 6, 9
    if 3 <= row < 6 and 0 <= col < 3:
        startRow, endRow = 3, 6
        startCol, endCol = 0, 3
    if 3 <= row < 6 and 3 <= col < 6:
        startRow, endRow = 3, 6
        startCol, endCol = 3, 6
    if 3 <= row < 6 and 6 <= col < 9:
        startRow, endRow = 3, 6
        startCol, endCol = 6, 9
    if 6 <= row < 9 and 0 <= col < 3:
        startRow, endRow = 6, 9
        startCol, endCol = 0, 3
    if 6 <= row < 9 and 3 <= col < 6:
        startRow, endRow = 6, 9
        startCol, endCol = 3, 6
    if 6 <= row < 9 and 6 <= col < 9:
        startRow, endRow = 6, 9
        startCol, endCol = 6, 9
    return [startRow, endRow, startCol, endRow]


def getEmptyPosition(board):
    pos = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '.':
                return [i, j]
    return pos


def getPotentialNums(position, board):
    nums = []
    checkNums = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    rows = board[position[0]]
    cols = [i[position[1]] for i in board]
    squareCorners = getSquareCorners(position)
    square = [board[i][j] for i in range(squareCorners[0], squareCorners[1]) for j in range(squareCorners[2], squareCorners[3])]
    for i in checkNums:
        if i not in rows and i not in cols and i not in square:
            nums.append(i)
    return nums


def isValidSudoku(board):
    if not getEmptyPosition(board):
        return board
    else:
        pos = getEmptyPosition(board)
        nums = getPotentialNums(pos, board)
        if nums:
            for i in nums:
                temp_board = copy.deepcopy(board)
                temp_board[pos[0]][pos[1]] = i
                print(temp_board)
                isValidSudoku(temp_board)




boardSud = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

boardSud1 = [["5", "3", "4", "6", "7", "8", "9", "1", "."]
    , ["6", "7", "2.", "1", "9", "5", "3", "4", "8"]
    , ["1", "9", "8", "3", "4", "2", "5", "6", "."]
    , ["8", "5", "9", "7", "6", "1", "4", ".", "3"]
    , ["4", "2", "6", "8", "5", "3", "7.", ".", "1"]
    , ["7", "1", "3.", "9.", "2", "4", "8", ".", "6"]
    , ["9", "6", "1", "5", "3", "7", "2", "8", "."]
    , ["2", "8", "7", "4", "1", "9", "6", ".", "5"]
    , ["3", "4", "5", "2", "8", "6", ".", "7", "9"]]

# print(getPotentialNums([4, 4], boardSud))

print(isValidSudoku(boardSud))

# print(isValidSudoku([['4', '4', '4'],
#                      ['4', '4', '4'],
#                      ['4', '4', '4']]))
