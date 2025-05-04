def solve(grid):
    R, C = len(grid), len(grid[0])
    from collections import Counter
    cnt = Counter(c for row in grid for c in row)
    bad = min((c for c in cnt if 0 < cnt[c] < R*C//4), key=lambda c: cnt[c])
    rs = [r for r in range(R) for c in range(C) if grid[r][c]==bad]
    cs = [c for r in range(R) for c in range(C) if grid[r][c]==bad]
    r0, r1 = min(rs), max(rs)
    c0, c1 = min(cs), max(cs)
    h, w = r1-r0+1, c1-c0+1
    # pick the untouched block in same column or same row
    def find_block(color):
        rs2 = [r for r in range(R) for c in range(C) if grid[r][c]==color]
        if not rs2: return None
        ra, rb = min(rs2), max(rs2)
        ca, cb = min([c for r in range(R) for c in range(C) if grid[r][c]==color]), max([c for r in range(R) for c in range(C) if grid[r][c]==color])
        return ra, ca
    for col in (c0,):
        top = find_block(bad)
        for r in range(0, R-h+1):
            sub = [row[col:col+w] for row in grid[r:r+h]]
            flat = [x for row in sub for x in row]
            if bad not in flat:
                ans = [row[col:col+3] for row in grid[r+ h-1 : r-1 : -1][:3]]
                return ans
    return []