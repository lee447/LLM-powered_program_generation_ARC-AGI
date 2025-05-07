from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    freq = {}
    for r in range(h):
        for c in range(w):
            v = grid[r][c]
            if v != 0:
                freq[v] = freq.get(v, 0) + 1
    sep = max(freq, key=lambda k: freq[k])
    row_seps = [r for r in range(h) if sum(1 for v in grid[r] if v == sep) > w//2]
    col_seps = [c for c in range(w) if sum(1 for r in range(h) if grid[r][c] == sep) > h//2]
    rs = [-1] + row_seps + [h]
    cs = [-1] + col_seps + [w]
    counts = {}
    for i in range(len(rs)-1):
        r0, r1 = rs[i]+1, rs[i+1]
        if r0 >= r1: continue
        for j in range(len(cs)-1):
            c0, c1 = cs[j]+1, cs[j+1]
            if c0 >= c1: continue
            seen = None
            for r in range(r0, r1):
                for c in range(c0, c1):
                    v = grid[r][c]
                    if v != 0 and v != sep:
                        seen = v
                        break
                if seen is not None:
                    break
            if seen is not None:
                counts[seen] = counts.get(seen, 0) + 1
    items = sorted(counts.items(), key=lambda x: x[1])
    if not items:
        return []
    maxc = max(cnt for _, cnt in items)
    out = []
    for v, cnt in items:
        row = [v]*cnt + [0]*(maxc-cnt)
        out.append(row)
    return out