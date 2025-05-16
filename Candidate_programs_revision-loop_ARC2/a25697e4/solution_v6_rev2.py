from typing import List, Tuple
def solve(grid: List[List[int]]) -> List[List[int]]:
    h, w = len(grid), len(grid[0])
    bg = max({c: sum(row.count(c) for row in grid) for row in grid for c in row}, key=lambda c: sum(row.count(c) for row in grid))
    cols = [c for row in grid for c in row if c != bg]
    cols = sorted(set(cols), key=lambda c: sum(row.count(c) for row in grid))
    c_small, c_mid, c_large = cols[0], cols[1], cols[2]
    def bbox(color: int) -> Tuple[int,int,int,int]:
        rs = [i for i in range(h) for j in range(w) if grid[i][j] == color]
        cs = [j for i in range(h) for j in range(w) if grid[i][j] == color]
        return min(rs), min(cs), max(rs), max(cs)
    r1,c1,r2,c2 = bbox(c_mid)
    r3,c3,r4,c4 = bbox(c_small)
    r5,c5,r6,c6 = bbox(c_large)
    out = [row[:] for row in grid]
    for i in range(h):
        for j in range(w):
            if grid[i][j] in (c_mid,c_small):
                out[i][j] = bg
    def embed(src_bbox, tgt_bbox, color):
        r0, c0, r3, c3 = tgt_bbox
        r1, c1, r2, c2 = src_bbox
        src_h, src_w = r2-r1+1, c2-c1+1
        tgt_h = max(1,(r3-r0+1)-2)
        tgt_w = max(1,(c3-c0+1))
        for dy in range(tgt_h):
            for dx in range(tgt_w):
                sy = round(dy*(src_h-1)/max(1,tgt_h-1))
                sx = round(dx*(src_w-1)/max(1,tgt_w-1))
                if grid[r1+sy][c1+sx] == color:
                    out[r0+1+dy][c0+dx] = color
    embed((r1,c1,r2,c2),(r5,c5,r6,c6),c_mid)
    embed((r3,c3,r4,c4),(r1,c1,r2,c2),c_small)
    return out