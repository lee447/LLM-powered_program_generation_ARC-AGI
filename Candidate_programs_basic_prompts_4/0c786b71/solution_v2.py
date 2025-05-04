def solve(grid: list[list[int]]) -> list[list[int]]:
    h = len(grid)
    w = len(grid[0])
    A = [[grid[h-1-i][w-1-j] for j in range(w)] for i in range(h)]
    B = [row[::-1] for row in A]
    C = A[::-1]
    D = [row[::-1] for row in C]
    return [A[i] + B[i] for i in range(h)] + [C[i] + D[i] for i in range(h)]