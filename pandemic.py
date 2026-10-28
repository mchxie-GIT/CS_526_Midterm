import sys


def spread_infection(board):
    n = len(board)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while True:
        new_infections = []

        for row in range(n):
            for col in range(n):
                if board[row][col] == 1:
                    continue

                neighbors = 0
                for dr, dc in directions:
                    r = row + dr
                    c = col + dc
                    if 0 <= r < n and 0 <= c < n:
                        neighbors += board[r][c]

                if neighbors >= 2:
                    new_infections.append((row, col))

        if not new_infections:
            break

        # Apply changes after checking the whole board for this day.
        for row, col in new_infections:
            board[row][col] = 1


def main():
    with open(sys.argv[1]) as file:
        n = int(file.readline())
        board = [[0 for col in range(n)] for row in range(n)]
        for line in file:
            row, col = map(int, line.split())
            board[row][col] = 1

    spread_infection(board)

    for row in board:
        if 0 in row:
            print("There are healthy counties left")
            return

    print("There are no healthy counties left")


if __name__ == "__main__":
    main()
