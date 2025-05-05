from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    rs = [i for i in range(n) if all(grid[i][j] == 0 for j in range(m))]
    cs = [j for j in range(m) if all(grid[i][j] == 0 for i in range(n))]
    out = [row[:] for row in grid]
    R = len(rs) - 1
    C = len(cs) - 1
    for br in range(R):
        for bc in range(C):
            r0, r1 = rs[br], rs[br+1]
            c0, c1 = cs[bc], cs[bc+1]
            r_lo, r_hi = r0+1, r1-1
            c_lo, c_hi = c0+1, c1-1
            region = [(i,j) for i in (r_lo, r_hi) for j in (c_lo, c_hi)]
            vals = [out[i][j] for i,j in region]
            cnt = {}
            for v in vals:
                cnt[v] = cnt.get(v, 0) + 1
            if len(cnt) != 2:
                continue
            items = sorted(cnt.items(), key=lambda x: x[1])
            mis, maj = items[0][0], items[1][0]
            pts_maj = [(i,j) for i,j in region if out[i][j] == maj]
            if len(pts_maj) != 3:
                continue
            anti_bc = C-1-bc
            rr0, rr1 = rs[br], rs[br+1]
            cc0, cc1 = cs[anti_bc], cs[anti_bc+1]
            r_lo2, r_hi2 = rr0+1, rr1-1
            c_lo2, c_hi2 = cc0+1, cc1-1
            region2 = [(i,j) for i in (r_lo2, r_hi2) for j in (c_lo2, c_hi2)]
            vals2 = [out[i][j] for i,j in region2]
            cnt2 = {}
            for v in vals2:
                cnt2[v] = cnt2.get(v, 0) + 1
            Z = max(cnt2.items(), key=lambda x: x[1])[0]
            mi = min(i+j for i,j in region)
            ma = max(i+j for i,j in region)
            for i,j in pts_maj:
                if i+j != ma:
                    out[i][j] = Z
    return out