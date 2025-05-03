def solve(grid: list[list[int]]) -> list[list[int]]:
    h = len(grid)
    w = len(grid[0])
    q = [[grid[h-1-i][w-1-j] for j in range(w)] for i in range(h)]
    ext = [row + row[::-1] for row in q]
    return ext + ext[::-1]