def solve(grid):
    N, M = len(grid), len(grid[0])
    cnt = {}
    for i in range(N):
        for j in range(M):
            v = grid[i][j]
            if v not in (0,1,4):
                cnt[v] = cnt.get(v, 0) + 1
    accent = max(cnt, key=cnt.get) if cnt else None
    br = [i for i in range(N) if all(grid[i][j]==4 for j in range(M))]
    bc = [j for j in range(M) if all(grid[i][j]==4 for i in range(N))]
    def segments(boundaries, length):
        segs = []
        prev = -1
        for b in boundaries + [length]:
            if b - prev > 1:
                segs.append((prev+1, b))
            prev = b
        return segs
    row_segs = segments(br, N)
    col_segs = segments(bc, M)
    res = [row[:] for row in grid]
    for rs, re in row_segs:
        for cs, ce in col_segs:
            h = re - rs
            w = ce - cs
            if h!=w or h<1: continue
            has_accent = any(res[i][j]==accent for i in range(rs, re) for j in range(cs, ce))
            if has_accent: continue
            # main diag
            if all(grid[rs+i][cs+i]==1 for i in range(h)):
                for i in range(h):
                    res[rs+i][cs+i] = accent
            # sec diag
            elif all(grid[rs+i][cs+w-1-i]==1 for i in range(h)):
                for i in range(h):
                    res[rs+i][cs+w-1-i] = accent
    return res