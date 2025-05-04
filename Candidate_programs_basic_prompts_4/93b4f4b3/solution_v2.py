from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w2 = len(grid[0])
    w = w2 // 2
    A = [[grid[i][j] for j in range(w)] for i in range(h)]
    visited = [[False] * w for _ in range(h)]
    comps = []
    for i in range(h):
        for j in range(w):
            if A[i][j] == 0 and not visited[i][j]:
                stack = [(i, j)]
                coords = []
                visited[i][j] = True
                r0 = r1 = i
                c0 = c1 = j
                while stack:
                    r, c = stack.pop()
                    coords.append((r, c))
                    if r < r0: r0 = r
                    if r > r1: r1 = r
                    if c < c0: c0 = c
                    if c > c1: c1 = c
                    for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                        rr, cc = r+dr, c+dc
                        if 0 <= rr < h and 0 <= cc < w and A[rr][cc] == 0 and not visited[rr][cc]:
                            visited[rr][cc] = True
                            stack.append((rr, cc))
                comps.append((r0, coords, c0, c1, r1))
    comps.sort(key=lambda x: x[0])
    shape_colors = []
    for r0, coords, c0, c1, r1 in comps:
        cols = set()
        for r in range(r0, r1+1):
            for c in range(c0, c1+1):
                v = grid[r][w + c]
                if v != 0:
                    cols.add(v)
        shape_colors.append(max(cols) if cols else 0)
    sc = sorted(shape_colors)
    k = len(sc)
    shift = sc[0] - 1 if k else 0
    new_colors = [sc[(i+shift) % k] for i in range(k)]
    res = [row[:] for row in A]
    for idx, (_, coords, _, _, _) in enumerate(comps):
        col = new_colors[idx]
        for r, c in coords:
            res[r][c] = col
    return res