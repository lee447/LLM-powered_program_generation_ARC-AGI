import numpy as np
from collections import defaultdict

def solve(grid):
    g = np.array(grid)
    R, C = g.shape
    row_map = defaultdict(list)
    for i in range(R):
        key = tuple(g[i, :])
        row_map[key].append(i)
    sep_r = sorted([i for key, idxs in row_map.items() if len(idxs) > 1 and len(set(key)) <= 2 for i in idxs])
    col_map = defaultdict(list)
    for j in range(C):
        key = tuple(g[:, j])
        col_map[key].append(j)
    sep_c = sorted([j for key, idxs in col_map.items() if len(idxs) > 1 and len(set(key)) <= 2 for j in idxs])
    r0s = [0] + [i+1 for i in sep_r] 
    r1s = sep_r + [R]
    c0s = [0] + [j+1 for j in sep_c]
    c1s = sep_c + [C]
    blocks = []
    for r0, r1 in zip(r0s, r1s):
        row = []
        for c0, c1 in zip(c0s, c1s):
            row.append(g[r0:r1, c0:c1])
        blocks.append(row)
    patterns = {}
    order = []
    for br in blocks:
        for b in br:
            m = b.max()
            pat = tuple(map(tuple, (b == m).astype(int)))
            if pat not in patterns:
                patterns[pat] = None
                order.append(pat)
    colors = {}
    for i, pat in enumerate(order):
        colors[pat] = pat and pat[0][0] or 0
    bh = max(b.shape[0] for row in blocks for b in row)
    bw = max(b.shape[1] for row in blocks for b in row)
    H = len(blocks) * bh
    W = len(blocks[0]) * bw
    out = np.zeros((H, W), int)
    for i, brow in enumerate(blocks):
        for j, b in enumerate(brow):
            m = b.max()
            pat = tuple(map(tuple, (b == m).astype(int)))
            mask = np.zeros((bh, bw), bool)
            h, w = b.shape
            mask[:h, :w] = (b == m)
            out[i*bh:(i+1)*bh, j*bw:(j+1)*bw][mask] = colors[pat]
    return out.tolist()