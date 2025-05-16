from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    g = [row[:] for row in grid]
    cnt = {}
    for r in range(h):
        for c in range(w):
            v = g[r][c]
            if v:
                cnt[v] = cnt.get(v, 0) + 1
    cols = sorted(cnt.items(), key=lambda x: -x[1])
    B = cols[0][0]
    S = cols[1][0] if len(cols) > 1 else None
    def fill_gap(color):
        changed = True
        while changed:
            changed = False
            for r in range(h):
                for c in range(w-2):
                    if g[r][c]==color and g[r][c+2]==color and g[r][c+1]==0:
                        g[r][c+1] = color
                        changed = True
            for c in range(w):
                for r in range(h-2):
                    if g[r][c]==color and g[r+2][c]==color and g[r+1][c]==0:
                        g[r+1][c] = color
                        changed = True
    if S is not None:
        fill_gap(S)
    return g