from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    seg = w // 3
    colors = [0] * 3
    for s in range(3):
        region = [row[s*seg:(s+1)*seg] for row in grid]
        total = sum(val == 5 for row in region for val in row)
        if total == 1:
            c = 4
        elif total == h * seg - 1:
            c = 3
        elif total == seg and region[0].count(5) == seg:
            c = 6
        elif total == seg and region[-1].count(5) == seg:
            c = 1
        else:
            c = 9
        colors[s] = c
    return [[colors[j // seg] for j in range(w)] for _ in range(h)]