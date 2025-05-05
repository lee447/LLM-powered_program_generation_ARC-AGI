from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    gray = 5
    n = 3
    stripe_w = w // n
    zones = [list(range(i * stripe_w, (i + 1) * stripe_w)) for i in range(n)]
    counts = [sum(grid[r][c] == gray for r in range(h) for c in zone) for zone in zones]
    avail = sorted({grid[r][c] for r in range(h) for c in range(w) if grid[r][c] not in (0, gray)})
    if len(avail) < n:
        cand = [i for i in range(1, 10) if i != gray and i not in avail]
        avail += cand[: n - len(avail)]
    order = sorted(range(n), key=lambda i: counts[i], reverse=True)
    assign = [0] * n
    for k, i in enumerate(order):
        assign[i] = avail[k]
    out = [[0] * w for _ in range(h)]
    for i, zone in enumerate(zones):
        c = assign[i]
        for r in range(h):
            for col in zone:
                out[r][col] = c
    return out