from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    best = -1
    br = bc = 0
    for r in range(h - 2):
        for c in range(w - 2):
            cnt = 0
            for i in range(3):
                for j in range(3):
                    if grid[r + i][c + j] == 6:
                        cnt += 1
            if cnt > best:
                best = cnt
                br, bc = r, c
            elif cnt == best and r == br and c > bc:
                bc = c
    out = [row[:] for row in grid]
    for i in range(3):
        for j in range(3):
            if out[br + i][bc + j] != 6:
                out[br + i][bc + j] = 4
    return out