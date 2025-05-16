import numpy as np
from typing import List
def solve(grid: List[List[int]]) -> List[List[int]]:
    g = np.array(grid)
    h, w = g.shape
    colors = [c for c in np.unique(g) if c != 0]
    def find_rods():
        rods = []
        for c in colors:
            mask = (g == c)
            for r in range(h):
                consec = max((sum(1 for _ in group) for val, group in __import__('itertools').groupby(mask[r,:]) if val), default=0)
                if consec >= 3:
                    rods.append(('h', c, r))
                    break
            for col in range(w):
                consec = max((sum(1 for _ in group) for val, group in __import__('itertools').groupby(mask[:,col]) if val), default=0)
                if consec >= 3:
                    rods.append(('v', c, col))
                    break
        return rods
    rods = find_rods()
    hrods = [r for r in rods if r[0]=='h']
    vrods = [r for r in rods if r[0]=='v']
    if hrods and vrods:
        _, hc, hr = hrods[0]
        _, vc, vc_col = vrods[0]
        row_vals = np.where(g[hr]==hc)[0]
        col_vals = np.where(g[:,vc_col]==vc)[0]
        c_start, c_end = row_vals.min(), row_vals.max()
        r_start, r_end = col_vals.min(), col_vals.max()
        if hr < r_start:
            g[:hr, c_start:c_end+1] = 0
        else:
            g[r_start:r_end+1, vc_col+1:] = hc
    return g.tolist()