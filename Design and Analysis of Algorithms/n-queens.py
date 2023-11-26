def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True

def print_solution(board):
    for row in board:
        print(' '.join(['Q' if col == 1 else '.' for col in row]))
    print()

def solve_n_queens(board, row, n, count):
    if row == n:
        print_solution(board)
        count[0] += 1
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            solve_n_queens(board, row + 1, n, count)
            board[row][col] = 0

n = int(input("Enter the value of N for N-Queens: "))
board = [[0] * n for _ in range(n)]
count = [0]
solve_n_queens(board, 0, n, count)
print(f"Number of solutions: {count[0]}")
