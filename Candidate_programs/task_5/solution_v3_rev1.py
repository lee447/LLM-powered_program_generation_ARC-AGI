from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(h):
        row = grid[r]
        runs = []
        c = 0
        while c < w:
            if row[c] == 6:
                start = c
                while c < w and row[c] == 6:
                    c += 1
                runs.append((start, c - 1))
            else:
                c += 1
        for i, j in runs:
            n = j - i + 1
            left_val = row[i - 1] if i - 1 >= 0 else None
            right_val = row[j + 1] if j + 1 < w else None
            for k in range(n):
                if left_val is not None and right_val is not None:
                    out[r][i + k] = left_val if k < n // 2 else right_val
                elif left_val is not None:
                    out[r][i + k] = left_val
                elif right_val is not None:
                    out[r][i + k] = right_val
    return out