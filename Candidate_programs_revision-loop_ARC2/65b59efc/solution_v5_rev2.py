import numpy as np
from typing import List

def solve(grid: List[List[int]]) -> List[List[int]]:
    g = np.array(grid)
    sep_r = [i for i,row in enumerate(g) if set(row) <= {0,5}]
    sep_c = [j for j,col in enumerate(g.T) if set(col) <= {0,5}]
    keep_r = [i for i in range(g.shape[0]) if i not in sep_r]
    keep_c = [j for j in range(g.shape[1]) if j not in sep_c]
    sub = g[np.ix_(keep_r, keep_c)]
    h, w = sub.shape
    bh = h // 3
    bw = w // 3
    hints_row = sub[-1, :].reshape(3, bw).mean(axis=1).astype(int)
    hints_col = sub[:, -1].reshape(bh, 3).mean(axis=0).astype(int)
    body = sub[:-1, :-1]
    out = np.zeros_like(body)
    for bi in range(3):
        for bj in range(3):
            block = body[bi*bh:(bi+1)*bh, bj*bw:(bj+1)*bw]
            m = block.max()
            mask = (block == m)
            color = hints_row[bj] if bi < 2 else hints_col[bi]
            out[bi*bh:(bi+1)*bh, bj*bw:(bj+1)*bw][mask] = color
    return out.tolist()