from collections import Counter

def solve(grid):
    R, C = len(grid), len(grid[0]) if grid else 0
    sep_rows = [r for r in range(R) if grid[r][0] != 0 and all(grid[r][c] == grid[r][0] for c in range(C))]
    sep_cols = [c for c in range(C) if grid[0][c] != 0 and all(grid[r][c] == grid[0][c] for r in range(R))]
    row_colors = {grid[r][0] for r in sep_rows}
    col_colors = {grid[0][c] for c in sep_cols}
    sep = (row_colors & col_colors) and (row_colors & col_colors).pop() or (row_colors or col_colors).pop()
    cnt = Counter()
    for i in range(R-1):
        for j in range(C-1):
            v = grid[i][j]
            if v != 0 and v != sep and grid[i+1][j] == v and grid[i][j+1] == v and grid[i+1][j+1] == v:
                cnt[v] += 1
    if not cnt:
        return []
    width = max(cnt.values())
    items = sorted(cnt.items(), key=lambda x: x[1])
    res = []
    for v, k in items:
        if k <= width:
            row = [v]*k + [0]*(width-k)
            res.append(row)
    return res