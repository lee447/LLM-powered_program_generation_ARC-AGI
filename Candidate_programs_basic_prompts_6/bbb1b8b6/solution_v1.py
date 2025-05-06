from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h = len(grid)
    split = next(c for c, v in enumerate(grid[0]) if v == 5)
    left = [row[:split] for row in grid]
    right = [row[split+1:] for row in grid]
    w = len(left[0])
    left_zeros = {(r, c) for r in range(h) for c in range(w) if left[r][c] == 0}
    right_nonzeros = {(r, c) for r in range(h) for c in range(w) if right[r][c] != 0}
    if right_nonzeros == left_zeros:
        out = [[0]*w for _ in range(h)]
        for r in range(h):
            for c in range(w):
                if left[r][c] != 0:
                    out[r][c] = left[r][c]
                elif right[r][c] != 0:
                    out[r][c] = right[r][c]
                else:
                    out[r][c] = 0
        return out
    else:
        return [row[:] for row in left]