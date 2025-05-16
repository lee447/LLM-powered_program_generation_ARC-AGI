from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    C = grid[0][0]
    seg = (h - 2) // 3
    blocks = [(2, 2 + seg), (2 + seg, 2 + 2 * seg), (2 + 2 * seg, h)]
    idx = None
    for i, (r0, r1) in enumerate(blocks):
        for r in range(r0, r1):
            if C in grid[r]:
                idx = i
                break
        if idx is not None:
            break
    if idx is None:
        return grid
    new = [[0] * w for _ in range(h)]
    for c in range(w):
        new[0][c] = grid[0][c]
    for r in range(1, h):
        new[r][0] = grid[r][0]
    for i, (r0, r1) in enumerate(blocks):
        src0, src1 = blocks[(i + idx) % 3]
        for dr, r in enumerate(range(r0, r1)):
            sr = src0 + dr
            if sr < src1:
                for c in range(1, w):
                    new[r][c] = grid[sr][c]
    return new