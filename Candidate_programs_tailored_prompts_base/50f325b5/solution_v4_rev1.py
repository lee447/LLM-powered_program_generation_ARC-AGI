from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    for r in range(h):
        c = 0
        while c < w:
            v = grid[r][c]
            if v in (3, 8):
                length = 1
                while c + length < w and grid[r][c + length] == v:
                    length += 1
                if length >= 2:
                    new = 8 if v == 3 else 3
                    for i in range(length):
                        out[r][c + i] = new
                c += length
            else:
                c += 1
    return out