from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    res = [row[:] for row in grid]
    for y in range(h):
        c = 0
        while c < w:
            if grid[y][c] == 6:
                start = c
                while c < w and grid[y][c] == 6:
                    c += 1
                end = c - 1
                width = end - start + 1
                right = start + width
                if right + width <= w and all(grid[y][x] != 6 for x in range(right, right + width)):
                    sl = [grid[y][x] for x in range(right, right + width)]
                    for i, v in enumerate(reversed(sl)):
                        res[y][start + i] = v
                else:
                    left = start - width
                    sl = [grid[y][x] for x in range(left, start)]
                    for i, v in enumerate(reversed(sl)):
                        res[y][start + i] = v
            else:
                c += 1
    return res