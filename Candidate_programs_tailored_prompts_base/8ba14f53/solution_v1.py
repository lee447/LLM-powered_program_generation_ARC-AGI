from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    zero_cols = [all(grid[r][c] == 0 for r in range(H)) for c in range(W)]
    regions = []
    c = 0
    while c < W:
        while c < W and zero_cols[c]:
            c += 1
        if c >= W:
            break
        start = c
        while c < W and not zero_cols[c]:
            c += 1
        regions.append((start, c))
    def extract_border(r0, r1, c0, c1):
        top = next(r for r in range(r0, r1) if all(grid[r][c] != 0 for c in range(c0, c1)))
        bottom = next(r for r in range(r1-1, r0-1, -1) if all(grid[r][c] != 0 for c in range(c0, c1)))
        choose = bottom if all(grid[bottom][c] != 0 for c in range(c0, c1)) else top
        vals = [grid[choose][c] for c in range(c0, c1)]
        return vals[:3] + [0] * max(0, 3 - (c1 - c0))
    def extract_top(r0, r1, c0, c1):
        top = next(r for r in range(r0, r1) if any(grid[r][c] != 0 for c in range(c0, c1)))
        vals = [grid[top][c] for c in range(c0, c1)]
        return vals[:3] + [0] * max(0, 3 - (c1 - c0))
    (a0, a1), (b0, b1) = regions[0], regions[1]
    rowsA = [r for r in range(H) if any(grid[r][c] != 0 for c in range(a0, a1))]
    rowsB = [r for r in range(H) if any(grid[r][c] != 0 for c in range(b0, b1))]
    rA0, rA1 = rowsA[0], rowsA[-1] + 1
    rB0, rB1 = rowsB[0], rowsB[-1] + 1
    topA = extract_top(rA0, rA1, a0, a1)
    bordB = extract_border(rB0, rB1, b0, b1)
    return [topA, bordB, [0, 0, 0]]