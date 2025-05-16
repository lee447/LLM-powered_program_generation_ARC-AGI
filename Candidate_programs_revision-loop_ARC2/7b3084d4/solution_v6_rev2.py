from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    seen = [[False] * m for _ in range(n)]
    comps = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != 0 and not seen[i][j]:
                clr = grid[i][j]
                stack = [(i, j)]
                seen[i][j] = True
                cells = []
                while stack:
                    r, c = stack.pop()
                    cells.append((r, c))
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < n and 0 <= cc < m and not seen[rr][cc] and grid[rr][cc] == clr:
                            seen[rr][cc] = True
                            stack.append((rr, cc))
                minr = min(r for r,c in cells)
                maxr = max(r for r,c in cells)
                minc = min(c for r,c in cells)
                maxc = max(c for r,c in cells)
                rc = (minr + maxr) / 2
                cc = (minc + maxc) / 2
                br = 0 if rc < n/2 else 1
                bc = 1 if cc < m/2 else 0
                comps.append((cells, clr, minr, maxr, minc, maxc, br, bc))
    widths = [maxc - minc + 1 for cells, clr, minr, maxr, minc, maxc, br, bc in comps if len(cells) > 1]
    p = min(widths)
    out = [[0] * (2*p) for _ in range(2*p)]
    for cells, clr, minr, maxr, minc, maxc, br, bc in comps:
        h = maxr - minr
        w = maxc - minc
        pat = [[0]*p for _ in range(p)]
        if len(cells) == 1:
            rr = p//2
            cc = p//2
            pat[rr][cc] = clr
        else:
            for r, c in cells:
                rr = round((r - minr) * (p-1) / h) if h > 0 else p//2
                cc = round((c - minc) * (p-1) / w) if w > 0 else p//2
                pat[rr][cc] = clr
        obc = 1 - bc
        obr = br
        ro, co = obr*p, obc*p
        for i in range(p):
            for j in range(p):
                if pat[i][j]:
                    out[ro+i][co+j] = pat[i][j]
    return out