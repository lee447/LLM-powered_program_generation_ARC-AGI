def solve(grid):
    h, w = len(grid), len(grid[0])
    def find_stripe(v):
        hr = max((r for r in range(h) if any(grid[r][c]==v for c in range(w))), key=lambda r: max((sum(1 for _ in grp) for val,grp in __import__('itertools').groupby(grid[r]) if val==v), default=0))
        vr = max((c for c in range(w) if any(grid[r][c]==v for r in range(h))), key=lambda c: max((sum(1 for _ in grp) for val,grp in __import__('itertools').groupby(grid[r][c] for r in range(h)) if val==v), default=0))
        lenv = max(sum(1 for _ in grp) for val,grp in __import__('itertools').groupby([grid[r][vr] for r in range(h)]) if val==v)
        return hr, vr, lenv
    for v in (4,3):
        try:
            hr, vr, sz = find_stripe(v)
            break
        except:
            pass
    br = hr+1; tr = br+sz
    lc = vr-sz; rc = vr
    block = [row[lc:rc] for row in grid[br:tr]]
    return block[::-1]