from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    visited = [[False]*w for _ in range(h)]
    shapes = []
    for i in range(h):
        for j in range(w):
            if grid[i][j] == 3 and not visited[i][j]:
                stack = [(i, j)]
                coords = []
                visited[i][j] = True
                while stack:
                    r, c = stack.pop()
                    coords.append((r, c))
                    for dr, dc in ((1, 0), (-1, 0), (0, 1), (0, -1)):
                        nr, nc = r+dr, c+dc
                        if 0 <= nr < h and 0 <= nc < w and grid[nr][nc] == 3 and not visited[nr][nc]:
                            visited[nr][nc] = True
                            stack.append((nr, nc))
                rs = [r for r, c in coords]
                cs = [c for r, c in coords]
                minr, maxr, minc, maxc = min(rs), max(rs), min(cs), max(cs)
                rel = [(r-minr, c-minc) for r, c in coords]
                shapes.append((minr, minc, maxr, maxc, rel))
    h_shape = next(s for s in shapes if (s[3]-s[1]) > (s[2]-s[0]))
    v_shape = next(s for s in shapes if s is not h_shape)
    res = [row[:] for row in grid]
    # horizontal copy
    minr, minc, maxr, maxc, rel = h_shape
    height = maxr-minr+1
    width = maxc-minc+1
    dest_r = minr
    dest_c = maxc + 2
    ok = True
    for dr, dc in rel:
        rr, cc = dest_r+dr, dest_c+dc
        if not (0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0):
            ok = False; break
    if not ok:
        dest_c = minc - width - 1
    for dr, dc in rel:
        res[dest_r+dr][dest_c+dc] = 1
    # vertical copy
    minr, minc, maxr, maxc, rel = v_shape
    height = maxr-minr+1
    width = maxc-minc+1
    dest_c = minc
    dest_r = minr - height - 1
    ok = dest_r >= 0
    if ok:
        for dr, dc in rel:
            rr, cc = dest_r+dr, dest_c+dc
            if not (0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0):
                ok = False; break
    if not ok:
        dest_r = maxr + 2
    for dr, dc in rel:
        res[dest_r+dr][dest_c+dc] = 8
    return res