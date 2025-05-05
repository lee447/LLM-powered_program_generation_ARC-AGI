from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    H, W = len(grid), len(grid[0])
    cols = sorted({grid[r][c] for r in range(H) for c in range(W) if grid[r][c] != 0})
    def bbox(val):
        rs, cs = [], []
        for r in range(H):
            for c in range(W):
                if grid[r][c] == val:
                    rs.append(r); cs.append(c)
        return min(rs), max(rs), min(cs), max(cs)
    b0 = bbox(cols[0])
    b1 = bbox(cols[1])
    if b0[2] < b1[2]:
        rL0, rL1, cL0, cL1 = b0
        rR0, rR1, cR0, cR1 = b1
    else:
        rL0, rL1, cL0, cL1 = b1
        rR0, rR1, cR0, cR1 = b0
    blockL = [grid[r][cL0:cL1+1] for r in range(rL0, rL1+1)]
    blockR = [grid[r][cR0:cR1+1] for r in range(rR0, rR1+1)]
    def pick_strip(block):
        h = len(block)
        if h == 3:
            return block[1][:3]
        else:
            return block[0][:3]
    def trunc(row):
        cnt = 0
        out = []
        for x in row:
            if x != 0:
                cnt += 1
            out.append(x if cnt <= 2 else 0)
        return out
    stripL = trunc(pick_strip(blockL))
    stripR = trunc(pick_strip(blockR))
    return [stripL, stripR, [0,0,0]]