from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = max(r for r, row in enumerate(grid) for v in row if v == 5) + 1
    out = [row[:] for row in grid]
    for r in range(len(grid)):
        non5 = [c for c,v in enumerate(grid[r]) if v not in (0,5)]
        if not non5:
            continue
        # above the anchor: only rows with r < h-1 can keep singletons
        if r < h:
            if r < h-1:
                continue
            # in the last row of the 5-block no action
            if r == h-1:
                continue
        # below the anchor: drop exactly one cell in each 4-row band, the second band, etc.
        else:
            band = (r - h) // (h - 1) if h > 1 else 0
            if band == 0:
                continue
            if (r - h) % (h - 1) != band - 1:
                continue
        c = max(non5)
        out[r][c] = 0
    return out