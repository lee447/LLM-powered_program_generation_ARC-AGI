from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    cnt = {}
    for r in range(h):
        for c in range(w):
            cnt[grid[r][c]] = cnt.get(grid[r][c], 0) + 1
    bg = max(cnt, key=lambda k: cnt[k])
    shapes = {}
    for r in range(h):
        for c in range(w):
            if grid[r][c] != bg:
                shapes.setdefault(grid[r][c], []).append((r, c))
    items = []
    for color, pts in shapes.items():
        minr = min(r for r, _ in pts)
        minc = min(c for _, c in pts)
        items.append((minr, minc, color, pts))
    items.sort(key=lambda x: (x[0], x[1]))
    out = [[bg] * w for _ in range(h)]
    for i, (_, _, color, pts) in enumerate(items):
        shift = -1 if i % 2 == 0 else 1
        for r, c in pts:
            nc = c + shift
            if 0 <= nc < w:
                out[r][nc] = color
    return out