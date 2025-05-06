from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    visited = [[False]*cols for _ in range(rows)]
    comps = []
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] != 0 and not visited[r][c]:
                comp = []
                stack = [(r, c)]
                visited[r][c] = True
                while stack:
                    i, j = stack.pop()
                    comp.append((i, j))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        ni, nj = i + dr, j + dc
                        if 0 <= ni < rows and 0 <= nj < cols and not visited[ni][nj] and grid[ni][nj] != 0:
                            visited[ni][nj] = True
                            stack.append((ni, nj))
                comps.append(comp)
    rects = []
    for comp in comps:
        rs = [p[0] for p in comp]
        cs = [p[1] for p in comp]
        minr, maxr, minc, maxc = min(rs), max(rs), min(cs), max(cs)
        if (maxr - minr + 1) * (maxc - minc + 1) == len(comp):
            rects.append((len(comp), minr, maxr, minc, maxc))
    _, br0, br1, bc0, bc1 = max(rects, key=lambda x: x[0])
    mapping = {}
    for comp in comps:
        if len(comp) == 2:
            rs = [p[0] for p in comp]
            cs = [p[1] for p in comp]
            minr, maxr, minc, maxc = min(rs), max(rs), min(cs), max(cs)
            if minr == maxr and maxc - minc == 1:
                if not (br0 <= minr <= br1 and bc0 <= minc <= bc1):
                    left = grid[minr][minc]
                    right = grid[minr][maxc]
                    mapping[right] = left
    res = []
    for r in range(br0, br1 + 1):
        row = []
        for c in range(bc0, bc1 + 1):
            v = grid[r][c]
            row.append(mapping.get(v, v))
        res.append(row)
    return res