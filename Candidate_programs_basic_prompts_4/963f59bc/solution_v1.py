from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    counts = {}
    for i in range(H):
        for j in range(W):
            v = grid[i][j]
            if v != 0:
                counts[v] = counts.get(v, 0) + 1
    template_color = max((c for c in counts if counts[c] > 1), key=lambda c: counts[c])
    tpl = [(i, j) for i in range(H) for j in range(W) if grid[i][j] == template_color]
    minr = min(r for r, _ in tpl)
    maxr = max(r for r, _ in tpl)
    rows = {}
    for r, c in tpl:
        rows.setdefault(r, []).append(c)
    for r in range(minr, maxr+1):
        if len(rows.get(r, [])) == 1:
            pivot_r = r
            pivot_c = rows[r][0]
            break
    for i in range(H):
        for j in range(W):
            v = grid[i][j]
            if v != 0 and v != template_color and counts.get(v,0) == 1:
                dr = i - pivot_r
                dc = j - pivot_c
                for tr, tc in tpl:
                    nr, nc = tr + dr, tc + dc
                    if 0 <= nr < H and 0 <= nc < W:
                        out[nr][nc] = v
    return out