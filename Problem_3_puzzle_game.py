import sys

def is_valid(board, symbols):
    n = len(board)
    size = int(n ** 0.5)
    
    #Check allowed symbols and duplicates in each row
    for row in board:
        seen = set()
        for symbol in row:
            if symbol == ".":
                continue
            if symbol not in symbols or symbol in seen:
                return False
            seen.add(symbol)

    #Check each column
    for col in range(n):
        seen = set()
        for row in range(n):
            symbol = board[row][col]
            if symbol == ".":
                continue
            if symbol in seen:
                return False
            seen.add(symbol)

    #Check each square sub-board
    for start_row in range(0, n, size):
        for start_col in range(0, n, size):
            seen = set()
            for row in range(start_row, start_row + size):
                for col in range(start_col, start_col + size):
                    symbol = board[row][col]
                    if symbol == ".":
                        continue
                    if symbol in seen:
                        return False
                    seen.add(symbol)

    return True

def main():
    with open(sys.argv[1]) as file:
        n = int(file.readline())
        symbols = [value.strip() for value in file.readline().split(",")]
        board = []
        for row in range(n):
            values = file.readline().strip().split(",")
            board.append([value.strip() for value in values])

    if is_valid(board, symbols):
        print("The board is valid")
    else:
        print("The board is invalid")

if __name__ == "__main__":
    main()
