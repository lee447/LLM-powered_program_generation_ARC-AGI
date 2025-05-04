def solve(grid):
    R, C = len(grid), len(grid[0])
    anchors = []
    for r in range(R - 1):
        for c in range(C - 1):
            if grid[r][c] == 8 and grid[r][c+1] == 8 and grid[r+1][c] == 8 and grid[r+1][c+1] == 8:
                anchors.append((r, c))
    res = []
    for r, c in anchors:
        vec = []
        for dr, dc, sr, sc in [(-1, -1, r-1, c-1), (-1, 1, r-1, c+2), (1, 1, r+2, c+2), (1, -1, r+2, c-1)]:
            val = 0
            rr, cc = sr, sc
            while 0 <= rr < R and 0 <= cc < C:
                if grid[rr][cc] != 0:
                    val = grid[rr][cc]
                    break
                rr += dr
                cc += dc
            vec.append(val)
        res.append(vec)
    return res