from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    H = len(grid)
    W = len(grid[0])
    ys = []
    for y in range(H):
        if any(v not in (0,5) for v in grid[y]):
            ys.append(y)
    xs0 = []
    lengths = []
    patterns = []
    for y in ys:
        row = grid[y]
        xs = [i for i,v in enumerate(row) if v not in (0,5)]
        x0 = min(xs)
        x1 = max(xs)+1
        xs0.append(x0)
        pat = row[x0:x1]
        patterns.append(pat)
        lengths.append(len(pat))
    dx = xs0[1]-xs0[0] if len(xs0)>1 else 0
    dxl = lengths[1]-lengths[0] if len(lengths)>1 else 0
    const_len = all(l==lengths[0] for l in lengths)
    uniform = all(len(set(p))==1 for p in patterns)
    if const_len:
        next_len = lengths[0]
    else:
        next_len = lengths[-1] + dxl
    next_x0 = xs0[-1] + dx
    if const_len:
        pattern = patterns[0][:]
    else:
        pattern = [patterns[0][0]]*next_len if uniform else patterns[-1][:]
    out = [[0]*W for _ in range(3)]
    for i,v in enumerate(pattern):
        if 0 <= next_x0+i < W:
            out[1][next_x0+i] = v
    return out