from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    w = len(grid[0])
    out = [[0]*w for _ in range(h)]
    for i in range(h):
        seq = [x for x in grid[i] if x != 0]
        if not seq:
            continue
        start = w - len(seq)
        for k, v in enumerate(seq):
            out[i][start + k] = v
    return out