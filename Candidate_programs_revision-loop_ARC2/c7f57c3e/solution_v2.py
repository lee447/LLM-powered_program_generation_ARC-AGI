def solve(grid):
    h, w = len(grid), len(grid[0])
    bg = grid[0][0]
    def neighbors(r, c):
        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
            rr, cc = r+dr, c+dc
            if 0 <= rr < h and 0 <= cc < w:
                yield rr, cc
    seen = [[False]*w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if not seen[i][j] and grid[i][j] != bg:
                col = grid[i][j]
                stack = [(i,j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r,c))
                    for rr, cc in neighbors(r,c):
                        if not seen[rr][cc] and grid[rr][cc] == col:
                            seen[rr][cc] = True
                            stack.append((rr,cc))
                comps.append((min(r for r,c in cells), min(c for r,c in cells), col, cells))
    comps.sort()
    n = len(comps)
    res = [row[:] for row in grid]
    for idx, (_,_,col,cells) in enumerate(comps):
        nc = comps[(idx+1)%n][2]
        for r,c in cells:
            res[r][c] = nc
    return res