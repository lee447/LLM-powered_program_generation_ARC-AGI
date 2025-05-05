from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    rows, cols = len(grid), len(grid[0])
    ycol = next(c for c in range(cols) if any(grid[r][c] == 4 for r in range(rows)))
    out = [[0]*4 for _ in range(rows)]
    for r in range(rows):
        left = grid[r][:ycol]
        right = grid[r][ycol+1:]
        li = ri = 0
        i = 0
        while i < len(left):
            if left[i] == 8:
                if li < 2:
                    out[r][li] = 2
                li += 1
                while i < len(left) and left[i] == 8:
                    i += 1
                continue
            i += 1
        i = 0
        while i < len(right):
            if right[i] == 5:
                if ri < 2:
                    out[r][2+ri] = 2
                ri += 1
                while i < len(right) and right[i] == 5:
                    i += 1
                continue
            i += 1
    return out