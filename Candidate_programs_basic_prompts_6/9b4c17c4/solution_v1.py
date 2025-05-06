from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    freq = {}
    for row in grid:
        for c in row:
            freq[c] = freq.get(c, 0) + 1
    freq_ex = {c: v for c, v in freq.items() if c != 2}
    bg_colors = sorted(freq_ex, key=lambda c: freq_ex[c], reverse=True)[:2]
    regions = {}
    for bg in bg_colors:
        min_r, max_r, min_c, max_c = h, -1, w, -1
        for r in range(h):
            for c in range(w):
                if grid[r][c] == bg:
                    if r < min_r: min_r = r
                    if r > max_r: max_r = r
                    if c < min_c: min_c = c
                    if c > max_c: max_c = c
        regions[bg] = (min_r, max_r, min_c, max_c)
    res = [list(row) for row in grid]
    for bg, (r1, r2, c1, c2) in regions.items():
        visited = [[False]*w for _ in range(h)]
        for r in range(r1, r2+1):
            for c in range(c1, c2+1):
                if grid[r][c] == 2 and not visited[r][c]:
                    comp = []
                    queue = [(r, c)]
                    visited[r][c] = True
                    while queue:
                        cr, cc = queue.pop(0)
                        comp.append((cr, cc))
                        for dr, dc in ((1,0),(-1,0),(0,1),(0,-1)):
                            nr, nc = cr+dr, cc+dc
                            if r1 <= nr <= r2 and c1 <= nc <= c2 and not visited[nr][nc] and grid[nr][nc] == 2:
                                visited[nr][nc] = True
                                queue.append((nr, nc))
                    min_cr = min(x for x,y in comp)
                    max_cr = max(x for x,y in comp)
                    min_cc = min(y for x,y in comp)
                    max_cc = max(y for x,y in comp)
                    height = max_cr - min_cr + 1
                    width = max_cc - min_cc + 1
                    for (cr, cc) in comp:
                        res[cr][cc] = bg
                    if bg == 1:
                        new_c1 = c2 - width + 1
                    else:
                        new_c1 = c1
                    for dr in range(height):
                        for dc in range(width):
                            res[min_cr+dr][new_c1+dc] = 2
    return res