from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    segments = []
    for j in range(w):
        i = 0
        while i < h:
            if grid[i][j] != 0:
                start = i
                i += 1
                while i < h and grid[i][j] != 0:
                    i += 1
                end = i - 1
                length = end - start + 1
                if length >= 3 and grid[start][j] == grid[end][j]:
                    bc = grid[start][j]
                    ic = grid[start+1][j]
                    if ic != bc:
                        ok = True
                        for k in range(start+1, end):
                            if grid[k][j] != ic:
                                ok = False
                                break
                        if ok:
                            segments.append((length, j, start, end, bc))
            else:
                i += 1
    if segments:
        max_len = max(s[0] for s in segments)
        candidates = [s for s in segments if s[0] == max_len]
        _, cj, cs, ce, ccol = min(candidates, key=lambda x: x[1])
        for r in range(cs+1, ce):
            grid[r][cj] = ccol
    return grid