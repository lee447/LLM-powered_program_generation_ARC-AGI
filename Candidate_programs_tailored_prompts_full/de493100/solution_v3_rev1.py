from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    seen = [[False]*W for _ in range(H)]
    comps = []
    for i in range(H):
        for j in range(W):
            if not seen[i][j]:
                col = grid[i][j]
                stack = [(i, j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < H and 0 <= nc < W and not seen[nr][nc] and grid[nr][nc] == col:
                            seen[nr][nc] = True
                            stack.append((nr, nc))
                rs = [r for r,_ in cells]
                cs = [c for _,c in cells]
                comps.append((col, len(cells), min(rs), max(rs), min(cs), max(cs)))
    cand = [c for c in comps if c[0] in (6,7)]
    col2, _, rmin, rmax, cmin, cmax = max(cand, key=lambda x: x[1])
    grey_rows = set()
    for r in range(H):
        for c in range(cmin, cmax+1):
            if grid[r][c] == 5:
                grey_rows.add(r)
    grey_cols = set()
    for r in range(rmin, rmax+1):
        for c in range(W):
            if grid[r][c] == 5:
                grey_cols.add(c)
    if (rmax-rmin) < (cmax-cmin):
        above = [r for r in grey_rows if r < rmin]
        below = [r for r in grey_rows if r > rmax]
        if above:
            top = max(above) + 1
            bot = rmin
        else:
            top = rmax + 1
            bot = min(below)
        return [row[cmin:cmax+1] for row in grid[top:bot]]
    else:
        lefts = [c for c in grey_cols if c < cmin]
        rights = [c for c in grey_cols if c > cmax]
        if lefts:
            left = max(lefts) + 1
            right = cmin
        else:
            left = cmax + 1
            right = min(rights)
        return [row[left:right] for row in grid[rmin:rmax+1]]