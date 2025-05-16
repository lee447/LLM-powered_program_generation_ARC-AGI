from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    n, m = len(grid), len(grid[0])
    def fence_color():
        candidates = []
        for c in set(x for row in grid for x in row):
            rows = sum(1 for i in range(n) if sum(1 for v in grid[i] if v == c) > m//2)
            cols = sum(1 for j in range(m) if sum(1 for i in range(n) if grid[i][j] == c) > n//2)
            if rows == cols and rows > 1:
                candidates.append(c)
        return candidates[0] if candidates else None
    fence = fence_color()
    row_f = [i for i in range(n) if sum(1 for v in grid[i] if v == fence) > m//2]
    col_f = [j for j in range(m) if sum(1 for i in range(n) if grid[i][j] == fence) > n//2]
    rk = [0] + row_f + [n]
    ck = [0] + col_f + [m]
    R, C = len(rk)-1, len(ck)-1
    bh = max(rk[i+1]-rk[i]-1 for i in range(R))
    bw = max(ck[j+1]-ck[j]-1 for j in range(C))
    out = [[0]*(bw*C) for _ in range(bh*R)]
    legend = {}
    for br in range(R):
        for bc in range(C):
            r0, c0 = rk[br]+1, ck[bc]+1
            block = [grid[i][c0:c0+bw] for i in range(r0, r0+bh) if i < n]
            cnt = {}
            mask = [[0]*bw for _ in range(bh)]
            for i in range(len(block)):
                for j in range(len(block[0])):
                    v = block[i][j]
                    if v != fence and v != 0:
                        cnt[v] = cnt.get(v,0) + 1
                        mask[i][j] = 1
            if br == R-1:
                for v,k in cnt.items():
                    legend[bc] = v
            else:
                if cnt:
                    color = legend.get(bc, max(cnt, key=cnt.get))
                    for i in range(bh):
                        for j in range(bw):
                            if mask[i][j]:
                                out[br*bh+i][bc*bw+j] = color
    return out