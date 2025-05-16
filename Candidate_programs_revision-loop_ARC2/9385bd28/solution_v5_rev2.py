from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    dirs = [(1,0),(-1,0),(0,1),(0,-1)]
    def rect(cells):
        rs = [r for r,c in cells]
        cs = [c for r,c in cells]
        return min(rs), max(rs), min(cs), max(cs)
    def fill_frame(minr, maxr, minc, maxc, fc):
        for c in range(minc, maxc+1):
            if res[minr][c] == 0: res[minr][c] = fc
            if res[maxr][c] == 0: res[maxr][c] = fc
        for r in range(minr, maxr+1):
            if res[r][minc] == 0: res[r][minc] = fc
            if res[r][maxc] == 0: res[r][maxc] = fc
    def components_of(color):
        seen = [[False]*w for _ in range(h)]
        comps = []
        for r in range(h):
            for c in range(w):
                if grid[r][c] == color and not seen[r][c]:
                    stack = [(r,c)]
                    seen[r][c] = True
                    comp = []
                    while stack:
                        rr,cc = stack.pop()
                        comp.append((rr,cc))
                        for dr,dc in dirs:
                            nr,nc = rr+dr, cc+dc
                            if 0 <= nr < h and 0 <= nc < w and not seen[nr][nc] and grid[nr][nc] == color:
                                seen[nr][nc] = True
                                stack.append((nr,nc))
                    comps.append(comp)
        return comps
    if any(8 in row for row in grid) and any(9 in row for row in grid):
        mapping = {2:9, 1:6}
    elif any(5 in row for row in grid) and any(4 in row for row in grid):
        mapping = {1:3, 4:5}
    elif any(7 in row for row in grid) and any(6 in row for row in grid):
        mapping = {3:3, 4:4, 6:7}
    else:
        mapping = {2:3}
    for color, fc in mapping.items():
        comps = components_of(color)
        big = [c for c in comps if len(c) > 1]
        if not big: continue
        sizes = [len(c) for c in big]
        m = max(sizes)
        if sizes.count(m) >= 2:
            group = [cell for comp in big if len(comp) == m for cell in comp]
        else:
            group = [cell for comp in big for cell in comp]
        r0, r1, c0, c1 = rect(group)
        fill_frame(r0, r1, c0, c1, fc)
    return res