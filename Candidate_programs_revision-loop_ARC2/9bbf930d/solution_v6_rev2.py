from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    def stripe_color(r):
        cnt = {}
        for v in grid[r][2:]:
            if v not in (7, 6):
                cnt[v] = cnt.get(v, 0) + 1
        if not cnt:
            return None
        return max(cnt, key=cnt.get)
    for i in range(h - 2):
        c1 = stripe_color(i)
        c2 = stripe_color(i + 2)
        if c1 is not None and c1 == c2:
            m = i + 1
            out[m][0] = 7
            if grid[m][w - 1] == 7:
                out[m][w - 1] = 6
    return out