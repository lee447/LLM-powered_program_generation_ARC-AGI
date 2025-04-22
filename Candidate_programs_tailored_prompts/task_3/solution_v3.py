def solve(grid):
    h, w = len(grid), len(grid[0])
    zero_rows = [r for r in range(h) if all(grid[r][c] == 0 for c in range(w))]
    bands = [(zero_rows[i] + 1, zero_rows[i+1] - 1) for i in range(len(zero_rows)-1)]
    patterns = [
        [[0,1,0],[1,1,1],[0,1,0]],
        [[1,0,0],[0,1,0],[0,0,1]],
        [[0,0,1],[0,1,0],[1,0,0]],
    ]
    out = [row[:] for row in grid]
    for top, bot in bands:
        row = top
        cols0 = [c for c in range(w) if grid[row][c] and (c==0 or grid[row][c-1]==0)]
        for i, c0 in enumerate(cols0):
            col0 = c0
            col1 = col0+1
            color = grid[row][col0]
            pat = patterns[i]
            for dr in range(3):
                for dc in range(3):
                    if pat[dr][dc]:
                        out[top+dr][col1+dc] = color
    return out