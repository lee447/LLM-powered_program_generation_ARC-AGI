def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = 8
    fill = 3
    rows = []
    for i in range(h-2):
        if any(grid[i][j] != bg and grid[i][j] != 6 for j in range(w)) and all(grid[i+1][j] != bg and grid[i+1][j] != 6 for j in range(w)) and all(grid[i+2][j] != bg and grid[i+2][j] != 6 for j in range(w)):
            rows.append(i)
    cols = []
    r0 = rows[0]
    for j in range(w-2):
        if grid[r0][j] != bg and grid[r0][j] != 6 and grid[r0][j+1] != bg and grid[r0][j+1] != 6 and grid[r0][j+2] != bg and grid[r0][j+2] != 6:
            cols.append(j)
    def outline(r0, c0):
        for dj in range(3):
            if grid[r0-1][c0+dj] == bg: grid[r0-1][c0+dj] = fill
            if grid[r0+3][c0+dj] == bg: grid[r0+3][c0+dj] = fill
        for di in range(3):
            if grid[r0+di][c0-1] == bg: grid[r0+di][c0-1] = fill
            if grid[r0+di][c0+3] == bg: grid[r0+di][c0+3] = fill
    for idx, r0 in enumerate(rows):
        for c0 in cols:
            vs = [grid[r0+i][c0+j] for i in range(3) for j in range(3)]
            if vs.count(vs[0]) == 9:
                outline(r0, c0)
    return grid