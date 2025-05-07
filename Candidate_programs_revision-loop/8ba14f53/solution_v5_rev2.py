from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    rows = [(0, 0), (1, 1), (2, h - 1)]
    cols = [(0, w // 3 - 1), (w // 3, 2 * w // 3 - 1), (2 * w // 3, w - 1)]
    out = [[0] * 3 for _ in range(3)]
    for i, (r0, r1) in enumerate(rows):
        for j, (c0, c1) in enumerate(cols):
            seen = set()
            for rr in range(r0, r1 + 1):
                for cc in range(c0, c1 + 1):
                    v = grid[rr][cc]
                    if v:
                        seen.add(v)
                        if len(seen) > 1:
                            break
                if len(seen) > 1:
                    break
            if len(seen) == 1:
                out[i][j] = seen.pop()
    return out