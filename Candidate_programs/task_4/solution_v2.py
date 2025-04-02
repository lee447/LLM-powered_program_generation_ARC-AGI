from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    out = [row[:] for row in grid]
    n = len(out)
    if n == 0: 
        return out
    m = len(out[0])
    blues = [i for i in range(min(n, m)) if out[i][i] == 1]
    if len(blues) < 2:
        return out
    gap = blues[1] - blues[0]
    pos = blues[-1] + gap
    while pos < min(n, m):
        if out[pos][pos] != 1:
            out[pos][pos] = 2
        pos += gap
    return out