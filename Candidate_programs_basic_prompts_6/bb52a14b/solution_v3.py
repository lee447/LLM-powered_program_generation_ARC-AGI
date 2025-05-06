from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    R, C = len(grid), len(grid[0])
    best_total = -1
    best_diff = -10**9
    br = bc = 0
    for r in range(R-2):
        for c in range(C-2):
            ones = eights = 0
            for dr in range(3):
                for dc in range(3):
                    v = grid[r+dr][c+dc]
                    if v == 1:
                        ones += 1
                    elif v == 8:
                        eights += 1
            total = ones + eights
            diff = ones - eights
            if total > best_total or (total == best_total and diff > best_diff):
                best_total = total
                best_diff = diff
                br, bc = r, c
    out = [row[:] for row in grid]
    for dr in range(3):
        for dc in range(3):
            if out[br+dr][bc+dc] == 0:
                out[br+dr][bc+dc] = 4
    return out