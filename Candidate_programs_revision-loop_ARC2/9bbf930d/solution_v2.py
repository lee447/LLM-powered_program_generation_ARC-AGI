def solve(grid):
    h, w = len(grid), len(grid[0])
    out = [row[:] for row in grid]
    def stripe_color(r):
        cnt = {}
        for v in grid[r][2:]:
            if v not in (7,6):
                cnt[v] = cnt.get(v,0) + 1
        if not cnt: return None
        return max(cnt, key=cnt.get)
    for i in range(h-2):
        c1 = stripe_color(i)
        c2 = stripe_color(i+2)
        if c1 is not None and c1 == c2:
            b = i+1
            ok = True
            for j in range(2, w):
                if grid[b][j] != 7:
                    ok = False
                    break
            if ok:
                out[b][0] = 7
                j = max(j for j in range(2, w) if grid[b][j] == 7)
                out[b][j] = 6
    return out