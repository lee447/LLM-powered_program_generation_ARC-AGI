from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    best_line = []
    for dr, dc in [(1, 1), (1, -1)]:
        for r in range(h):
            for c in range(w):
                if grid[r][c] != 0:
                    continue
                pr, pc = r - dr, c - dc
                if 0 <= pr < h and 0 <= pc < w and grid[pr][pc] == 0:
                    continue
                line = []
                rr, cc = r, c
                while 0 <= rr < h and 0 <= cc < w and grid[rr][cc] == 0:
                    line.append((rr, cc))
                    rr += dr
                    cc += dc
                if len(line) > len(best_line):
                    best_line = line
    res = [row[:] for row in grid]
    for r, c in best_line:
        res[r][c] = 8
    return res