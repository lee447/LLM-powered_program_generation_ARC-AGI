from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    rs = [i for i in range(n) if all(grid[i][j] == 0 for j in range(m))]
    cs = [j for j in range(m) if all(grid[i][j] == 0 for i in range(n))]
    rs.sort(); cs.sort()
    out = [row[:] for row in grid]
    for bi in range(len(rs) - 1):
        r0, r1 = rs[bi] + 1, rs[bi+1]
        for bj in range(len(cs) - 1):
            c0, c1 = cs[bj] + 1, cs[bj+1]
            counts = {}
            for i in range(r0, r1):
                for j in range(c0, c1):
                    v = out[i][j]
                    if v:
                        counts[v] = counts.get(v, 0) + 1
            if not counts:
                continue
            bg = max(counts.items(), key=lambda x: x[1])[0]
            motif = [(i, j, out[i][j]) for i in range(r0, r1) for j in range(c0, c1) if out[i][j] and out[i][j] != bg]
            mc = {}
            for _, _, v in motif:
                mc[v] = mc.get(v, 0) + 1
            maj = next((k for k, c in mc.items() if c > 1), None)
            mis = next((k for k, c in mc.items() if c == 1), None)
            if maj is None or mis is None:
                continue
            for i, j, v in motif:
                if v == maj:
                    out[i][j] = mis
    return out