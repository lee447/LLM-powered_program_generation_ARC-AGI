from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    maxc = 0
    for r in range(h - 2):
        for c in range(w - 2):
            cnt = 0
            for i in range(3):
                for j in range(3):
                    if grid[r + i][c + j] == 6:
                        cnt += 1
            if cnt > maxc:
                maxc = cnt
    out = [row[:] for row in grid]
    for r in range(h - 2):
        for c in range(w - 2):
            cnt = 0
            for i in range(3):
                for j in range(3):
                    if grid[r + i][c + j] == 6:
                        cnt += 1
            if cnt == maxc:
                for i in range(3):
                    for j in range(3):
                        if out[r + i][c + j] != 6:
                            out[r + i][c + j] = 4
    return out